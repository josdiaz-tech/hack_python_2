"""
generic script

["1","-"] => type string
["0"] => type string

text: ["a","b","c","d","e"] output => ["1","-","3","-","5"]
text: [] output => ["0"] 
"""


def fn_hack_6(s):
    result = s
    tamano = len(s)

    if tamano == 0:
        return ["0"]
    
    for index in range(tamano):
        if(index % 2):
            result[index] = '-'
            continue
        result[index] = str(index+1)
    #...
    return result

#y=fn_hack_6(["a","b","c","d","e"])
#print(y)
