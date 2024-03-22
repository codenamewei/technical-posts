
from functools import lru_cache


@lru_cache 
def get_design_request_stopwords() -> list[str]:
    
    index_enumeration = list(range(1, 6))

    numbering = list(map(lambda x: str(x) + ".", index_enumeration))

    raw_description = ["스타일", "색상 및 소재", "기능 및 활용 (필요가구 & 라이프스타일)", "기타 (특이사항 & 디테일 요구사항)"]
    description0 = list(map(lambda s : s + ":", raw_description))
    description1 = list(map(lambda s : s + " :", raw_description))
    index_enumeration = list(range(1, 4))
    index_enumeration.append(5)

    numbering = list(map(lambda x: str(x) + ".", index_enumeration))

    raw_description = ["스타일", "색상 및 소재", "기능 및 활용 (필요가구 & 라이프스타일)", "기타 (특이사항 & 디테일 요구사항)"]
    description0 = list(map(lambda s : s + ":", raw_description))
    description1 = list(map(lambda s : s + " :", raw_description))

    denial_sentiment = ["상관없음", "없음"]

    repetitive_sentiment = ["을 ", "를 ", "이 ", "가 ", "여야 합니다", "하고 싶어요", "합니다", "하고 싶다", "하고싶다", "하고 싶어하심", "하고 싶습니다", "하고싶습니다", "추천해주세요", "선호합니다", "선호하셨습니다", "필요하다", "필요합니다", "필요해요", "입니다", "만들어주세요", "원합니다", "요청했습니다", "요청하셨습니다",  "원했습니다", "원하셨습니다", "희망합니다", "희망했습니다", "부탁드립니다", "부탁 드립니다"]

    punctuation_marks = [":", "\""]

    stop_words = list()

    for i in [numbering, description0, description1, denial_sentiment,repetitive_sentiment,  punctuation_marks]:
        
        stop_words.extend(i)

    return stop_words