class Solution:
    def isValid(self, s: str) -> bool:
        # creamos mapa de los pares de parentesis al intversa
        map = { ')' : '(', '}' : '{' , ']' : '[' }
        # luego creamos un stack data structure 
        st = []
        # recorrer cada carecter en la cadena de entrada
        for i in s:
            if len(st) == 0 or not i in map.keys():
                st.append(i)
            elif map.get(i) == st[-1]:
                st.pop()
            else:
                st.append(i)

    def is_Valid(self, s: str) -> bool:
        # crear un par de parentesis abiertos y cerrados
        opcl = dict(('()', '[]', '{}'))
        # Crear stack data structure...
        stack = []
        # Recorrer cada carácter en la cadena de entrada...
        for idx in s:
            # si hay parentesis abiertos, append en el stack 
            if idx in '([{':
                stack.append(idx)
            # Si el carácter está cerrando paréntesis, verifique que el mismo tipo de paréntesis de apertura se esté empujando a la pila o no...
            # si no, nosotros retornamos False
            elif len(stack) == 0 or idx != opcl[stack.pop()]:
                return False
        # Por último, comprobamos si la pila está vacía o no...
        # Si la pila está vacía, significa que todos los paréntesis abiertos se están cerrando 
        # y podemos devolver verdadero; de lo contrario, devolveremos falso...
        return len(stack) == 0
