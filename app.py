from flask import Flask, render_template, request, redirect
import requests

app = Flask(__name__)

API_KEY = "fcb03aa8c90c4368bcb9e3dfc1a000a8"

# COVER PAGE
@app.route('/')
def cover():
    return render_template("cover.html")

# HALAMAN SEARCH
@app.route('/home', methods=['GET', 'POST'])
def home():
    games = []

    if request.method == 'POST':
        game = request.form['game']

        url = f"https://api.rawg.io/api/games?key={API_KEY}&search={game}"
        response = requests.get(url)
        data = response.json()

        for g in data['results'][:8]:
            games.append({
                "name": g['name'],
                "rating": g['rating'],
                "released": g['released'],
                "image": g['background_image']
            })

    return render_template("index.html", games=games)

if __name__ == '__main__':
    app.run(debug=True)