from cs50 import get_int

#Pedir altura ao usuário
while True:
    n = get_int ( "Height: ")
    if n > 0 and n < 9:
        break

#Determinar a quantidade de linhas e colunas
for i in range (0, n, 1):
    for j in range (0, n, 1):
        if (i + j < n -1):
            print(" ", end="")

        else:
            print ( "#", end="")

    print()


