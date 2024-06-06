import json
from game import check_word
from openai import OpenAI
from dotenv import load_dotenv
import os

# Função que pega as letras, o idioma e a dificuldade e retorna uma palavra e uma dica
def get_gpt_word(theme, language, difficulty, api_key):

    # Puxo os dados do Chat GPT, aplicando as variáveis que estão no arquivo .json (letras, idioma, dificuldade)
    client = OpenAI(api_key=api_key)  # Usando a chave do arquivo de configuração
    prompt = [{"role": "user", "content": f"Escolha uma palavra aleatória do dicionário, sem hifen e espaco, com o tema {theme}, no idioma {language}, de nível {difficulty}, dê um a dica sem usar a palavra, mande a dica na lingua {language}, e mande como uma string JSON"}]
    response = client.chat.completions.create(messages=prompt, model="gpt-3.5-turbo", max_tokens=100, temperature=1)

    # Pego a resposta do Chat
    response_text = response.choices[0].message.content

    print(response_text)

    # Separo a palavra e a dica
    word = json.loads(response_text)["palavra"]
    hint = json.loads(response_text)["dica"]

    
    # Retorno a palavra e a dica
    return {"word": word, "hint": hint}


