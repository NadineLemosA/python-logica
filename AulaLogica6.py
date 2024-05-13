# # exemplo com variavel boolean
#condição simples
nome=input("Digite um nome: ")
while nome:
    print(nome)
    nome=input("Digite um nome: ")

print("***************")

numero=int(input("Digite o numero que quer multiplicar: "))
while numero>0:
    contador=1
    while contador<=10:
        resultado=numero*contador
        print(resultado)
        contador+=1
    numero=int(input("Digite outro numero: "))
print("Fim do programa!")

nome=(input("Digite o nome "))
while nome:
    while True:
        try:
            anoNasc=int(input(f'Digite o ano de nascimento de {nome}'))
            break
        except:
            print('Criatura ano de nascimento!')
    idade=2024-anoNasc
    print(f'{nome} tem {idade} anos de idade.')
    nome=(input("Digite o nome "))

# Crie um programa que inicie em 10 e conte regressivamente até 1 usando um
# loop while. Após a contagem, exiba uma mensagem, por exemplo, "Foguete lançado!".

for i in range (10,-1,-1):
     print(i)
print('Foguete lançado')

# Adivinhe o Número com Loop While e if: Implemente um jogo em que o programa gera um número aleatório entre 1 e 100,
# e o usuário tenta adivinhá-lo. O programa deve fornecer dicas ("maior" ou "menor") até que o usuário adivinhe o número correto,
# usando um loop while e comandos if.

import random
x = random.random()
n = int(x*100)
print(n)

numero = int(input('Adivinhe o numero: '))
while numero:
    if n > numero:
        print('O numero é maior que o digitado!')
    elif n < numero:
        print('O numero é menor que o digitado!')
    else:
        print('ACERTOU!')
        break
    numero = int(input('Adivinhe o numero: '))
print("*******SAIU********")

# 1. Faça um programa que implemente um menu onde o usurário deverá selecionar 1 ou 0. Caso seja entrado
# um número diferente, o programa deverá solicitar uma nova opção.

numero = int(input('Escolha a opção 0 ou 1: '))

while numero:
    if numero > 1:
        print('Selecione uma opção valida!')
        numero = int(input('Escolha a opção 0 ou 1: '))
    else:
        print(f'Opção {numero} selecionada corretamente')
        break

# 2. Faça um programa que leia número reais maiores que zero. Quando for entrado o número zero, o
# programa deverá apresentar quantos números foram entrados e a média destes.

numero = int(input('Digite um numero: '))
contador = 0
soma = 0

while numero:
    if numero > 0:
        contador+=1
        soma+=numero
        numero = int(input('Digite um numero: '))
    elif numero == 0:
        break
    else:
        print("Numero negativo n")
# precisa sair do loop para fazer o calculo
print(f'Foram digitados {contador} numeros.')
print(f'A media dos numeros é {soma/contador}.')












