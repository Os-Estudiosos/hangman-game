import json
from game import check_word
from openai import OpenAI
from dotenv import load_dotenv
import os

# Função que pega as letras, o idioma e a dificuldade e retorna uma palavra e uma dica
def get_gpt_word(letters, language, difficulty):

    # Puxo os dados do Chat GPT, aplicando as variáveis que estão no arquivo .json (letras, idioma, dificuldade)
    api_key = os.getenv("OPENAI_API_KEY")
    client = OpenAI(api_key=api_key)  # Usando a chave do arquivo de configuração
    prompt = [{"role": "user", "content": f"Dê-me uma palavra de {letters} letras em {language} de nível {difficulty} para jogar o jogo da forca e dê uma dica sem usar a palavra"}]
    response = client.chat.completions.create(messages=prompt, model="gpt-3.5-turbo", max_tokens=100, temperature=1)

    # Pego a resposta do Chat
    response_text = response.choices[0].message.content

    # Separo a palavra e a dica
    word = response_text.split('Palavra: ')[1].split('\n')[0].strip()
    hint = response_text.split('Dica: ')[1].strip()

    
    # Retorno a palavra e a dica
    return {"word": word, "hint": hint}


