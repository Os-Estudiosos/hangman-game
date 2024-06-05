# Módulos importados
from flask import Flask
from dotenv import load_dotenv

# Módulos próprios
from word_management import *

# Blueprints das rotas
from routes.api import api
from routes.static import static


if __name__ == "__main__":
    load_dotenv()  # Carrego as variáveis ambiente

    # Inicializando a aplicação
    app = Flask(__name__)

    # Adicionando blueprints
    app.register_blueprint(static, url_prefix="/")
    app.register_blueprint(api, url_prefix="/api")

    # Rodando a aplicação
    app.run(debug=True)