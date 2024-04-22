numero=int(input("Digite o numero que quer multiplicar: "))
while numero>0:
    contador=1
    while contador<=10:
        resultado=numero*contador
        print(resultado)
        contador+=1  
    numero=int(input("Digite outro numero: "))
else:
    print("Fim do programa!")