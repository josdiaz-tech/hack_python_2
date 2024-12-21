"""
text: [{"a":"b"},{"c","d"},{"e":"f"}] output => [{"1":"2"},{"3","4"},{"5":"6"}]
"""


def fn_hack_10(s):
    result = s
    # Crear el diccionario usando comprensión de diccionario
    alphabet_dict = {chr(i): i - 96 for i in range(97, 123)}
    tamano = len(s)
    _str = []

    for i in range(tamano):
        tipo = type(s[i])
        tamano_sub = len(s[i])
        if  tipo is dict:
           dict_arr = dict()
           for key, value in s[i].items():
               key_equivalente = str(alphabet_dict[key])
               value_equivalente = str(alphabet_dict[value])

               dict_arr[key_equivalente] = value_equivalente
               _str.append(dict_arr)

        elif tipo is set:
            #arr de elementos en el set
            set_arr = set()
            #recorrer el set encontrado en s[i] (result[i])
            for set_elem in s[i]:
               #agrega al set de agrupamiento  set_arr el equivalente del valor del elementor en el alphabet_dict
               set_arr.add(str(alphabet_dict[set_elem]))
            _str.append(set_arr)

    #...
    result = _str
    return result


#y=fn_hack_10([{"a":"b"},{"c","d"},{"e":"f"}])
#print(y)