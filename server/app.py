#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:param>')
def print_string(param):
    print(param)
    return param

@app.route('/count/<int:n>')
def count(n):
    if n < 1:
        print('Please enter a positive integer.')
        return
    output = '\n'.join(str(i) for i in range(n)) + '\n'
    print(output)
    return output

@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math (num1, operation, num2):
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        if num2 == 0:
            return "Error: Division by zero is not allowed", 400
        result = num1 / num2
    elif operation == '%':
        result = num1 % num2
    else:
        return 'Invalid operation', 400
    return str(result)

if __name__ == '__main__':
    app.run(port=5555, debug=True)



