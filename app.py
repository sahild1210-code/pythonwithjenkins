from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    profile = {
        "name": "Sahil Sunil Deshmukh",
        "role": "Python & DevOps Enthusiast!",
        "about": "I am a passionate student learning Python, Flask, DevOps tools like Jenkins, Docker, and Git."
    }

    skills = ["Python", "Flask", "HTML", "CSS", "Git", "Docker", "Jenkins"]

    projects = [
        {"title": "Flask Portfolio Website", "desc": "Personal portfolio using Flask"},
        {"title": "CI/CD Pipeline", "desc": "Git + Jenkins + Docker automation"},
        {"title": "Python Automation", "desc": "Automated tasks using Python scripts"}
    ]

    return render_template(
        "index.html",
        profile=profile,
        skills=skills,
        projects=projects
    )

if __name__ == "__main__":
    app.run(debug=True)
