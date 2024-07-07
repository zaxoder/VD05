from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def hello_world():

    return render_template("index.html")
@app.route("/price/")
def hello():

    return render_template("price.html")
@app.route("/contacts/")
def hel():
    return render_template("contacts.html")

@app.route("/stat/")
def help():
    return render_template("stat.html")

if __name__ == '__main__':
    app.run()