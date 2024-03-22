from coreengine.mapping.data.maptype.catalogmaptype import CatalogMapType
from coreengine.mapping.ops import maphelper
from coreengine.mapping.ops.mapsequence import MapSequence
from coreengine.mapping.data.property.pricerangemap import PriceRangeMap
from coreengine.mapping.data.property.hardnessmap import HardnessMap
import enum

column_value_mapping : dict = {

    CatalogMapType.CATEGORY.value: CatalogMapType.CATEGORY,
    CatalogMapType.MATERIAL.value: CatalogMapType.MATERIAL,
    CatalogMapType.MOOD.value: CatalogMapType.MOOD,

    CatalogMapType.STYLE.value: CatalogMapType.STYLE,
    CatalogMapType.COLOR.value: CatalogMapType.COLOR,

    CatalogMapType.SHAPE.value: CatalogMapType.SHAPE,
    CatalogMapType.CHAIR_BACK_SHAPE.value: CatalogMapType.CHAIR_BACK_SHAPE,
    CatalogMapType.TABLE_TOP_SHAPE.value: CatalogMapType.TABLE_TOP_SHAPE,

    CatalogMapType.HARDNESS.value: HardnessMap, #enum
    CatalogMapType.PRICE_RANGE.value: CatalogMapType.PRICE_RANGE.value, #str
    CatalogMapType.BOOLEAN.value: True,

    CatalogMapType.BED_TYPE.value: CatalogMapType.BED_TYPE,
    CatalogMapType.FLOOR_LAMP_TYPE.value: CatalogMapType.FLOOR_LAMP_TYPE,
    CatalogMapType.LOUNGE_CHAIR_TYPE.value: CatalogMapType.LOUNGE_CHAIR_TYPE,
    CatalogMapType.PENDANT_LAMP_TYPE.value: CatalogMapType.PENDANT_LAMP_TYPE,
    CatalogMapType.SOFA_TYPE.value: CatalogMapType.SOFA_TYPE,

    CatalogMapType.STORAGE_DOOR_TYPE.value: CatalogMapType.STORAGE_DOOR_TYPE,
    CatalogMapType.TABLE_FRAME_TYPE.value: CatalogMapType.TABLE_FRAME_TYPE,
    CatalogMapType.LIGHTING_METHOD.value: CatalogMapType.LIGHTING_METHOD,

    CatalogMapType.STORAGE_CLASS.value: None,
    CatalogMapType.PROJECT_PROGRESS.value: CatalogMapType.PROJECT_PROGRESS,

    CatalogMapType.TYPE_OF_SPACE.value: CatalogMapType.TYPE_OF_SPACE,
    CatalogMapType.MAIN_ACTIVITIES.value: CatalogMapType.MAIN_ACTIVITIES,
    CatalogMapType.PROJECT_PROGRESS.value: CatalogMapType.PROJECT_PROGRESS,

    CatalogMapType.LEG_PRESENCE.value: True,
    CatalogMapType.ARMREST_PRESENCE.value: True,
    CatalogMapType.FOOTSTOOL_PRESENCE.value: True,
    CatalogMapType.LIGHT_BULB_PRESENCE.value: True

}

"""
key: column_name
value: key value mapping of property / boolean (need to be special build) / and other type


- unresolved: what if column_name not found?
"""

def get_catalog_column_value_mapping(column_name : CatalogMapType, value_as_int : bool = False, key_as_eng : bool = False) -> dict[str, str]:
    """
    second return value is the default value to be placed if the key value pair is not found
    """

    if column_name.value not in column_value_mapping.keys():

        raise ValueError(f"{column_name} not found in column value mapping")
    
    valuetype = column_value_mapping[column_name.value]

    if key_as_eng and not isinstance(valuetype, CatalogMapType):

        raise ValueError("Only CatalogMapType can have english as key value")


    if isinstance(valuetype, CatalogMapType):

        if key_as_eng:

            eng2kor_mapping = maphelper.get_tag_map(valuetype, MapSequence.ENG2KOR)

            if value_as_int:

                int_value_list : list[int] = list(range(len(eng2kor_mapping)))

                eng2int_mapping = dict(zip(eng2kor_mapping.keys(), int_value_list))
            
                return eng2int_mapping

            else:

                return eng2kor_mapping

        else:

            kor2value_mapping = maphelper.get_tag_map(valuetype, MapSequence.KOR2ENG)

            if value_as_int:

                int_value_list : list[int] = list(range(len(kor2value_mapping)))

                kor2value_mapping = dict(zip(kor2value_mapping.keys(), int_value_list))


            if column_name.value == CatalogMapType.STYLE.value:

                substituted_key, substituted_value = list(), list()

                for k, v in kor2value_mapping.items():
                    
                    if k.find("네추럴") != -1:

                        substituted_key.append(k.replace("네추럴", "내추럴")) 

                        substituted_value.append(v)

                    if k.find("센추리") != -1:

                        substituted_key.append(k.replace("센추리", "센츄리")) 

                        substituted_value.append(v)


                if substituted_key:

                    for k, v in zip(substituted_key, substituted_value):
                        kor2value_mapping[k] = v

            elif column_name.value == CatalogMapType.MATERIAL.value:

                kor2value_mapping["스틸"] = kor2value_mapping["스틸/금속"]

            
            elif column_name.value == CatalogMapType.COLOR.value:   

                kor2value_mapping["브라우톤"] = kor2value_mapping["브라운톤"]

    
            return kor2value_mapping
    elif isinstance(valuetype, enum.EnumMeta):

        kor2eng_mapping = maphelper.get_enum_map(valuetype)

        if value_as_int:

            int_value_list : list[int] = list(range(len(kor2eng_mapping)))

            kor2int_mapping = dict(zip(kor2eng_mapping.keys(), int_value_list))

            return kor2int_mapping

        else:

            return kor2eng_mapping
        

    elif isinstance(valuetype, bool):


        korean_no = ["NO", "무"]
        korean_yes = ["YES", "유"]
        korean_none = ["NONE"]

        kor_list = korean_no + korean_yes# + korean_none

        if not value_as_int:
            eng_list = ["NO"] * len(korean_no) + ["YES"] * len(korean_yes) + korean_none
        else:
            eng_list = [0]  * len(korean_no) + [1] * len(korean_yes) + korean_none

        return dict(zip(kor_list, eng_list))
    
    elif isinstance(valuetype, str):

        if valuetype == CatalogMapType.PRICE_RANGE.value:

            high_end = ["HIGH-END"]
            masstige = ["MASTIGE", "MASSTIGE"]
            premium = ["PREMIUM"]

            kor_list = high_end + masstige + premium

            if not value_as_int:
                eng_list = [PriceRangeMap.HIGHEND.value] * len(high_end) + [PriceRangeMap.MASSTIGE.value] * len(masstige) + [PriceRangeMap.PREMIUM.value] * len(premium)
            else:
                eng_list = [0]  * len(high_end) + [1] * len(masstige) + [2] * len(premium)

            return dict(zip(kor_list, eng_list))