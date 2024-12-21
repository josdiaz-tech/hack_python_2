"""
generic script

["1",2] => type string & type int
[0] => type int

text: ["a","b","c","d","e"] output => ["1",2,"3",4,"5"]
text: [0] output => [0] 
"""


def fn_hack_7(s):
    result = s
    tamano = len(s)

    if s == [0]:
        return [0]
    
    for index in range(tamano):
        if(index % 2):
            result[index] = int(index+1)
            continue
        result[index] = str(index+1)
    #...
    return result

#y=fn_hack_7(["a","b","c","d","e"])
#print(y)