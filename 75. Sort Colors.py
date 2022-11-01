nums = [2,0,2,1,1,0]
Output = [0,0,1,1,2,2]
class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # solo usamos dos variantes porque la tercera se usa directamente con el else
        z = 0                   # z o numero 0 le ponemos valor igual a 0
        o = 0                  # o numero 1 le ponemos valor igual a 0
        
        for num in nums:    # para numeros en nums, 
            if num == 0:       # si la vairante numeros es == 0
                z += 1             # le sumamos uno a la variante z(cero)
            elif num == 1:     # si la vairante numero es == 1
                o += 1             # le sumamos uno a la variante o(uno)
                
        for i in range(len(nums)):     # para la variante i en el rango de len de nums
            if i < z:                              # aqui vamos a usar el if, siguiendo lo siguiente
                nums[i] = 0                   # si i es mayor que z, los nums de i son = 0
            elif i < (z + o):                   # pero si la i es mayor que (z + o) 
                nums[i] = 1                    # entonces nums[i] = 1
            else:                                    # recuerden que la variante i suma uno por cada vez que se cunple una condición por eso se suma(z+o)
                nums[i] = 2                     # y si no se cumple ninguna, nums[i] es = 2
#---------------------------------------#
# solucion diferente
    def sortColors(self, nums):
        red, white, blue = 0, 0, len(nums)-1     #rojo es el valor 0, blanco el valor 1 y blue el valor 2
                                                                     # aqui vamos a trabajar con el blanco para un lado y luego para el otro
        while white <= blue:                                                    # cuando blanco es menor que azul implementamos
            if nums[white] == 0:                                                        # si nums[white] == 0 
                nums[red], nums[white] = nums[white], nums[red]     # implementamos esto para hacer un cambio de variantes
                white += 1                                                                     # y le sumamos 1 a white
                red += 1                                                                        # y uno a red
            elif nums[white] == 1:                                                         
                white += 1
            else:
                nums[white], nums[blue] = nums[blue], nums[white]
                blue -= 1