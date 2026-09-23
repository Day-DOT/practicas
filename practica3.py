cantidad = int(input("¿Cuántas proposiciones quieres? "))

# Crear nombres P, Q, R, S...
proposiciones = []
for i in range(cantidad):
    proposiciones.append(chr(80 + i))

# Encabezado
for p in proposiciones:
    print(p, end="\t")
print()

print("-" * (cantidad * 8))

total = 2 ** cantidad

for numero in range(total):
    for posicion in range(cantidad):
        valor = (numero // (2 ** (cantidad - posicion - 1))) % 2

        if valor == 1:
            print("True", end="\t")
        else:
            print("False", end="\t")

    print()