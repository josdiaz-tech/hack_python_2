"""
generic script

a = @
e = 3
i = ¡
o = 0
u = v

text: "fooziman" output => "F00z¡m@N" 
text: "barziman" output => "B@rz¡m@N" 
text: "3q" output => "3Q" 
text: "qu" output => "Qv" 
text: "qux" output => "QvX" 
"""


def fn_hack_3(s):
    result = s
    mapa = {
        'a': '@',
        'e': '3',
        'i': '¡',
        'o': '0',
        'u': 'v'
        }
    for char in result:
        if char in mapa.keys():
            result = result.replace(char, mapa[char])

    result = result.capitalize()

    if result[-1] not in mapa.values():
        result = result[:-1] + result[-1].upper()

    return result

#y=fn_hack_3('fooziman')
#print(y)