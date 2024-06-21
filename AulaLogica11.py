alunos=['GABRIEL', 'LUCAS','RODRIGO', 'JÚLIA','SCHEILA','CAMILA' ]
pesos=[80, 90, 78, 45, 60, 100]
alturas=[1.45, 1.88, 1.78, 1.66, 1.70, 1.68]
imcs=[]

def insercao():
    print('#' * 30, ' Insere alunos ', '#' * 30, )
    while True:
        nome = input('Digite o nome do(a) aluno(a):')
        if nome:
            while True:
                try:
                    peso = float(input(f'Digite o peso de {nome}: '))
                    altura = float(input(f'Digite a altura de {nome}: '))
                    break 
                except: 
                    print('CRIATURA digite números reais')
            alunos.append(nome.upper())
            pesos.append(peso)
            alturas.append(altura)
        else:
            break  

def mostrarListas():
    print()
    print('#' * 30, ' Lista Turma ', '#' * 30, )
    for i in range(len(alunos)):
        print(f'Aluno: {alunos[i]}  tem peso = {pesos[i]} e altura = {alturas[i]}')
        #  print('aluno:', alunos[i],' tem nota ', notas[i])
    print('#' * 50)

def buscaAlunoNome():
    print('#' * 30, ' Busca aluno ', '#' * 30)
    mostrarListas()
    while True:
        try:
            nome=input('Digite nome para buscar aluno:')
            indice=alunos.index(nome.upper())
            imcs=round(pesos[indice] / alturas[indice] ** 2, 2)
            break
        except:
            print(f'{nome} não está na turma!')
    print(f' {nome} tem imc {imcs}')
    print('#' * 60 )

def calcularMedia():
    print('#' * 30, ' Calcula Média ', '#' * 30)
    mostrarListas()
    mediaPeso=sum(pesos) / len(pesos)
    mediaAltura=sum(alturas) / len(alturas)
    mediaImcs=sum(imcs) / len(imcs)
    print (f'Media de peso da turma = {round(mediaPeso,2)}')
    print (f'Media de altura da turma = {round(mediaAltura,2)}')
    print (f'Media de imc da turma = {round(mediaImcs,2)}')
    print('#' * 60 )

#inicio do Programa
while True: 
    print('Escolha uma opção do Menu')
    print('1- Cadastra alunos pesos e alturas')
    print('2- Lista todos alunos,   pesos,  altura e imc')
    print('3- Busca um aluno e seu peso e altura e mostra o  IMC')
    print('4- Calcula as média da turma do peso, da altura  e do imc')
    print('5- Encerra programa')
    while True: 
        try:
            opcao=int(input('Opção: '))
            break 
        except:
            print('Digite opção valores inteiros [1-5]')
    if opcao==5:
        break 
    elif opcao==1:
        insercao()
        input('Enter => Continua')
    elif opcao==2:
        mostrarListas()
    elif opcao==3:
        buscaAlunoNome()
        input('Enter => Continua')
    # elif opcao==4:
    #     calcularMedia()

print ('fim')