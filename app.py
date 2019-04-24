from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/test', methods=['POST'])
def cut_string():
    requested = str(request.get_json()['string_to_cut'])
    letters = ''.join(character for character in requested if character.isalpha())
    cut = letters[2::3]
    return jsonify({"return_string": cut})


if __name__ == '__main__':
    app.run()
