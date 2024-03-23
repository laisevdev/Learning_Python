
DESNUTRICAO_GRAVE = 'DESNUTRIDO(A) GRAVE'
DESNUTRIDO = 'DESNUTRIDO(A)'
BAIXO_PESO = 'BAIXO PESO'
EUTROFICO = 'EUTRÓFICO/SAUDÁVEL'
SOBREPESO = 'SOBREPESO'
OBESIDADE = 'OBESIDADE'
OBESIDADE_MORBIDA = 'OBESO(A) MÓRBIDA'


def calcula_imc ():

    while True:
        boas_vindas = "Olá seja muito bem vindo(a) ao nosso app de IMC."
        nome = input(f'{boas_vindas} Por favor, nos diga qua é o seu nome: ' )

        while True:
            try:
                peso = float(input(f'Seja bem vindo(a) {nome}. Para saber o seu Índice de Massa Corporal e classificação Nutricional precisamos de algumas informações. Digite por favor seu peso em kg aqui: '))
                altura = float(input(f'Por favor, agora digite sua altura: '))

                if peso == 0 or altura == 0:
                        print('Você digitou zero, digite por favor novamente abaixo um número válido.')
                else:
                    break
            except ValueError:
                print("Por favor, digite um valor numérico válido.")

        
        imc = peso / (altura * altura)
        if imc < 15.50:
            print(f"Seu IMC é {imc:.2f} kg/m², classificado como {DESNUTRICAO_GRAVE}. Recomendamos procurar um nutricionista para orientações.")
        if imc >= 15.50 and imc < 17:
            print(f"Seu IMC é {imc:.2f} kg/m², classificado como {DESNUTRIDO}. Recomendamos procurar um nutricionista para orientação.")
        if imc > 17 and imc <= 18.50:
            print(f"Seu IMC é {imc:.2f} kg/m², classificado como {BAIXO_PESO}. Recomendamos procurar um nutricionista para orientações.")
        if imc > 18.50 and imc <= 24.99:
            print(f"Seu IMC é {imc:.2f} kg/m², classificado como {EUTROFICO}. Seu peso é adequado para sua altura.")
        if imc >= 25 and imc <= 29.99:
            print(f"Seu IMC é {imc:.2f} kg/m², classificado como {SOBREPESO}. Recomendamos procurar um nutricionista para orientação e perda de peso.")
        if imc > 30 and imc <= 35:
            print(f"Seu IMC é {imc:.2f} kg/m², classificado como {OBESIDADE}. Recomendamos procurar um nutricionista para orientação e perda de peso.")
        elif imc > 35:
             print(f"Seu IMC é {imc:.2f} kg/m², classificado como {OBESIDADE_MORBIDA}. Recomendamos procurar um nutricionista para orientação médica especializada.")
        else:
            print(f"")
        
        continuar = input("Deseja calcular o IMC novamente? (Digite 'c' para continuar ou 's' para sair: ")
        if continuar.lower() == 's':
            print('Obrigado e volte sempre ao nosso app.')
            break              

(calcula_imc())