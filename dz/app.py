from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///faculties.db'
db = SQLAlchemy(app)


class Faculty(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    facultyName = db.Column(db.String(100), nullable=False)
    departmentNumber = db.Column(db.Integer, default=0)


with app.app_context():
    db.create_all()


@app.route("/index")
@app.route("/")
def index():
    return render_template('index.html')


@app.route("/faculties")
def faculties():
    faculties = Faculty.query.all()
    return render_template('faculties.html', faculties=faculties)


@app.route("/create", methods=['POST', 'GET'])
def create():
    if request.method == 'POST':
        facultyName = request.form['facultyName']
        departmentNumber = request.form['departmentNumber']

        faculty = Faculty(facultyName=facultyName, departmentNumber=departmentNumber)

        try:
            db.session.add(faculty)
            db.session.commit()
            return redirect('/')

        except:
            return 'При добавлении факультета произошла ошибка'

    else:
        return render_template('create.html')


if __name__ == '__main__':
    app.run(debug=True)

