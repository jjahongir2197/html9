from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def longest_word():

    if request.method == "POST":

        text = request.form["text"]
        words = text.split()

        longest = max(words, key=len)

        return f"Eng uzun so‘z: {longest}"

    return render_template("index.html")

app.run(debug=True)
