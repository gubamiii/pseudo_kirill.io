from flask import Flask, render_template, request, jsonify
from flask_cors import CORS

app = Flask(__name__)  
CORS(app)


replacements = {
    'а': 'a', 'б': '6', 'в': 'ß', 'г': 'g', 'д': 'd',
    'е': 'e', 'ё': 'ë', 'ж': 'ж', 'з': '3', 'и': 'u',
    'й': 'ũ', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'H',
    'о': 'o', 'п': 'n', 'р': 'p', 'с': 'c', 'т': 'т',
    'у': 'y', 'ф': 'f', 'х': 'x', 'ц': 'ц', 'ч': '4',
    'ш': 'w', 'щ': 'w', 'ъ': "'", 'ы': 'bI', 'ь': 'b',
    'э': 'e', 'ю': 'ю', 'я': 'я'
}

def convert_text(text):
    """Функция конвертации из оригинального скрипта"""
    return ''.join(replacements.get(char, char) if char.lower() == char 
                  else char for char in text)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    text = request.json.get('text', '')
    converted = convert_text(text)
    return jsonify({'result': converted})


@app.route('/convert_keypress', methods=['POST'])
def convert_keypress():
    key = request.json.get('key', '')
    if key in replacements:
        return jsonify({'result': replacements[key]})
    return jsonify({'result': key})

if __name__ == '__main__':
    app.run(debug=True)