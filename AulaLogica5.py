n1=int(input("Digite número inicial:"))
n2=int(input("Digiten número final:"))

if n2<n1:
    aux=n1
    n1=n2
    n2=aux

if n1%2==0:
    n1+=1
    n2+=1
    passo = 2

for i in range(n1,n2,passo):
    print(i)
    
# segundo exercicio
n1=int(input("digite o primeiro numero: "))
n2=int(input("digite o segundo numero: "))
n2+=1

for i in range (n1,n2,1):
    if i%2 ==1:
        print(i)
     
# Terceiro exercicio
contador=0
while (contador<5):
    print(contador)
    contador+=1
else:
    print("Terminou Normal")

print("Fim")

# Quarto exercicio
numeroPedido=int(input("Digite um numero: "))
contador=1
while (contador<=numeroPedido):
    print(contador)
    contador+=1

senha=input("Digite a senha:")
contador=1

while senha!="SenhaCorreta":
    print("Senha invalida!")
    if contador>=3:
        print("Programa encerrado")
        break
    print(f"Tentativa {contador} / 3")
    contador+=1
    senha=input("Digite a senha")
else:
    print("Fim")

# Quinto exercicio
import  datetime
dataAtual=datetime.datetime.now()
anoAtual=dataAtual.year

nome=input("Digite um nome: ")
while nome.lower()!= "fim":
    anoNasc=int(input("Digite o ano de nascimento do " + nome))
    print(f"{nome} tem {anoAtual-anoNasc} anos de idade")
    nome=input("Digite outro nome: ")
else:
    print("Digitou fim")
print("Fim do programa!")

# Sexto exercicio
nome=input("Digite um nome: ")
while nome.lower()!= "fim":
    nota1=int(input("Digite a primeira nota de " + nome))
    nota2=int(input("Digite a segunda nota de " + nome))
    media=(nota1+nota2)/2
    if media>=7:
        print(f"A nota é {media}")
        print(f" {nome} está aprovado")
    else:
        print(f"A nota é {media}")
        print(f"{nome} está reprovado")
        nome=input("Digite outro nome: ")
else:
    print("Digitou fim")
print("Fim do programa!")