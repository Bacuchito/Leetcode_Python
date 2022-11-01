class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # lo primero que hacemos es crear un diccionario, en este caso le pusimos la variante dict
        dict = {}
        # para idx, la variante e enumarada en (nums), esto lo hacemos para tome en cuenta los numeros dentro de la variante nums
        for idx, e in enumerate(nums):
            # aqui si target(9) - e(que son los numeros de nums), basicamente aqui lo que va a hacer es buscar las variantes que den el target
            if target -e in dict:
                return dict[target -e], idx
        # aqui dict[e] es igual a idx.      
        dict[e] = idx