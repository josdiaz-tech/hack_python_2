"""
text: {"foo":"fookziman","bar":"barziman"} output => {"Foo":"Fooziman"}
"""


def fn_hack_9(s):
    result = {}
    for key, value in s.items():
        # Verificar si el valor contiene "ziman" después de la transformación
        if "foo" in value:
            # Capitalizar la primera letra de la clave
            new_key = key.capitalize()
            # Tomar el resultado anterior y agregar los faltante de la llave al valor
            new_value = new_key + value[4:]
            # Agregar solo esta clave y valor al resultado
            result[new_key] = new_value
    return result
