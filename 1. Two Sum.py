class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # Crea un diccionario vacío
        dict = {}
        
        # Recorre la lista nums
        for idx, e in enumerate(nums):
            # Si target - e está en el diccionario, devuelve el índice de target - e y el índice de e
            if target - e in dict:
                return dict[target - e], idx
            
            # Agrega el elemento e y su índice al diccionario
            dict[e] = idx

s = Solution()

nums = [2, 7, 11, 15]
target = 9
result = s.twoSum(nums, target)
print(result) # Output: [0, 1]


nums = [3, 2, 4]
target = 6
result = s.twoSum(nums, target)
print(result) # Output: [1, 2]