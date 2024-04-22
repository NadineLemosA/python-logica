#iIDLE - python

a1 = float (input("Digite a aresta 1 do triangulo"))
a2 = float(input("Digite a aresta 2 do triangulo"))
a3 = float (input("Digite a aresta 3 do triangulo"))
p1= a1 + a2 + a3
print("Perimetro do triangulo 1 = ", p1)

b1 = float(input("Digite a aresta 1 do triangulo"))
b2 = float(input("Digite a aresta 2 do triangulo"))
b3 = float(input("Digite a aresta 3 do triangulo"))
p2= b1 + b2 + b3
print("Perimetro do triangulo 2 = ", p2)

if p1 > p2:
    print("Triangulo 1 é o maior")
else:
    print("Triangulo 2 é o maior")


#Cuidar tabulação!!

valor1= int (input("Digite o primeiro valor:"))
valor2= int (input("Digite o segundo valor:"))

if valor1 == valor2:
    print("Os valores são iguais")
elif valor1 > valor2:
    print("O primeiro valor,", valor1," é o maior")
else:
    print("O segundo valor,", valor2," é o maior")


#pega data do sistema
import datetime
dataAtual = datetime.datetime.now().year

nome1=input("Digite o nome da primeira pessoa:")
dataNascimento1= int (input("Digite o ano de nascimento " + nome1))
calculoIdade1 = 2024 - dataNascimento1

nome2=input("Digite o nome da segunda pessoa:")
dataNascimento2= int (input("Digite o ano de nascimento " + nome2))
calculoIdade2 = 2024 - dataNascimento2
 
if calculoIdade1 == calculoIdade2:
    print(nome1, "e", nome2, "tem a mesma idade")
elif calculoIdade1 > calculoIdade2:
    print(nome1, "é mais velha que", nome2)
else:
    print(nome2, "é mais velha que", nome1)