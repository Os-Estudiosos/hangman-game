import json
from openai import OpenAI

# Função para ler o arquivo "config.json"
def read_config():
    with open("config.json", "r", encoding="utf-8") as file:
        file_json = json.load(file)
    return file_json

# Função que pega as letras, o idioma e a dificuldade e retorna uma palavra e uma dica
def get_gpt_word(letters, language, difficulty):
    read_config()  # Leio o arquivo

    # Puxo os dados do Chat GPT, aplicando as variáveis que estão no arquivo .json (letras, idioma, dificuldade)
    client = OpenAI(api_key= "sk-proj-PAZCG7ysv5iKjU3HTDt5T3BlbkFJsEOhwguL2OglilN0CBSd")  # Usando a chave do arquivo de configuração
    prompt = [{"role": "user", "content": f"Dê-me uma palavra de {letters} letras em {language} de nível {difficulty} para jogar o jogo da forca e dê uma dica sem usar a palavra"}]
    response = client.chat.completions.create(messages=prompt, model="gpt-3.5-turbo", max_tokens=50, temperature=0)

    # Pego a resposta do Chat
    response_text = response.choices[0].message.content

    # Separo a palavra e a dica
    try:
        word = response_text.split('Palavra: ')[1].split('\n')[0].strip()
        hint = response_text.split('Dica: ')[1].strip()
    except IndexError:
        word = ""
        hint = response_text.strip()


    # Retorno a palavra e a dica
    return {"word" : word, "hint" : hint}

print(get_gpt_word(10, "português brasileiro", "difícil"))
