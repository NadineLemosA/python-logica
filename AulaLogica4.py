for i in range(0,3,1):
    letra=input("Digite uma letra:")
    letraFinal=letra.lower()

if letraFinal== 'a':
    print(f"A letra '{letra}' é uma vogal.")
elif letraFinal== 'e':
    print(f"A letra '{letra}' é uma vogal.")
elif letraFinal== 'i':
    print(f"A letra '{letra}' é uma vogal.")
elif letraFinal== 'o':
    print(f"A letra '{letra}' é uma vogal.")
elif letraFinal== 'u':
    print(f"A letra '{letra}' é uma vogal.")
else:
    print(f"A letra '{letra}' é uma consoante.")

''' inicio - 0  limite enquanto - < 3 passo - 1'''
'''ao nao colocar, o inicio e o passo sao padroes, 0 e 1 respectivamente'''

for i in range(0,3,1):
    print(i)

print("\n\n***********")
i=0
print(i)
i=1
print(i)

for i in range(10,0,-1):
    print(i)