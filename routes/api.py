from flask import Blueprint, request
from word_management import get_gpt_word
from game import check_word as ckw

api = Blueprint('api', __name__)

@api.route('/check-word', methods=["POST"])
def check_word():
    word = request.json['word']
    content = request.json['content']
    return ckw(word, content)


@api.route('/catch_word', methods=['GET'])
def catch_word():
    input_theme = request.args.get('theme')
    select_language = request.args.get('language')
    input_difficulty = request.args.get('difficulty')

    return get_gpt_word(input_theme, select_language, input_difficulty)

