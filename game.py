import unicodedata 

# Retiro os acentos da palavara
def tira_acento(palavra):
    texto_normalizado = unicodedata.normalize('NFD', palavra)
    temp_s = ''.join(c for c in texto_normalizado if unicodedata.category(c) != 'Mn')
    return (temp_s)

# Checo se string/char está dentro da palavra e retorno uma lista com as posições (se for True) ou uma lista vazia (se for False) ou acertou se for a palavra
def check_word(palavra, content):
    
    temp_s = tira_acento(palavra).lower()
    content = tira_acento(content).lower()
  
    #cria uma lista com os caracteres sem acento:
    palavra_sem_acentos = []
    for char in temp_s:
        palavra_sem_acentos.append(char)
    
    # Se for exatamente a palavra, retorno venceu e uma lista vazia
    if(content == temp_s):
        return{"variavel" : "venceu", "index_s" : [] }

    variavel = "false"
    
    index_s = []
        
    index = 0
    
    # Faço uma lista com as posições em que a letra está
    for char in temp_s:
        if(char == content):
            index_s.append(index)
            variavel = "true"
        index += 1
    
    # Retorno uma lista com True (posições que a letra está) e False 
    return {"variavel": variavel,"index_s": index_s}           


