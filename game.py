import platform
#import os
import unicodedata

#pede uma palavra

#temp = get_gpt_word(letters, idiome, difficulty)

temp = input("Escolha uma palavra\n")


#Retira os acentos da palavra e cria uma lista temporária
texto_normalizado = unicodedata.normalize('NFD', temp)
temp_s = ''.join(c for c in texto_normalizado if unicodedata.category(c) != 'Mn')

#cria a lista com os caracteres das palavra original
palavra = []
for char in temp:
    palavra.append(char)


#cria uma lista com os caracteres da palavra sem acento
palavra_sem_acento = []
for char in temp_s:
    palavra_sem_acento.append(char)


#cria a lista que será mostrada para o usuário
lista = []
for char in palavra:
    lista.append('_')

#mostra a lista na tela
for letter in lista:
    print(letter, end = ".")
    



vidas = 6
#os.system("cls")
while(lista != palavra and vidas != 0):    
    
    #Lê uma letra ou a palavra do usuário
    letra = input("\ndiga uma letra:")
    if(letra == temp):
        for letter in palavra:
            print(letter, end ="")
        break    
    lost = "yes"
    cac = unicodedata.normalize('NFD', letra)
    letra = ''.join(c for c in cac if unicodedata.category(c) != 'Mn')
    for index,char in enumerate(palavra_sem_acento):
        if(letra == char):
            #caso a letra exista na palavra, ela aparece no usuário 
            lista[index] = palavra[index]
            lost = "no"
    if(lost == "yes"):
        vidas -= 1
#os.system("cls")
    for letter in lista:
        print(letter, end = ".")
    print("    vidas: ", vidas)
if(vidas == 0):
    print('\nPerdeu')
else:
    print("\nPabens")
    
    

   

