def evaluar_rpn(expresion):
    pila = []

    for elemento in expresion.split():
        if elemento.isdigit():
            pila.append(int(elemento))
        else:
            operando2 = pila.pop()
            operando1 = pila.pop()
            if elemento == "+":
                pila.append(operando1 + operando2)
            elif elemento == "-":
                pila.append(operando1 - operando2)
            elif elemento == "*":
                pila.append(operando1 * operando2)
            elif elemento == "/":
                pila.append(int(operando1 / operando2))

    return pila[0]

print(evaluar_rpn("2 3 1 * +"))  # imprime 5
print(evaluar_rpn("4 2 5 * + 1 3 2 * + /"))  # imprime 2
