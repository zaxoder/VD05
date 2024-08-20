from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

posts = []

@app.route("/")
def hello_world():

    return render_template("index.html")
@app.route("/price/")
def hello():

    return render_template("price.html")
@app.route("/contacts/")
def hel():
    return render_template("contacts.html")

@app.route("/stat/", methods=["GET", "POST"])
def help():
    if request.method == 'POST':
        title = request.form.get('title')
        con = request.form.get('con')
        cont = request.form.get('cont')
        conten = request.form.get('conten')
        content = request.form.get('content')

        if title and content and con and cont and conten:
            posts.append({'title': title, 'content': content, 'con': con, 'cont': cont, 'conten': conten})
            return redirect(url_for('help'))
    return render_template('stat.html', posts=posts)

if __name__ == '__main__':
    app.run(debug=True)