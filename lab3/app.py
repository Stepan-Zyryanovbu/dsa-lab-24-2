from flask import Flask, render_template_string
import json

app = Flask(__name__)

@app.route("/books")
def books():
    books = json.load(open("books.json", encoding="utf-8"))
    return render_template_string(
        "{% for b in books %}{{ b.name }} - {{ b.author }} - {{ b.year }}<br>{% endfor %}",
        books=books
    )

app.run()
