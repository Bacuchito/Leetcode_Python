strs = ["flower","flow","flight"]
Output ="fl"
class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        prefix = strs[0]                                        # prefix de strs[0] es la palabra que agarramos, en este caso es flower
        for word in strs:                                      # word de strs, aqui nos referimos a la palabra
            while word.find(prefix) != 0:               # aqui usamos un loop, cuando la palabra es diferente a 0
                prefix = prefix[:-1]                          # vamos a restar la ultima letra del prefijo hasta encontrar las que coincidan en este caso fl
                if prefix == '':                                  # aqui ponemos si el prefijo es igual a nada, entonces que nos retorne unas ''
                    return ''
    
        return prefix                                            # aqui retornamos el prefijo para ver el resultado