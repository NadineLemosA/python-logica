#criar lista vazia
lista=[]
#criar lista com conteúdo
lista1=[7,10,5,12,5]

#lista um elemento usando uma constante como índice
print(f"lista constante {lista1[1]}")

#alterar valor de um elemento da lista
lista1[2]=lista1[2]*5
print(lista1[2])

#print da lista
print(lista1)

#print da lista usando for e i como índice
for i in range (5):
    print(lista1[i])
lista1[3]="UNISENAC"
print(lista1)

#--------------------------------------------------------------
#                   0          1            2
lista_compras = ['banana','laranja','maçã']
#                 -3           -2         -1

print(lista_compras[2])
print(lista_compras[-1])
for i in range(3):
    print(f'{i} {lista_compras[i]}')

print()
for i in range (-1,-4,-1):
    print(f'{i} {lista_compras[i]}')

lista_compras.append('Arroz')
lista_compras.append('Feijão')
lista_compras.append('Alface e tomate')

# len(lista_compras) calcula o tamanho da Lista
for i in range(len(lista_compras)):
     print(f'{i} {lista_compras[i]}')