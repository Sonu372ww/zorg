from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    mysearch = None

    if request.method == 'POST':
        find = request.form.get('search_term')
        mysearch = google_search(find)

    return render_template('index.html', mysearch=mysearch)

def google_search(find):
    url = f"https://www.google.com/search?q={find}"
    req = requests.get(url)
    soup = BeautifulSoup(req.text, "html.parser")
    mysearch = soup.find("div", class_="BNeawe").text
    return mysearch

if __name__ == '__main__':
    app.run(debug=True)
