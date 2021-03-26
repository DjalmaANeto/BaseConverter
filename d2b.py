numberI = []
numberD = []


def divisions(d, D, numberI):
    print("Parte inteira: ")
    while D >= 1:
        R = D % d
        numberI.append(int(R))
        old = int(D)
        D = int(D)/d

        print(old, "/", d, "=", D, "→", old, "%", d, "=", int(R))
    numberI = numberI.reverse()


def multiplications(d, dec, numberD):
    print("Parte fracionária:")
    # no caso de uma dizima periodica sera interrompida em 6 casas
    x = 0
    while x <= 5:
        old = dec
        dec = dec * d
        temp = dec
        numberD.append(int(temp))
        if int(dec) == 1:
            dec = dec - 1

        print(old, "*", d, "=", temp, "→", int(temp))
        x = 1 + x


def checkAndTransform(d, D, numberI, numberD):
    if D - int(D) == 0:
        divisions(d, D, numberI)
        print("Resultado: ", end="")
        for x in numberI:
            print(x, end="")

    else:
        dec = D - int(D)
        divisions(d, D, numberI)
        multiplications(d, dec, numberD)
        print("Resultado: ", end="")
        for x in numberI:
            print(x, end="")
        print(".", end="")
        for x in numberD:
            print(x, end="")

# checkAndTransform(d, D, numberI, numberD)


def main():
    # entradas do teclado
    d = input('Entre com a base para conversão (digite apenas números): ')
    D = input('Entre com o número a ser convertido (digite apenas números): ')

    # formatando entradas do teclado
    for x in list(D):
        if x == ".":
            D = float(D)

    if float(D) - int(D) == 0:
        D = int(D)

    for x in list(d):
        if x == ".":
            d = float(d)
                
    if float(d) - int(d) == 0:
        d = int(d)
        

    checkAndTransform(d, D, numberI, numberD)

    op = input('\nDigite 0 para sair...\nOu qualquer outra tecla pra continuar...')

    if op != '0':
        main()


main()
