import platform
import os

temp = input("Escolha uma palavra\n")

palavra = []
for char in temp:
    palavra.append(char)

pinto = []

for char in palavra:
    pinto.append('_')
    
for cu in pinto:
    print(cu, end = ".")
    
cupinto = len(pinto)
vidas = 6
os.system("cls")
while(pinto != palavra and vidas != 0):    
    letra = input("\ndiga uma letra:")
    if(letra == temp):
        for cu in palavra:
            print(cu, end ="")
        break    
    lost = "yes"
    for index,char in enumerate(palavra):
        if(letra == char):
            pinto[index] = letra
            lost = "no"
    if(lost == "yes"):
        vidas -= 1
    os.system("cls")
    for cu in pinto:
        print(cu, end = ".")
    print("    vidas: ", vidas)
if(vidas == 0):
    print('\nPerdeu')
else:
    print("\nPabens")
   

