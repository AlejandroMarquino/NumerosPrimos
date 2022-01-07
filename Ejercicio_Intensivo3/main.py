"""
Enunciado: Crea una función que calcule los números primos entre 1 y N,
           siendo N el parámetro que recibe la función.
"""

# primero solicitamos al usuario en numero N, se especifica que debe ser positivo.
n = int (input("Introduce un número entero. Debe ser positivo.\n"))

if n > 0:
# iniciamos un bucle for iterando dentro de la funcion range().
# Esta la lista la iniciamos dándole 2 parámetros, por el que inicia y el termina, que será N.
    for i in range(2,n):
        divider = 2 #el denominador irá creciendo hasta el número anterior de la variable i

        isPrime = True

        while isPrime and divider < i:

            if i % divider == 0:

                isPrime = False
            else:
                divider += 1 #aquí hago crecer el denominador.

        if isPrime:

            print(i, "es un número primo")

# Por si acaso se introduce un 0 o negativo, validamos el número del usuario y si no es correcto, informamos al usuario.
# haremos unos condicionales con if.
else:
    print("El número no es válido. Introduzca un número entero. Debe ser positivo\n")
