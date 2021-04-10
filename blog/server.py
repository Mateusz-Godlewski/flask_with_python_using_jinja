from flask import Flask, render_template
import requests


app = Flask(__name__)


@app.route("/")
def home():
    blog_data = requests.get(url="https://api.npoint.io/5abcca6f4e39b4955965").json()
    return render_template("index.html", blog_data=blog_data)


@app.route("/guess/<guess>")
def guessed_name(guess):
    name = guess
    age_api = f"https://api.agify.io?name={name}"
    gender_api = f"https://api.genderize.io?name={name}"
    nation_api = f"https://api.nationalize.io?name={name}"
    try:
        age = requests.get(url=age_api).json()["age"]
        gender = requests.get(url=gender_api).json()["gender"]
        nation = requests.get(url=nation_api).json()["country"][0]["country_id"]
    except IndexError:
        return "Name provided could not be found. "
    return render_template("name.html", name=name, age=age, gender=gender, nation=nation)


@app.route("/blog/<num>")
def blog(num):
    blog_data = requests.get(url="https://api.npoint.io/5abcca6f4e39b4955965").json()
    return render_template("blog.html", blog_data=blog_data, num=int(num))


if __name__ == "__main__":
    app.run(debug=True)