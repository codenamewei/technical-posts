
from coreengine.datacleaning import standardizelookup
from coreengine.mapping.data.maptype.catalogmaptype import CatalogMapType
from coreengine.utils.rest.predictionitem import PredictionItem
from coreengine.utils import componentcache
from coreengine.ml import furniturebyspace
import random
import tensorflow as tf
import numpy as np
import polars as pl
import operator

prediction_column = "PREDICTION_SCORE"

ML_FEATURES = [CatalogMapType.MAIN_ACTIVITIES, CatalogMapType.STYLE]


OUTPUT_FEATURES = [CatalogMapType.PRICE_RANGE, CatalogMapType.HARDNESS, CatalogMapType.LEG_PRESENCE, CatalogMapType.MOOD, 
                   CatalogMapType.NUM_USERS, CatalogMapType.COLOR, CatalogMapType.STYLE, CatalogMapType.SOFA_TYPE, 
                   CatalogMapType.BED_TYPE, CatalogMapType.FLOOR_LAMP_TYPE, CatalogMapType.PENDANT_LAMP_TYPE, CatalogMapType.LOUNGE_CHAIR_TYPE, 
                   CatalogMapType.SHAPE, CatalogMapType.TABLE_TOP_SHAPE, CatalogMapType.TABLE_FRAME_TYPE, CatalogMapType.CHAIR_BACK_SHAPE, 
                   CatalogMapType.ARMREST_PRESENCE, CatalogMapType.FOOTSTOOL_PRESENCE, CatalogMapType.STORAGE_CLASS,
                   CatalogMapType.STORAGE_DOOR_TYPE, CatalogMapType.LIGHT_BULB_PRESENCE, CatalogMapType.LIGHTING_METHOD, CatalogMapType.MATERIAL]

BINARY_OUTPUT_FEATURES = [CatalogMapType.PRICE_RANGE, CatalogMapType.LEG_PRESENCE,CatalogMapType.NUM_USERS, CatalogMapType.PENDANT_LAMP_TYPE, CatalogMapType.LOUNGE_CHAIR_TYPE,CatalogMapType.TABLE_FRAME_TYPE, CatalogMapType.CHAIR_BACK_SHAPE, 
                   CatalogMapType.ARMREST_PRESENCE, CatalogMapType.FOOTSTOOL_PRESENCE, CatalogMapType.STORAGE_CLASS, CatalogMapType.LIGHT_BULB_PRESENCE, CatalogMapType.LIGHTING_METHOD ]



def invert_multi_hot(encoded_labels: list, top_n : int,features: list[str]) -> (list[str], list[str]):
    
    # Enumerate the list to get (index, value) pairs
    enumerated_list = list(enumerate(encoded_labels))

    # Sort the list based on the values in descending order
    sorted_list = sorted(enumerated_list, key=lambda x: x[1], reverse=True)
    # Get the indices of the top three elements
    top_n_indices, top_n_confidences = [], []

    for i in range(top_n):
        
        index, value =  sorted_list[i]
        
        
        if value > componentcache.get_project_config().CONFIDENCE_THRESHOLD:
    
            # Get the indices of the top three elements
            top_n_indices.append(index)

            top_n_confidences.append(int(value * 100))

    labels = list(map(lambda x : features[x], top_n_indices))
        
    return labels, top_n_confidences
        
def _encode_single_data(keyvalue: dict[str, list[str] | str]) -> np.array:

    feature_array = np.array([])

    for i, catalog_ref in enumerate(ML_FEATURES):
        
        
        column_mapping = standardizelookup.get_catalog_column_value_mapping(catalog_ref, key_as_eng = True)

        index = tf.keras.layers.StringLookup(vocabulary=list(column_mapping.keys()))
        encoder = tf.keras.layers.CategoryEncoding(num_tokens=index.vocabulary_size(), output_mode="multi_hot")
        
        raw_features = encoder(index(keyvalue[catalog_ref.value]))
        

        feature_array = np.concatenate((feature_array, raw_features), axis=None)

    return np.array([feature_array], dtype=np.float32)

