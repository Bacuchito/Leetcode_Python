class Solution:
    def reverse(self, x: int) -> int:
        # Almacena una copia del valor de x
        i = x
        
        # Crea una variable para almacenar el número invertido
        newNum = 0
        
        # Mientras x sea mayor que 0
        while x > 0:
            # Agrega el último dígito de x al nuevo número y lo multiplica por 10 para moverlo a la izquierda
            newNum = newNum * 10 + x%10
            # Divide x entre 10 para eliminar el último dígito
            x = x//10
        
        # Devuelve el número invertido
        return newNum


s = Solution()

x = 123
result = s.reverse(x)
print(result) # Output: 321

x = 321
result = s.reverse(x)
print(result) # Output: -123