class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        # almacena la longitud del array temperatures en la variable n.
        n = len(temperatures)
        # crea un nuevo array para almacenar el número de días que tienes que esperar para una temperatura más cálida para cada día.
        ans = [0] * n
        # Esta pila se usará para almacenar los índices de las temperaturas en el array
        stack = []
        # comienza un bucle que itera sobre los índices del array 'temperatures'.
        for i in range(n):
            # comienza un bucle que continúa mientras 'stack' no esté vacía y la temperatura actual sea mayor que la temperatura en la parte superior de la pila.
            while stack and temperatures[i] > temperatures[stack[-1]]:
                # elimina el elemento superior de la pila y lo almacena en la variable 'j'.
                j = stack.pop()
                #  calcula el número de días que tienes que esperar para una temperatura más cálida
                ans[j] = i - j
            # añade el índice actual a la parte superior de la pila.
            stack.append(i)
        # devuelve el array 
        return ans

