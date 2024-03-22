from coreengine.mapping.data.header.furnituremap import FurnitureMap
from coreengine.mapping.data.header.inputtagmap import InputTagMap
from coreengine.mapping.data.header.outputtagmap import OutputTagMap
from coreengine.mapping.data.header.outputfeaturetagmap import OutputFeatureTagMap
from coreengine.mapping.data.header.producttagmap import ProductTagMap
from coreengine.mapping.data.property.materialmap import MaterialMap
from coreengine.mapping.data.property.stylemap import StyleMap
from coreengine.mapping.data.property.moodmap import MoodMap
from coreengine.mapping.data.property.colormap import ColorMap
from coreengine.mapping.data.property.shapemap import ShapeMap
from coreengine.mapping.data.property.tabletopshapemap import TableTopShapeMap
from coreengine.mapping.data.property.chairbackshapemap import ChairBackShapeMap
from coreengine.mapping.data.property.colormap import ColorMap
from coreengine.mapping.data.property.lightingmethodmap import LightingMethodMap
from coreengine.mapping.data.property.activitymap import ActivityMap
from coreengine.mapping.data.property.projectprogressmap import ProjectProgressMap
from coreengine.mapping.data.property.type.bedtypemap import BedTypeMap
from coreengine.mapping.data.property.type.floorlamptypemap import FloorLampTypeMap
from coreengine.mapping.data.property.type.loungechairtypemap import LoungeChairTypeMap
from coreengine.mapping.data.property.type.pendantlamptypemap import PendantLampTypeMap
from coreengine.mapping.data.property.type.sofatypemap import SofaTypeMap
from coreengine.mapping.data.property.type.spacetypemap import SpaceTypeMap
from coreengine.mapping.data.property.type.storagedoortypemap import StorageDoorTypeMap
from coreengine.mapping.data.property.type.tableframetypemap import TableFrameTypeMap



from functools import lru_cache


@lru_cache 
def get_category_map() -> dict[str, str]:
    
    mapkeyvalue = FurnitureMap()

    return mapkeyvalue.model_dump()

@lru_cache 
def get_input_tag_map() -> dict[str, str]:
    
    mapkeyvalue = InputTagMap()

    return mapkeyvalue.model_dump()


@lru_cache 
def get_output_tag_map() -> dict[str, str]:
      
    mapkeyvalue = OutputTagMap()

    return mapkeyvalue.model_dump()



@lru_cache 
def get_output_feature_tag_map() -> dict[str, str]:
    
    mapkeyvalue = OutputFeatureTagMap()

    return mapkeyvalue.model_dump()


@lru_cache 
def get_product_tag_map() -> dict[str, str]:
    
    mapkeyvalue = ProductTagMap()

    return mapkeyvalue.model_dump()


@lru_cache 
def get_material_map() -> dict[str, str]:
    
    mapkeyvalue = MaterialMap()

    return mapkeyvalue.model_dump()


@lru_cache 
def get_style_map() -> dict[str, str]:
    
    mapkeyvalue = StyleMap()

    return mapkeyvalue.model_dump()


@lru_cache 
def get_mood_map() -> dict[str, str]:
    
    mapkeyvalue = MoodMap()

    return mapkeyvalue.model_dump()



@lru_cache 
def get_color_map() -> dict[str, str]:
    
    mapkeyvalue = ColorMap()

    return mapkeyvalue.model_dump()




@lru_cache 
def get_shape_map() -> dict[str, str]:
    
    mapkeyvalue = ShapeMap()

    return mapkeyvalue.model_dump()


@lru_cache 
def get_chairbackshape_map() -> dict[str, str]:
    
    mapkeyvalue = ChairBackShapeMap()

    return mapkeyvalue.model_dump()



@lru_cache 
def get_tabletopshape_map() -> dict[str, str]:
    
    mapkeyvalue = TableTopShapeMap()

    return mapkeyvalue.model_dump()


@lru_cache 
def get_bedtype_map() -> dict[str, str]:
    
    mapkeyvalue = BedTypeMap()

    return mapkeyvalue.model_dump()

@lru_cache 
def get_floorlamptype_map() -> dict[str, str]:
    
    mapkeyvalue = FloorLampTypeMap()

    return mapkeyvalue.model_dump()

@lru_cache 
def get_loungechairtype_map() -> dict[str, str]:
    
    mapkeyvalue = LoungeChairTypeMap()

    return mapkeyvalue.model_dump()

@lru_cache 
def get_pendantlamptype_map() -> dict[str, str]:
    
    mapkeyvalue = PendantLampTypeMap()

    return mapkeyvalue.model_dump()

@lru_cache 
def get_sofatype_map() -> dict[str, str]:
    
    mapkeyvalue = SofaTypeMap()

    return mapkeyvalue.model_dump()


@lru_cache 
def get_storagedoortype_map() -> dict[str, str]:
    
    mapkeyvalue = StorageDoorTypeMap()

    return mapkeyvalue.model_dump()


@lru_cache 
def get_tableframetype_map() -> dict[str, str]:
    
    mapkeyvalue = TableFrameTypeMap()

    return mapkeyvalue.model_dump()


@lru_cache 
def get_lightingmethod_map() -> dict[str, str]:
    
    mapkeyvalue = LightingMethodMap()

    return mapkeyvalue.model_dump()


@lru_cache 
def get_spacetype_map() -> dict[str, str]:
    
    mapkeyvalue = SpaceTypeMap()

    return mapkeyvalue.model_dump()


@lru_cache 
def get_activity_map() -> dict[str, str]:
    
    mapkeyvalue = ActivityMap()

    return mapkeyvalue.model_dump()

@lru_cache 
def get_projectprogress_map() -> dict[str, str]:
    
    mapkeyvalue = ProjectProgressMap()

    return mapkeyvalue.model_dump()
