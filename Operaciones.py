class Operaciones:
    
    @staticmethod
    def sumar(a, b): return a + b
    @staticmethod
    def restar(a, b): return a - b
    @staticmethod
    def multiplicar(a, b): return a * b

    @staticmethod
    def dividir(a, b):
        return a / b if b != 0 else float('inf')
