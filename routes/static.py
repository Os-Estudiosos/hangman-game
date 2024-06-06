from os import getenv
from dotenv import load_dotenv
from flask import Blueprint, render_template

static = Blueprint('static', __name__)

@static.route('/')
def index():
    return render_template("index.html")

@static.route('/configs')
def configs():
    return render_template("configs.html")

@static.route('/game')
def game():
    load_dotenv()
    return render_template("game.html", api_url=getenv('API_URL'))
