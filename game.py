import unicodedata 

def tira_acento(palavra):
    texto_normalizado = unicodedata.normalize('NFD', palavra)
    temp_s = ''.join(c for c in texto_normalizado if unicodedata.category(c) != 'Mn')
    return (temp_s)

def check_word(palavra, content):
    
    temp_s = tira_acento(palavra).lower()
    content = tira_acento(content).lower()
  
    #cria uma lista com os caracteres sem acento:
    palavra_sem_acentos = []
    for char in temp_s:
        palavra_sem_acentos.append(char)
    
    if(content == temp_s):
        return{"variavel" : "venceu", "index_s" : [] }
    variavel = "false"
    
    index_s = []
        
    index = 0
    
    for char in temp_s:
        if(char == content):
            index_s.append(index)
            variavel = "true"
        index += 1
    return {"variavel" : variavel, "index_s" : index_s}           