def predict_single_data(keyvalue: dict[str, list[str] | str]) -> list[PredictionItem]:

    input_features = _encode_single_data(keyvalue)

    properties = dict()


    raw_prediction = componentcache.get_model().predict(input_features)
    
    for i, output_feature in enumerate(OUTPUT_FEATURES):
        
        if output_feature in BINARY_OUTPUT_FEATURES:
            properties[output_feature.value], confidences = invert_multi_hot(raw_prediction[i][0].tolist(), 1, componentcache.get_lookup_table()[output_feature.value])
        else:
            properties[output_feature.value], confidences = invert_multi_hot(raw_prediction[i][0].tolist(), componentcache.get_project_config().TOP_N, componentcache.get_lookup_table()[output_feature.value])

    return _filter_list(selected_features = properties, space = keyvalue["SPACE"])

def _convert_to_predictionitem(df : pl.DataFrame) -> list[PredictionItem]:
    
    if df.shape[0] == 0:

        return list()
    
    column_mapping = standardizelookup.get_catalog_column_value_mapping(CatalogMapType.CATEGORY, key_as_eng = True)
    
    predictionitems = list()
    for row in df.iter_rows():
        predictionitems.append(PredictionItem(product_name = row[0], category = column_mapping[row[1]], product_id = int(row[2]), price = int(row[3]), url = row[4], prediction_score = row[5]))
    
    
    return predictionitems

