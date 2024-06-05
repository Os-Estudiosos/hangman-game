# Módulos importados
from os import getenv
from dotenv import load_dotenv

# Módulos próprios
from game import *
from word_management import *

load_dotenv()  # Carrega as variáveis ambiente

def main():
    interface = Interface()


if __name__ == "__main__":
    main()
