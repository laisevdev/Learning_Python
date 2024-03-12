nome = input("Digite seu nome por favor: "
)

numero = input(f"Por favor, digite um numero inteiro {nome}: ")


if "." or "," in numero: 
    print("Este não é um número inteiro, digite novamente um número sem ponto ou vírgula, por favor: ")
    numero = int(input(f"Por favor, digite um numero inteiro {nome}: "))
    
    if (numero % 2 == 0):
        print("Este número é PAR") 
    else:
        print("Este é um número ÍMPAR")
