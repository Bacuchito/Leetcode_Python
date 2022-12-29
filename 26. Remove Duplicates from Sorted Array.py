class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        # Inicializar la variable x con el valor 1
        x = 1

        # Recorrer la lista nums desde el elemento 1 hasta el penúltimo elemento
        for i in range(len(nums)-1):
            # Si el elemento actual es distinto del elemento siguiente
            if(nums[i] != nums[i + 1]):
                # Asignar el elemento siguiente a la posición x de la lista resultante
                nums[x] = nums[i + 1]
                # Aumentar x en 1
                x += 1

        # Devolver la longitud de la lista resultante
        return(x)

# Ejemplo 1
nums1 = [1, 1, 2]
s1 = Solution()
print(s1.removeDuplicates(nums1)) # Output: 2

# Ejemplo 2
nums2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
s2 = Solution()
print(s2.removeDuplicates(nums2)) # Output: 5





