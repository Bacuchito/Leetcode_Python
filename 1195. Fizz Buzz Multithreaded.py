import threading
# en este ejercicio vamos a llamar threading
'''Es básicamente una bandera y puede ser adquirida o liberada.
Así que una llamada a acquire() esperará hasta que Lock sea liberado. 
Originalmente los bloqueos son creados como liberados. 
Así que todo lo que necesitamos aquí es Lock() para crear un bloqueo y dos métodos: acquire() y release().'''
class FizzBuzz:
    def __init__(self, n: int):                     
        self.n = n
        self.f = threading.Lock()              #llamamos a lock tantas funciones sean necesarias, en este caso 4
        self.b = threading.Lock()             # 3 veces para las variantes FizzBuzz, Fizz y Buzz
        self.fb = threading.Lock()            # y 1 vez para los numeros en este caso variante i
        self.f.acquire ()                             # si vamos a usar Lock, necesitamos tambien usar acquire(), por eso las usamos en las 4 variantes,
        self.b.acquire ()                            # la diferencia es que acquiren en main la usamos al final del algorismo
        self.fb.acquire ()
        self.main = threading.Lock()

    # printFizz() outputs "fizz"
    def fizz(self, printFizz: 'Callable[[ ], None]') -> None:
        while True:
            self.f.acquire()                        #En primer lugar, cuando se inicialice la clase,   
            if self.n == 0:                         # queremos que sólo se libere el hilo principal,
                return                                 # los otros tres hilos deben permanecer bloqueados.
            printFizz()                                # Lo vamos a hacer así:
            self.main.release()

    # printBuzz() outputs "buzz"
    def buzz(self, printBuzz: 'Callable[[ ], None]') -> None:
    	while True:
            self.b.acquire()
            if self.n == 0:
                return
            printBuzz()
            self.main.release()

    # printFizzBuzz() outputs "fizzbuzz"
    def fizzbuzz(self, printFizzBuzz: 'Callable[[ ], None]') -> None:
        while True:
            self.fb.acquire()
            if self.n == 0:
                return
            printFizzBuzz
            self.main.release()
        

    # printNumber(x) outputs "x", where x is an integer.
    def number(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1, self.n+1):
            self.main.acquire()
            if i % 3 == 0 and i % 5 == 0:
                self.fb.release()
            elif i % 3 == 0:
                self.f.release()
            elif i % 5 == 0:
                self.b.release()
            else:
                printNumber(i)
                self.main.release
         
        self.main.acquire()
        self.n = 0
        self.f.release()
        self.b.release()
        self.fb.release()
        return