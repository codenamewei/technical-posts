
from functools import lru_cache
from coreengine.datacleaning import standardizelookup
from coreengine.mapping.data.maptype.catalogmaptype import CatalogMapType


@lru_cache
def exclude_furniture_by_space() -> dict[str, list[str]]:

    LIVING_ROOM = ["침대"] #all
    BALCONY = ["소파", "커피테이블", "수납장", "테이블", "침대"]
    PARTY_ROOM = [] # no record
    RESIDENTIAL_SPACE = ["테이블", "펜던트조명"] # no record
    STUDIO = ["테이블", "침대"]
    PREMIUM_RESIDENTIAL_SPACE = [] #data skewed due to no enough record
    COMMERCIAL_SPACE = ["침대", "테이블"]
    ONE_ROOM = ["커피테이블", "펜던트조명", "소파"]
    OFFICE = ["침대", "펜던트조명"]
    BEDROOM = ["펜던트조명"]
    DINING = ["침대", "소파", "커피테이블", "테이블"] 
    KITCHEN = ["소파", "라운지체어", "커피테이블", "사이드테이블", "데스크", "수납장", "선반장/책장", "침대", "펜던트조명"]
    
    STUDY_ROOM = ["테이블", "침대", "펜던트조명"]
    DRESSING_ROOM = ["라운지체어", "다이닝테이블", "테이블", "데스크", "침대", "펜던트조명"]
    GUEST_ROOM = ["소파", "커피테이블", "테이블", "펜던트조명"]
    ALPHA_ROOM = ["펜던트조명"]
    # here
    ATTIC = ["소파", "체어", "다이닝테이블", "테이블", "데스크", "선반장/책장", "침대", "장스탠드", "펜던트조명"]
    HOBBY = ["소파", "다이닝테이블", "데스크", "수납장", "침대", "펜던트조명"]
    LOUNGE_BAR = ["침대", "펜던트조명"]

    return dict(LIVING_ROOM = LIVING_ROOM, BALCONY = BALCONY, PARTY_ROOM = PARTY_ROOM, RESIDENTIAL_SPACE = RESIDENTIAL_SPACE,
                STUDIO = STUDIO, PREMIUM_RESIDENTIAL_SPACE = PREMIUM_RESIDENTIAL_SPACE, COMMERCIAL_SPACE = COMMERCIAL_SPACE,
                ONE_ROOM = ONE_ROOM, OFFICE = OFFICE, BEDROOM = BEDROOM, DINING = DINING, KITCHEN = KITCHEN, STUDY_ROOM = STUDY_ROOM,
                DRESSING_ROOM = DRESSING_ROOM, GUEST_ROOM = GUEST_ROOM, ALPHA_ROOM = ALPHA_ROOM, ATTIC = ATTIC, HOBBY  = HOBBY, LOUNGE_BAR = LOUNGE_BAR)


def get_furniture_by_space(space_in_eng) -> list[str]:

    excluded_furnitures = exclude_furniture_by_space()[space_in_eng]

    column_mapping = standardizelookup.get_catalog_column_value_mapping(CatalogMapType.CATEGORY)

    excluded_furnitures_in_eng = list(map(lambda x : column_mapping[x], excluded_furnitures))


    return excluded_furnitures_in_eng