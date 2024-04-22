#LOGICA DE PROGRAMAÇÃO - 28/03
#PYCHARM

'''Ler dois numeros e imprimir as variaveis na mesma ordem que foram digitadas'''
numero1=int(input("Digite o primeiro número: "))
numero2=int(input("Digite o segundo número: "))
numero3=int(input("Digite o terceiro número: "))

soma = numero1 + numero2 + numero3
'''modo formatado'''
'''f - representando String e {} para inserir a variável'''
print(f'\nA soma dos valores é: {soma}')

'''Arredondamento de casas após a virgula'''
print("A média é: ", round((numero1 + numero2+ numero3)/3,2))
'''OU'''
print(f'A média é: {(numero1 + numero2+ numero3)/3:.2f}')

'''Inversão de valores: '''
valor1=int(input("Digite o primeiro valor: "))
valor2=int(input("Digite o segundo valor: "))

print("Valores originais: ", valor1, valor2)

valorAux= valor1
valor1= valor2
valor2 = valorAux

print("Valores trocados: ", valor1, valor2)

'''Faça um programa que recebe um nome de candidato a motorista e seu ano de nascimento, informar se  pode tirar a CNH ou não'''
from datetime import date
anoatual=date.today().year

nome=input("Digite o nome do candidato: ")
anoNasc=int(input("Digite o ano de nascimento do candidato: "))

idade=anoatual-anoNasc

if idade <= 17:
    print("O candidato é menor de idade e ainda não pode tirar a CNH.")
else:
    print(idade,'anos \nO candidato está apto a tirar a CNH.')

''' COMO PEGAR ANO ATUAL DO SISTEMA EM PYTHON'''
data_atual = date.today()
print(data_atual)
dia=data_atual.day
mes=data_atual.month
ano=data_atual.year

print('{}/{}/{}'.format(dia, mes, ano))
