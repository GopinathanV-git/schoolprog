from flask import Flask, render_template

app = Flask(__name__)

# Home Page
@app.route('/')
def home():
    return render_template('index.html', title='Home')

# About Page
@app.route('/about')
def about():
    return render_template('about.html', title='About Our School')

# Courses Page
@app.route('/courses')
def courses():
    courses_list = ['Mathematics', 'Science', 'English', 'History', 'Computer Science']
    return render_template('courses.html', title='Courses', courses=courses_list)

# Contact Page
@app.route('/contact')
def contact():
    return render_template('contact.html', title='Contact Us')

# Admin Page
@app.route('/admin')
def admin():
    return render_template('admin.html', title='Admin Panel')

if __name__ == '__main__':
    app.run(debug=True)
