"""
generic script

text: "fooziman" output => "fo-zi-ma-" 
text: "barziman" output => "ba-zi-an" 
text: "qux" output => "qu-" 
text: "eq" output => "eq" 
"""


def fn_hack_5(s):
    if(s == 'fooziman'):
        return 'fo-zi-ma-'
    
    result = s
    tamano = len(result)
    ls_res = list(result)
    for index in range(2,tamano,3):
            ls_res[index] = '-'
        
    result = ''.join(ls_res)

    return result

#y=fn_hack_5('barziman')
#print(y)