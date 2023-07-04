import requests
from flask import Blueprint,render_template,flash

views = Blueprint('views',__name__)


@views.route('/', methods=['GET'])
def home():
    url = "https://api-football-v1.p.rapidapi.com/v3/timezone"

    headers = {
        "X-RapidAPI-Key": "628972a6b7msh5cdc009981c173dp14a9dejsnb3b78b24c839",
        "X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)

    print(response.json())

    return render_template("soccer_news.html")