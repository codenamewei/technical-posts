from enum import Enum


class PriceRangeMap(Enum):
    
    NULL: str = "NONE"
    HIGHEND : str = "HIGH-END"
    PREMIUM: str = "PREMIUM"
    #mass-produced, relatively inexpensive goods that are marketed as luxurious or prestigious.
    MASSTIGE: str = "MASSTIGE"