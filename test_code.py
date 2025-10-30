from flask import Flask, jsonify

app = Flask(__name__)

# 1. Home route
@app.route('/')
def home():
    return "Welcome to the Flask App!"

# 2. About route
@app.route('/about')
def about():
    return "This is a simple Flask application with 5 routes."

# 3. Dynamic route with name parameter
@app.route('/greet/<name>')
def greet(name):
    return f"Hello, {name.capitalize()}! Welcome to the app."

# 4. Route with integer parameter and simple logic
@app.route('/square/<int:number>')
def square(number):
    result = number ** 2
    return f"The square of {number} is {result}."

# 5. Route returning JSON
@app.route('/json')
def json_example():
    data = {
        "message": "Hello from the JSON route!",
        "status": "success",
        "routes": 5
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
