"""
generic script

text: ["a","b","c","d","e"] output => ["e-5","d-4","c-3","b-2","a-1"]
text: ["a","b","c"] output => ["c-3","b-2","a-1"]
text: ["a","b","c","d"] output => ["4","3","2","1"]
text: ["a","b"] output => ["2","1"]
"""

def fn_hack_8(s):
    result = s
    tamano = len(s)
    ultimo_indice = tamano - 1
    _str = []

    if tamano % 2 == 0:
        for i in range(tamano):
            _str.append(str(tamano - i))
    else:
        for i in range(tamano):
            _str.append(s[ultimo_indice-i]+"-"+str(tamano - i));

    result = _str

    return result



#y=fn_hack_8(["a","b","c"])
#print(y)