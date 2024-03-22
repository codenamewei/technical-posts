from . import nlphelper
import re

_RE_COMBINE_WHITESPACE = re.compile(r"\s+")

def strip_sentence(sentence: str) -> str:
    

    for word in nlphelper.get_design_request_stopwords():
        
        sentence = sentence.replace(word, "")
        
    #remove english words
    output = re.sub('[A-Za-z]', '' , sentence)
    
    sentence = output.rstrip()
    
    
    
    #remove punctuation
    
    for punctuation in [".", ","]:
        
        sentence = sentence.replace(punctuation, " ")
        
    #remove whitespace
    return _RE_COMBINE_WHITESPACE.sub(" ", sentence).strip()


def extract_tools(sentence: str) -> str:
    
    descriptions : list[str] = sentence.split("\n")
    
    tool_description = None
    
    if len(descriptions) > 3:
        
        for description in descriptions:
            
            find_index = list(filter(lambda var: var > -1 and var < 6, [description.find("기존 가구"), description.find("기존가구")]))
            
            if find_index:
                tool_description = description
                break            
    return tool_description

def extract_tools_unit(sentence: str) -> str:
    
    index = sentence.find(":")
    
    if index == -1 or (len(sentence) < (index + 1)):
        
        return None
    
    else:
        
        tools = sentence[index + 1:]
        
        if tools.find("없음") != -1 or tools.find("없습니다") != -1 or tools.find("제외") != -1:
            
            return None
        
        else:
        
            return tools.strip()
    
def strip_tool_line(raw_descriptions : list[str], tool_line: list[str]) -> list[str]:
    
    if len(raw_descriptions) != len(tool_line):
        
        print("length supposed to be the same")
        
    stripped_tool_line_descriptions = list()
        
    for i in range(len(raw_descriptions)):

        stripped_tool_line_descriptions.append(raw_descriptions[i].replace(tool_line[i], "") if raw_descriptions[i] and tool_line[i] else raw_descriptions[i])
            
    return stripped_tool_line_descriptions