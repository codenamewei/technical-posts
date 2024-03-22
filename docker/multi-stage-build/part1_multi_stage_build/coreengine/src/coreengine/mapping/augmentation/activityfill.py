from coreengine.datacleaning import standardizelookup
from coreengine.mapping.data.maptype.catalogmaptype import CatalogMapType

#Activity Fill features are based on space

class ActivityFill:

    default_spaces : list[str]

    def __init__(self):

        column_mapping = standardizelookup.get_catalog_column_value_mapping(CatalogMapType.TYPE_OF_SPACE)

        self.default_spaces = list(column_mapping.values())

    def get_default_activites(self, space: str, in_eng : bool = False) -> list[str]:

        standard_space = space.upper()

        match standard_space:

            case "BALCONY" | "발코니":

                return ["휴식", "독서"] if not in_eng else ["REST", "STUDY"]
            
            case "PARTY_ROOM" | "파티룸":

                return ["접객"] if not in_eng else ["GUEST_WELCOME"]
        
            case "RESIDENTIAL_SPACE" | "주거공간": 
        
                return ["휴식"] if not in_eng else ["REST"]
            
            case "STUDIO" | "스튜디오":
        
                return ["작업", "휴식"] if not in_eng else ["WORK", "REST"]
                        
            case "LIVING_ROOM" | "거실":
        
                return ["작업", "휴식", "TV시청"] if not in_eng else ["WORK", "REST", "TV"]
            
            case "PREMIUM_RESIDENTIAL_SPACE" | "고급주거공간":
        
                return ["휴식"] if not in_eng else ["REST"]
            
            case "COMMERCIAL_SPACE" | "상업공간":
        
                return ["작업", "접객"] if not in_eng else ["WORK", "GUEST_WELCOME"]
                        
            case "ONE_ROOM" | "원룸":
        
                return ["작업", "휴식"] if not in_eng else ["WORK", "REST"]
                        
            case "OFFICE" | "사무실":
        
                return ["작업", "접객"] if not in_eng else ["WORK", "GUEST_WELCOME"]
                        
            case "BEDROOM" | "침실":
        
                return ["휴식"] if not in_eng else ["REST"]
                        
            case "DINING" | "다이닝":
        
                return ["접객"] if not in_eng else ["GUEST_WELCOME"]
            
            case "KITCHEN" | "주방":
        
                return ["요리"] if not in_eng else ["COOKING"]
                        
            case "STUDY_ROOM" | "서재":
        
                return ["작업", "독서"] if not in_eng else ["WORK", "STUDY"]
            
            case "DRESSING_ROOM" | "드레스룸":
        
                return ["수납"] if not in_eng else ["STORAGE"]
                        
            case "GUEST_ROOM" | "게스트룸":
        
                return ["접객", "휴식"] if not in_eng else ["GUEST_WELCOME", "REST"]

            case "ALPHA_ROOM" | "알파룸":
        
                return ["작업", "휴식"] if not in_eng else ["WORK", "REST"]
            
            case "ATTIC" | "다락":
        
                return ["휴식"] if not in_eng else ["REST"]
                        
            case "HOBBY" | "취미공간/멀티페이스룸":
        
                return ["음악감상", "와인", "접객"] if not in_eng else ["MUSIC", "WINE", "GUEST_WELCOME"]
            
            case "LOUNGE_BAR" | "라운지바":
        
                return ["음악감상", "와인", "접객"] if not in_eng else ["MUSIC", "WINE", "GUEST_WELCOME"]
            case _:

                raise ValueError(f"Space to fill value is not available: {standard_space}")

    

