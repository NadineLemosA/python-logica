# Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.
numerosArray=[]
for i in range(5):
    num=int(input('Digite um numero: '))
    numerosArray.append(num)
'''identação faz o papel de fechar chaves'''
print(numerosArray)

# Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.
numerosArray=[]
for i in range(10):
    num=int(input('Digite um numero: '))
    numerosArray.append(num)
print(numerosArray)
#função que reverte na memoria
# numerosArray.sort(reverse=True)
for i in range (-1,-11,-1):
    print(numerosArray[i])

# Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.
# Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.
# Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.
# Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor. Imprima a idade e a altura na ordem inversa a ordem lida.
# Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos quadrados dos elementos do vetor.
# Faça um Programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20 elementos, cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores.
# Altere o programa anterior, intercalando 3 vetores de 10 elementos cada.
# Foram anotadas as idades e alturas de 30 alunos. Faça um Programa que determine quantos alunos com mais de 13 anos possuem altura inferior à média de altura desses alunos.
# Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista. Após isto, calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual, e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).

# # Faça um Programa que leia 4 notas, mostre as notas e a média na tela.
# notas=[]
# for i in range(4):
#     nota=int(input("Digite uma nota: "))
#     '''Append adiciona item no final de uma lista'''
#     notas.append(nota)
# print(notas)
# soma=sum(notas)
# print(soma)
# '''len tamanho do array'''
# print(f'A média é: {soma/len(notas)}')


# # Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.
# '''Cria array de vogais, cria array para alimentar com respostas. input append. print. '''

# vogais=['a','e','i','o','u']
# caracteres=[]
# #leitura 10 caracteres e colocados numa lista
# for i in range (10):
#     caracter=input('Digite uma letra (caracter):')
#     caracteres.append(caracter)
# print(caracteres)
# qtd=0
# for i in range (10):
#     try:
#         indice = vogais.index(caracteres[i])
#     except:
#         qtd+=1
#         print(caracteres[i])
# print(f'qtd de consoantes ={qtd} ')

# for i in range(10):
#     caracter=input('Digite uma letra: ')
#     caracter
#     for j in range(5):
#         if caracteres[i]==vogais[j]:
#             vogal=1
#     if vogal==0:
#         qtd+=1
#         print(caracteres[i])
#     print()


# vogais=['a','e','i','o','u']
# caracteres=[]

# #leitura 10 caracteres e colocados numa lista
# for i in range (10):
#     caracter=input('Digite uma letra (caracter):')
#     caracteres.append(caracter)
# print(caracteres)
# qtd=0
# for i in range(10):
#     vogal=0
#     for j in range(5):
#         if caracteres[i]==vogais[j]:
#             vogal=1
#     if vogal ==0:
#         qtd+=1
#         print(caracteres[i])
# print(f'qtd de consoantes ={qtd} ')
