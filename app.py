from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    name = "Sahil"
    skills = ["Python", "Flask", "HTML", "CSS"]
    return render_template("index.html", name=name, skills=skills)

if __name__ == "__main__":
    app.run(debug=True)
