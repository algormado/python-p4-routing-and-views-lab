from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:text>')
def print_string(text):
    # Print the string to the console
    print(text)
    # Display the string in the browser
    return f'<p>Printed String: {text}</p>'

@app.route('/count/<int:num>')
def count(num):
    # Create a string of numbers from 0 to num, separated by newlines
    numbers = '\n'.join(str(i) for i in range(num + 1))  # Includes 0 through num
    return f'<pre>{numbers}</pre>'

@app.route('/math/<float:num1>/<operation>/<float:num2>')
def math(num1, operation, num2):
    # Perform the requested mathematical operation
    result = None
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        if num2 != 0:
            result = num1 / num2
        else:
            return 'Error: Division by zero!'
    elif operation == '%':
        result = num1 % num2
    else:
        return 'Invalid operation!'

    if result is not None:
        return jsonify({'result': result})  # Returning JSON response for mathematical operations
    else:
        return 'Error: Operation not recognized!'


if __name__ == '__main__':
    app.run(port=5555, debug=True)

