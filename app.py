from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

# Create table once
def init_db():
    with sqlite3.connect('student.db') as conn:
        conn.execute('''CREATE TABLE IF NOT EXISTS students
                        (name TEXT, physics INTEGER, chemistry INTEGER, math INTEGER,
                         percentage REAL, grade TEXT)''')

@app.route('/')
def student():
    return render_template('student.html')

@app.route('/result', methods=['POST'])
def result():
    if request.method == 'POST':
        name = request.form['Name']
        physics = int(request.form['Physics'])
        chemistry = int(request.form['chemistry'])
        math = int(request.form['Mathematics'])

        total = physics + chemistry + math
        percentage = round(total / 3, 2)

        # Simple grading logic
        if percentage >= 90:
            grade = 'A+'
        elif percentage >= 75:
            grade = 'A'
        elif percentage >= 60:
            grade = 'B'
        elif percentage >= 45:
            grade = 'C'
        else:
            grade = 'F'

        # Save to database
        with sqlite3.connect('student.db') as conn:
            conn.execute("INSERT INTO students (name, physics, chemistry, math, percentage, grade) VALUES (?, ?, ?, ?, ?, ?)",
                         (name, physics, chemistry, math, percentage, grade))

        result_data = {
            "Name": name,
            "Physics": physics,
            "Chemistry": chemistry,
            "Mathematics": math,
            "Percentage": f"{percentage}%",
            "Grade": grade
        }

        return render_template("result.html", result=result_data)

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
