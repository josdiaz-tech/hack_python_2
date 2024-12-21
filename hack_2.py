"""
generic script

text: "fooziman" output => "fzmn" 
text: "barziman" output => "brzmn" 
text: "qux" output => "qx" 
"""


def fn_hack_2(s):
    result = s
    vocales = ['a','e','i','o','u']
    _str = []
    for char in result:
        if char not in vocales:
          _str.append(char)  
          
    result = "".join(_str)
    return result


#y=fn_hack_2('fooziman')
#print(y)