def _filter_list(selected_features : dict[str, list[str] | str], space : str) -> list[PredictionItem]:


    df = componentcache.get_furniture_master_df()

    # [POST-PROCESSSING]: filtered excluded furniture by space
    excluded_furnitures = furniturebyspace.get_furniture_by_space(space)

    filteredmasterdf = df.filter(
    ~pl.col(CatalogMapType.CATEGORY.value).is_in(excluded_furnitures),)
    # Compute Score of all furnitures

    SCORE_SUFFIX = "_SCORE"
    column_score = []

    for column_name, selection in selected_features.items():


        this_column_score = column_name + SCORE_SUFFIX
        column_score.append(this_column_score)
        
        def filterfunc(raw_input) -> float:
            
            if raw_input.find("[") != -1:
            
                raw_input = eval(raw_input)
                
                score = 0
                
                for feature in raw_input:
                
                    if feature in selection:

                        score = score + 1

                return score / (len(selection) + len(raw_input) - score)
                
            else:

                return 1 if raw_input in selection else 0

        filteredmasterdf = filteredmasterdf.with_columns(  

        pl.col(column_name).map_elements(filterfunc).alias(this_column_score),
        
        )

        filteredmasterdf = filteredmasterdf.with_columns(pl.col(this_column_score).fill_null(0))

    #print(filteredmasterdf["STYLE_SCORE"].unique().to_list())
    #print(filteredmasterdf["PRICE_RANGE_SCORE"].unique().to_list())

    sumarray = [0] * filteredmasterdf.shape[0]
    
    for column in column_score:
        sumarray = list(map(operator.add, sumarray, filteredmasterdf[column].to_list()))


    
    filteredmasterdf = filteredmasterdf.with_columns(pl.Series(name=prediction_column, values=sumarray)) 

    #print(filteredmasterdf[prediction_column].unique().to_list())


    #print(f"TOTAL_SCORE MIN: {min(filteredmasterdf[prediction_column].to_list())}")
    #print(f"TOTAL_SCORE MAX: {max(filteredmasterdf[prediction_column].to_list())}")

    columns = ["PRODUCT_NAME", "CATEGORY", "ID", "PRICE", "URL", prediction_column]
    filteredmasterdf = filteredmasterdf[columns]

    # --------------------------compute highest granularly (by category , w/wo price, w/wo randomness,  and # type per category)--------------------------
    category_column = CatalogMapType.CATEGORY.value
    unique_categories = filteredmasterdf[category_column].unique().to_list()

    #FIXME!!!!!!
    BUDGET_MIN = 6853800
    BUDGET_MAX = 10000000

    FACTOR_PRICE = componentcache.get_project_config().FACTOR_PRICE
    INCLUDE_RANDOM = componentcache.get_project_config().INCLUDE_RANDOM
    UNIT_PER_CATEGORY = componentcache.get_project_config().UNIT_PER_CATEGORY

    if componentcache.get_project_config().INCLUDE_RANDOM:
    
        random.seed()
        
    if componentcache.get_project_config().FACTOR_PRICE:

        print(f"Before trimming by price {filteredmasterdf.shape[0]}")

        # FIRST ROUND FILTERING TO EXCLUDE SINGLE ITEM THAT IS MORE EXPENSIVE THAT THE WHOLE BUDGET BY 80%
        CEIL_PRICE_BY_ITEM = 0.8 * BUDGET_MAX 
        
        filteredmasterdf = filteredmasterdf.filter(pl.col("PRICE") < CEIL_PRICE_BY_ITEM)


        print(f"After trimming by price {filteredmasterdf.shape[0]}")

    prediction_by_category = dict()


    for category in unique_categories:
        
        categorydf = filteredmasterdf.filter(pl.col(category_column) == category)
        
        categorydf = categorydf.sort(by = prediction_column, descending = True)
            
        prediction_by_category[category] = categorydf[:componentcache.get_project_config().TOP_N]
        

    # print(f"FACTOR_PRICE: {FACTOR_PRICE}")
    # print(f"INCLUDE_RANDOM: {INCLUDE_RANDOM}")
    # print(f"UNIT_PER_CATEGORY: {UNIT_PER_CATEGORY}")
        
    # Situation 1: x FACTOR_PRICE, x INCLUDE_RANDOM: only filter by UNIT_PER_CATEGORY for each category
    # Situation 2: x FACTOR_PRICE, o INCLUDE_RANDOM: filter by UNIT_PER_CATEGORY for each category 
    # Situation 3: o FACTOR_PRICE, x INCLUDE RANDOM: choose the highest score by UNIT_PER_CATEGORY in each category that satisfied the total sum
    # Situation 4: o FACTOR_PRICE, O INCLUDE_RANDOM: choose randomly by UNIT_PER_CATEGORY in each category that satisfied the total sum
    

    total_prediction_list : list[PredictionItem] = list()

    # Situation 1 & 2 
    if not FACTOR_PRICE:
        
        if not INCLUDE_RANDOM: 
            

            for table in prediction_by_category.values():
                total_prediction_list.extend(_convert_to_predictionitem(table[:UNIT_PER_CATEGORY]))
                
            
        else:
            
            
            for table in prediction_by_category.values():
                
                indexes = list(range(table.shape[0]))
                
                random.shuffle(indexes)
                
                total_prediction_list.extend(_convert_to_predictionitem(table[indexes[:UNIT_PER_CATEGORY]]))
                            
    # Situation 3 & 4 
    else: 
        #UNIT_PER_CATEGORY IS NOT IMPLEMENTED WHEN INCLUDING PRICE CALCULATION
        
        selected_index = dict(zip(prediction_by_category.keys(), [0] * len(prediction_by_category.keys())))
        break_init = False
        if not INCLUDE_RANDOM:
            
            index = 0
            to_random = False #toggle when increment of index does not result in results
            
            for i in range(0, 100): #iteration
            
                current_sum = 0
            
                for category, table in prediction_by_category.items():
                    
            
                    selected_index[category] = index if not to_random else random.randint(0, componentcache.get_project_config().TOP_N - 1)
                    
                    current_sum += table[selected_index[category]]["PRICE"][0]

                if (current_sum < BUDGET_MAX) & (current_sum > BUDGET_MIN):
                    break_init = True
                    break
                else:
                    index = index + 1
                    if index >= componentcache.get_project_config().TOP_N:
                                                                    
                        to_random = True
                                    
                                                                    
            if not break_init:
                
                print("DEBUGGING: CANNOT GET THE RIGHT BUDGET")
            
            
        else:
                                                                    
            for i in range(0, 100): #iteration
            
                current_sum = 0
            
                for category, table in prediction_by_category.items():
                    
                    selected_index[category] = random.randint(0, componentcache.get_project_config().TOP_N - 1)
                    
                    current_sum += table[selected_index[category]]["PRICE"][0]

                if (current_sum < BUDGET_MAX) & (current_sum > BUDGET_MIN):
                    break_init = True
                    break
                                    
                                                                    
            if not break_init:
                
                print("DEBUGGING: CANNOT GET THE RIGHT BUDGET")
                                                                   
        for category, row_index in selected_index.items():
            
                                                                        
            total_prediction_list.extend(_convert_to_predictionitem(prediction_by_category[category][row_index]))

    return total_prediction_list