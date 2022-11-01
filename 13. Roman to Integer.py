s = "III"
Output: 3
class Solution:
    def romanToInt(self, s: str) -> int:
        # lo primero es darle valor a cada letra, lo hacemos haciendo un dictionary 
        rti = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        # una vez que tengamos el diccionario usaremos replace para remplazar las variantes para que coincidan de manera correcta
        s = s.replace('IV', 'IIII').replace('IX', 'VIIII').replace('XL', 'XXXX').replace('XC', 'LXXXX').replace('CD', 'CCCC').replace('CM', 'DCCCC')
        # luego retornamos la rti, tal cual aquí
        return sum(map(lambda x: rti[x], s))