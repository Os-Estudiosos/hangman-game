from flask import Blueprint, request
from word_management import get_gpt_word
from game import check_word as ckw

api = Blueprint('api', __name__)

@api.route('/check-word', methods=["POST"])
def check_word():
    word = request.json['word']
    content = request.json['content']
    print(word, content)
    return ckw(word, content)


@api.route('/catch_word', methods=['GET'])
def catch_word():
    input_letters = request.args.get('letters')
    select_language = request.args.get('language')
    input_difficulty = request.args.get('difficulty')

    #print(f"Letters: {input_letters}, Language: {select_language}, Difficulty: {input_difficulty}")

    return get_gpt_word(input_letters, select_language, input_difficulty)

