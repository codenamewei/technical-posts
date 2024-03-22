
from functools import lru_cache
from coreengine.mapping.data.projectconfig import ProjectConfig
from coreengine.utils import jsonops
import os

#----------- project-----------
@lru_cache 
def get_project_config() -> ProjectConfig:
    
    projectconfig = ProjectConfig()

    return projectconfig

@lru_cache
def get_model():
    import tensorflow as tf

    modelabspath = os.path.join(get_project_config().PROJECT_DATA_PATH, get_project_config().MODEL_PATH)

    if not os.path.exists(modelabspath):

        raise FileNotFoundError(f"Model path {modelabspath} not found")
    
    model = tf.keras.models.load_model(modelabspath)

    return model

@lru_cache
def get_lookup_table() -> dict[str, list[str]]:

    keyvalue = dict()
    jsonsuffix = ".json"
    lookupabspath = os.path.join(get_project_config().PROJECT_DATA_PATH, get_project_config().LOOKUP_PATH)

    
    if not os.path.exists(lookupabspath):

        raise FileNotFoundError(f"Lookup path {lookupabspath} not found")
    
    tuple_files = os.walk(lookupabspath)


    for item in tuple_files:

        for file in item[2]:

            if file.endswith(jsonsuffix):

                key : str = file.split(".")[0].upper()
                key = key[:-2]

                values : list[str] = jsonops.read_list_from_json(os.path.join(item[0], file))

                keyvalue[key] = values

    return keyvalue

@lru_cache
def get_furniture_master_df():# -> pl.DataFrame:
    import polars as pl
    masterpath = os.path.join(get_project_config().PROJECT_DATA_PATH, get_project_config().LOOKUP_PATH, get_project_config().FURNITURE_MAPPING_FILE)
    return pl.read_csv(masterpath)

#temporary


@lru_cache
def get_groundtruth_df():# -> pl.DataFrame:

    import polars as pl
    from coreengine.mapping.data.maptype.catalogmaptype import CatalogMapType
    from coreengine.datacleaning import standardizelookup

    masterpath = os.path.join(get_project_config().PROJECT_DATA_PATH, get_project_config().GROUNDTRUTH_FURNITURE_PER_PROJECT)

    df = pl.read_csv(masterpath)

    column_mapping = standardizelookup.get_catalog_column_value_mapping(CatalogMapType.CATEGORY)

    df = df.filter(pl.col("CATEGORY").is_in(list(column_mapping.values())))

    return df