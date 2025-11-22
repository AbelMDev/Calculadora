from Operaciones import Operaciones as o

ops = {
    1: o.sumar,
    2: o.restar,
    3: o.multiplicar,
    4: o.dividir
}

a = float(input("Ingresar a: "))
b = float(input("Ingresar b: "))

op = int(input("Ingresar operacion (1.Suma, 2.Restar, 3.Multiplicar, 4.Dividir): "))

op_func = ops.get(op)

if op_func is None:
    print("Operación inválida.")
else:
    resultado = op_func(a, b)
    print("El resultado es:", resultado)