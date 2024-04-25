'''3. Faça um programa que receba uma
senha formada de quatro números inteiros,
verifique se a senha está
correta e, caso não esteja, solicite
novamente a senha. Se a senha entrada for
a correta, deverá ser
apresentada a mensagem “Senha Correta”,
caso contrário, “Senha Incorreta”.
'''

# senhaSecreta=1234
# while True:
#     while True:
#         try:
#             print("Querido e Mimoso usuário:")
#             senha=int(input("Digite a senha:"))
#             break
#         except:
#             print("Somente números")
#     if senha < 0 or senha > 9999:
#         print('Máximo de 4 dígitos POSITIVOS')
#     elif senha==senhaSecreta:
#         print("Senha Correta")
#         break
#     else:
#         print("Senha Incorreta")
# print("LOGIN OK")

'''Faça um programa que simule a urna
eletrônica.
A tela a ser apresentada deverá ser da seguinte
forma:
As opcoes sao:
1. Candidato Jair Rodrigues
2. Candidato Carlos Luz
3. Candidato Neves Rocha
4. Nulo
5. Branco
Entre com o seu voto:
O programa deverá ler os votos dos eleitores e,
quando for entrado o número 6, apresentar as seguintes
informações:
a) O número de votos de cada candidato;
b) A porcentagem de votos nulos;
c) A porcentagem de votos brancos;
d) O candidato venc'''

cand1=0
cand2=0
cand3=0
votoNulo=0
emBranco=0

print('-----------------------------')
print('-------URNA ELETRONICA-------')
print('Os candidatos são: ')
print('1. Candidato Jair Rodrigues ')
print('2. Candidato Carlos Luz')
print('3. Candidato Neves Rocha')
print('4. Nulo')
print('5. Branco')
print('-----------------------------')

voto=int(input('DIGITE SEU VOTO: '))

if voto == 1:
    cand1 +=1
elif voto == 2:
    cand2 +=1
elif voto == 3:
    cand3 +=1
elif voto == 4:
    votoNulo +=1
elif voto == 5:
    emBranco +=1
else:
    print('Digite inteiros de 1 a 6')



#     while True:
#     print('\n\n1. Candidato Jair Rodrigues')
#     print('2. Candidato Carlos Luz')
#     print('3. Candidato Neves Rocha')
#     print('4. Nulo')
#     print('5. Branco')
#     while True:
#         try:
#             voto=int(input('DIGITE SEU VOTO:'))
#             break
#         except:
#             print('Somente inteiros de 1 a 6')
#     if voto==6:
#         break
#     elif voto == 1:
#         cand1 +=1
#     elif voto == 2:
#         cand2 +=1
#     elif voto == 3:
#         cand3 +=1
#     elif voto == 4:
#         nulos+=1
#     elif voto ==5:
#         brancos +=1
#     else:
#         print('Digite inteiros de 1 a 6')
#
# total=cand1 + cand2 + cand3 + nulos +brancos
# if total == 0:
#     print("Não houve votação")
# else:
#     print(f'Jair Rodrigues =    {cand1} votos')
#     print(f'Carlos Luz     =    {cand2} votos')
#     print(f'Neves Rocha    =    {cand3} votos')
#     percNulos = (nulos * 100) / total
#     percBrancos = brancos * 100 / total
#     print(f'votos Nulos = {nulos} percentual de {percNulos:.2f} %')
#     print(f'votos Brancos = {brancos} percentual de {percBrancos:.2f} %')
#     if cand1 > cand2 and cand1 > cand3:
#         print("Vencedor foi Jair Rodrigues ")
#     elif cand2 > cand1 and cand2 > cand3:
#         print("Vencedor foi Carlos Luz ")
#     elif cand3 > cand1 and cand3 > cand2:
#         print("Vencedor foi Neves Rocha ")










