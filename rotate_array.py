class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Crea una copia de la lista nums
        copy = [num for num in nums]
        
        # Calcula el tamaño de la lista original
        n = len(nums)
        
        # Recorre la lista copy
        for i, num in enumerate(copy):
            # Calcula la posición en la que se debe almacenar el elemento num en la lista original
            # y asigna el valor de num a esa posición
            nums[(i + k) % n] = copy[i]

s = Solution()
nums = [1, 2, 3, 4, 5]
k = 2
s.rotate(nums, k)
print(nums) # Output: [4, 5, 1, 2, 3]
