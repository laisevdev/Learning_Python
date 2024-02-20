#Exercício

nome_usu = input('Digite seu nome: ')
idade_usu = input('Digite sua idade aqui: ')
usuario = (f'Nome: {nome_usu} e idade: {idade_usu}')


if nome_usu and idade_usu: 
    print(f'O nome do usuario é {nome_usu} e sua idade é de {idade_usu} anos.')
    print(f'O seu nome invertido é {nome_usu[::-1]}')
    print(f'Seu nome tem {len(nome_usu)} letras ')
    print(f'A primeira letra do seu nome é: {nome_usu[0]}')
    print(f'A última letra do seu nome é {nome_usu[-1]}')

    if ' ' in nome_usu:
        print('Seu nome contém espaços')
    else: 
        print('Seu nome NÃO tem espaços')
else: 
    print('Desculpe, vc deixou campos vazios')
