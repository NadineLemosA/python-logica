# Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.

numerosVetor=[]
for i in range(5):
    numero=int(input("Digite um numero: "))
    numerosVetor.append(numero)
print(numerosVetor) 


# Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.

numerosArray=[]
for i in range(10):
    num=int(input('Digite um numero: '))
    numerosArray.append(num)
print(numerosArray)
''''função que reverte na memoria e modifica a ordenacao por crescente
numerosArray.sort(reverse=True)'''
for i in range (-1,-11,-1):
    print(numerosArray[i])


# Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor
# PAR e os números IMPARES no vetor impar. Imprima os três vetores.

generalVector=[]
evenVector=[]
oddVector=[]

for i in range(20):
    number=int(input('Digite um numero: '))
    generalVector.append(number)
    if number%2 == 0:
        evenVector.append(number)
    else:
        oddVector.append(number)

print(generalVector)
print(evenVector)
print(generalVector)

# Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média
# de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.
