from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///faculties.db'
db = SQLAlchemy(app)


class Faculty(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    facultyName = db.Column(db.String(100), nullable=False)
    departments = db.relationship('Department', backref='faculty', lazy=True)

    @property
    def departmentNumber(self):
        return len(self.departments)


class Department(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    departmentName = db.Column(db.String(100), nullable=False)
    tuitionFee = db.Column(db.Integer, default=0)
    faculty_id = db.Column(db.Integer, db.ForeignKey('faculty.id'))


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


@app.route("/faculties/departments/id=<int:faculty_id>")
def departments(faculty_id):
    departments = Department.query.filter_by(faculty_id=faculty_id)
    return render_template('departments.html', departments=departments, faculty_id=faculty_id)


@app.route("/create_faculty", methods=['POST', 'GET'])
def create_faculty():
    if request.method == 'POST':
        facultyName = request.form['facultyName']

        faculty = Faculty(facultyName=facultyName)

        try:
            db.session.add(faculty)
            db.session.commit()
            return redirect('/faculties')

        except:
            return 'При добавлении факультета произошла ошибка'

    else:
        return render_template('create_faculty.html')
    

@app.route("/faculty_id=<int:faculty_id>/create_department", methods=['POST', 'GET'])
def create_department(faculty_id):
    if request.method == 'POST':
        departmentName = request.form['departmentName']
        tuitionFee = request.form['tuitionFee']

        department = Department(departmentName=departmentName, tuitionFee=tuitionFee, faculty_id=faculty_id)

        try:
            db.session.add(department)
            db.session.commit()
            return redirect(f'/faculties/departments/id={faculty_id}')

        except:
            return 'При добавлении кафедры произошла ошибка'

    else:
        return render_template('create_department.html')


if __name__ == '__main__':
    app.run(debug=True)

