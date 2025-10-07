from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text

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


@app.route("/add", methods=["GET", "POST"])
def handle_add():
    if request.method == "POST":
        agent_data = request.form.to_dict()
        new_agent = Agents(
            codename=agent_data["codename"],
            email=agent_data["email"],
            phone=agent_data["phone"],
            access=agent_data["access"],
        )
        db.session.add(new_agent)
        db.session.commit()
        return redirect("/")
    else:
        return render_template("add.html")


@app.route("/edit/<int:agent_id>", methods=["GET", "POST"])
def handle_edit(agent_id):
    if request.method == 'POST':
        Agents.query.filter_by(id=agent_id).update(request.form.to_dict())
        db.session.commit()
        return redirect('/')
    else:
        agent = Agents.query.get_or_404(agent_id)
        return render_template("edit.html", agent=agent)


@app.route("/agent/<int:agent_id>")
def handle_agent_info(agent_id):
    agent = Agents.query.get_or_404(agent_id)
    return render_template("agent.html", agent=agent)


@app.route("/execute")
def handle_execute():
    con = db.engine.connect()
    con.execute(text('''
        DELETE FROM agents where id = 4 or id = 5
    '''))
    con.commit()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)

