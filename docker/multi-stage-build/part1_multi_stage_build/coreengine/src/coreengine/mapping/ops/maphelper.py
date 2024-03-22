from .mapsequence import MapSequence
from coreengine.mapping.data.maptype.catalogmaptype import CatalogMapType
from . import mapdata
import logging
import enum

def get_tag_map(maptype : CatalogMapType, sequence : MapSequence) -> dict[str, str]:
    
    mapkeyvalue = get_catalog_map(maptype)

    if sequence is MapSequence.KOR2ENG:
        mapkeyvalue = {v: k for k, v in mapkeyvalue.items()}

    return mapkeyvalue

def get_enum_map(enumtype : enum.EnumMeta) -> dict:
    
    mapkeyvalue = dict(zip([e.name for e in enumtype], [e.value for e in enumtype]))

    return mapkeyvalue

def get_catalog_map(maptype: CatalogMapType) -> dict[str, str]:

    match maptype:

        case CatalogMapType.CATEGORY:

            return mapdata.get_category_map()
          
        case CatalogMapType.MATERIAL:

            return mapdata.get_material_map()

        case CatalogMapType.STYLE:

            return mapdata.get_style_map()
         
        case CatalogMapType.MOOD:

            return mapdata.get_mood_map()
        
        case CatalogMapType.COLOR:
            
            return mapdata.get_color_map()

        case CatalogMapType.SHAPE:

            return mapdata.get_shape_map()
         
        case CatalogMapType.LIGHTING_METHOD:
            
            return mapdata.get_lightingmethod_map()
        
        case CatalogMapType.SOFA_TYPE:

            return mapdata.get_sofatype_map()

        case CatalogMapType.PENDANT_LAMP_TYPE:

            return mapdata.get_pendantlamptype_map()
         
        case CatalogMapType.LOUNGE_CHAIR_TYPE:

            return mapdata.get_loungechairtype_map()
        
        case CatalogMapType.FLOOR_LAMP_TYPE:
            
            return mapdata.get_floorlamptype_map()

        case CatalogMapType.BED_TYPE:

            return mapdata.get_bedtype_map()
        
        case CatalogMapType.CHAIR_BACK_SHAPE:

            return mapdata.get_chairbackshape_map()
        
        case CatalogMapType.TABLE_TOP_SHAPE:
            
            return mapdata.get_tabletopshape_map()

        case CatalogMapType.STORAGE_DOOR_TYPE:

            return mapdata.get_storagedoortype_map()
        
        case CatalogMapType.TABLE_FRAME_TYPE:

            return mapdata.get_tableframetype_map()
        
        case CatalogMapType.INPUT_TAG:

            return mapdata.get_input_tag_map()

        case CatalogMapType.OUTPUT_TAG:

            return mapdata.get_output_tag_map()
        
        case CatalogMapType.OUTPUT_FEATURE_TAG:

            return mapdata.get_output_feature_tag_map()
        
        case CatalogMapType.PRODUCT_TAG:

            return mapdata.get_product_tag_map()
        
         
        case CatalogMapType.TYPE_OF_SPACE:

            return mapdata.get_spacetype_map()
        
        case CatalogMapType.MAIN_ACTIVITIES:

            return mapdata.get_activity_map()
        
        case CatalogMapType.PROJECT_PROGRESS:

            return mapdata.get_projectprogress_map()        

        case default:

            logging.error("No map have been chosen")
            raise ValueError(f"Invalid map type input: {maptype}")

