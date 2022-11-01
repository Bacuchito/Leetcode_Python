nums = [1,1,2]
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        # Usamos una variable (x = 1) que se incrementa al 
        # siguiente índice cada vez que encontramos un elemento único e 
        # insertamos este elemento en su índice correspondiente.
        x = 1
        # creamos un rango con el len de nums -1.
        for i in range(len(nums)-1):
            # aquí ponemos nums[i] que seria el rango completo, y si es diferente de nums[i + 1]
	        if(nums[i] != nums[i + 1]):
                # va a cumplir que que nums de x es igual a nums de i + 1
		        nums[x] = nums[ i + 1]
                # luego el valor de x le sumamos 1
                x += 1
            # luego retornamos x
            return(x)
        