"""
generic script

text: "fooziman" output => "fOozIman" 
text: "qux" output => "qUx" 
text: "eq" output => "eq" 
"""


def fn_hack_1(s):
    result = s
    vocales = ['i','o','u']
    tamano_s = len(s)
    for x in range(tamano_s):
        if result[x] in vocales:
            vocales.remove(result[x])
            result = result.replace(result[x], result[x].upper(), 1)

    return result


#y=fn_hack_1('fooziman')
#print(y)

# si encuentra vocal reemplaza por mayuscula primera vez, siguiente ignora