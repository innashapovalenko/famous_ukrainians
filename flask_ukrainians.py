from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import os


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///ukrainian_poets.db"
db = SQLAlchemy(app)

#Database model
class Human(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    poem = db.Column(db.Text, nullable=True) 
    biography = db.Column(db.Text, nullable=True)




db_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), "ukrainian_poets.db")
if os.path.exists(db_path):
    os.remove(db_path)
    print("Old database deleted.")

# Create new database
with app.app_context():
    db.create_all()
    print("New database created.")


@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        name = request.form.get("name").strip()
        human = Human.query.filter_by(name=name).first()
        if human:
            result = human
        else:
            result = "No data found. Try another name."

    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)