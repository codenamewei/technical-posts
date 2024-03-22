
from coreengine.mapping.ops import maphelper
from coreengine.mapping.ops.mapsequence import MapSequence
from coreengine.mapping.data.maptype.catalogmaptype import CatalogMapType

def mapvalue(input : list[str], maptype : CatalogMapType, maporder : MapSequence = MapSequence.KOR2ENG) -> list[str]:

    lut = maphelper.get_tag_map(maptype, maporder)

    return list(map(lambda x : lut[x], input))


# def keyvaluepair(keys : list[str], maptype : CatalogMapType, maporder : MapSequence = MapSequence.KOR2ENG) -> dict[str, str]:

#     lut = maphelper.get_tag_map(maptype, maporder)
#     values = list(map(lambda x : lut[x], keys))

#     return dict(zip(keys, values))