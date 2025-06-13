from flask import Flask, render_template, request, redirect, url_for, flash
import mysql.connector

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# MySQL Database Connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="placement_db"
)
cursor = db.cursor()


# --------------- ROUTES ---------------

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        cursor.execute("SELECT * FROM users WHERE username=%s AND password=%s", (username, password))
        user = cursor.fetchone()

        if user:
            flash(f"Welcome, {username}!", "success")
            return redirect(url_for('admin'))
        else:
            flash("Invalid username or password", "error")
            return redirect(url_for('login'))

    return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        student_id = request.form['studentid']
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        department = request.form['department']
        year = request.form['year']
        company = request.form['Company']
        status = request.form['status']

        cursor.execute("""
            INSERT INTO placement_registration
            (student_id, name, email, phone, department, graduation_year, company, status)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """, (student_id, name, email, phone, department, year, company, status))

        db.commit()
        flash("Registration successful!")
        return redirect(url_for('home'))

    return render_template('reg.html')


@app.route('/admin')
def admin():
    cursor.execute("SELECT name, department, company, status FROM placement_registration")
    records = cursor.fetchall()
    return render_template('admin.html', records=records)


@app.route('/student', methods=['GET', 'POST'])
def student_profile():
    if request.method == 'POST':
        student_id = request.form['studentId']
        name = request.form['studentName']
        course = request.form['course']
        email = request.form['email']

        cursor.execute("""
            INSERT INTO student_profiles (student_id, name, course, email)
            VALUES (%s, %s, %s, %s)
        """, (student_id, name, course, email))
        db.commit()
        flash("Student profile submitted successfully!")
        return redirect(url_for('student_profile'))

    return render_template('stu.html')


@app.route('/student/placement', methods=['POST'])
def student_placement():
    student_id = request.form.get('studentId', 'N/A')
    company = request.form['company']
    position = request.form['position']
    package = request.form['package']
    status = request.form['status']

    cursor.execute("""
        INSERT INTO placements (student_id, company, position, package, status)
        VALUES (%s, %s, %s, %s, %s)
    """, (student_id, company, position, package, status))
    db.commit()
    flash("Placement details submitted successfully!")
    return redirect(url_for('student_profile'))


@app.route('/suthan', methods=['GET', 'POST'])
def suthan():
    if request.method == 'POST':
        company = request.form.get('companyName')
        role = request.form.get('role')
        package = request.form.get('package')
        # Optional: save to DB if needed
        flash("Company details saved (not actually stored in DB yet)")
        return redirect(url_for('suthan'))

    return render_template('suthan.html')



# --------------- MAIN ---------------
if __name__ == '__main__':
    app.run(debug=True)
