from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


# <------ Database stuff ------>
class Agents(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    codename = db.Column(db.String(30), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(40), nullable=False)
    access = db.Column(db.Integer, default=0)

    def __repr__(self):
        return f"<Agent id={self.id}, codename='{self.codename}', phone={self.phone}, email={self.email}, access={self.access}>"


with app.app_context():
    db.create_all()


# <------ Routes ------>
@app.route("/")
def handle_agents():
    agents = Agents.query.all()
    return render_template("home.html", agents=agents)


if __name__ == "__main__":
    app.run(debug=True)

