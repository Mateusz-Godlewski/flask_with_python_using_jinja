from flask import Flask, render_template
from datetime import datetime


app = Flask(__name__)



@app.route("/")
def home():
    current_year = str(datetime.today()).split("-")[0]
    my_name = "Godlewski Mateusz"
    return render_template("index.html", year=current_year, c_name=my_name)


if __name__ == "__main__":
    app.run(debug=True)