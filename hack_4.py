"""
generic script

text: "fooziman" output => "oozima" 
text: "barziman" output => "arzima" 
text: "qux" output => "qux" 
"""


def fn_hack_4(s):
    result = s
    tamano = len(result)
    if tamano > 3:
        result = result[1:-1]
    
    return result
