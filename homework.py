from flask import Flask, render_template, request
from googletrans import Translator
import requests

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    author, content = None, None
    translated_author, translated_content = None, None
    if request.method == 'POST':
        author, content = get_quote()
        translated_author, translated_content = translate_quote(author, content)
    return render_template("quote.html", author=author, content=content,
                           translated_author=translated_author, translated_content=translated_content)

def get_quote():
    author, content = None, None
    url = "https://api.quotable.io/random"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        author = data.get("author")
        content = data.get("content")
    return author, content


def translate_quote(author, content):
    translator = Translator()
    translated_author = translator.translate(author, src='en', dest='ru').text
    translated_content = translator.translate(content, src='en', dest='ru').text
    return translated_author, translated_content


if __name__ == '__main__':
    app.run(debug=True)
