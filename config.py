# Mudar o campo difficulty para inteiros de 1 a 5 (inclusos)

import json

def change_config(difficulty, letters, language, music):

    if not isinstance(difficulty, str):
        raise TypeError("A dificuldade deve ser uma string")
    
    if not isinstance(letters, int) or letters <= 0:
        raise ValueError("O número de letras deve ser um inteiro positivo")

    if not isinstance(language, str):
        raise TypeError("O idioma deve ser uma string")

    if not isinstance(music, str):
        raise TypeError("A música deve ser uma string")

    config_dict = {
        "difficulty": difficulty,
        "letters": letters,
        "language": language,
        "music": music
    }

    with open("config.json", "w", encoding="utf-8") as config_file:
        json.dump(config_dict, config_file, indent=4, ensure_ascii=False)

    return config_dict

difficulty = "difícil"
letters = 10
language = "brasileiro"
music = "false"

try:
    result = change_config(difficulty, letters, language, music)
    print(result)
except (TypeError, ValueError) as e:
    print("Erro:", e)