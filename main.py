from flask import Flask, render_template, request
import requests

app = Flask(__name__)


# формируем путь и методы GET и POST
@app.route('/', methods=['GET', 'POST'])
def index():
    weather = None
    news = None
    # задаём условия для проверки метода
    if request.method == 'POST':
        # в форме будет одно поле – город; этот город мы будем брать для запроса API
        city = request.form['city']
        weather = get_weather(city)
        news = get_news()
    return render_template("index.html", weather=weather, news=news)


def get_weather(city):
    api_key = "bf599969fa3d07075ac981c3ba80fab8"
    # адрес, по которому мы будем отправлять запрос
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    return response.json()

def get_news():
    api_key = "d8acec0029374c7c99ab3ca28348deb3"
    url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}"
    response = requests.get(url)
    return response.json().get('articles', [])


if __name__ == '__main__':
    app.run(debug=True)
