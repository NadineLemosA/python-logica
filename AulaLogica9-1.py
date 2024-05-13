# Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.

numerosArray=[]
for i in range(10):
    num=int(input('Digite um numero: '))
    numerosArray.append(num)
print(numerosArray)
#função que reverte na memoria e modifica a ordenacao por crescente
# numerosArray.sort(reverse=True)

for i in range (-1,-11,-1):
    print(numerosArray[i])