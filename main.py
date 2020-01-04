from flask import Flask, request
from fractions import Fraction

app = Flask(__name__)

@app.route('/')
def index():
    if request.method == 'POST':
        num1 = request.form['num1']
        num2 = request.form['num2']
        operation = request.form['operation']
    return 'Usage;\n<Operation>?A=<V1>&B=<V2>\n'


@app.route('/add')
def addition():
    try:
        num1, num2 = take_inputs()
        result = num1 + num2
    except ValueError:
        warning_msg = take_inputs()
        return warning_msg
    else:
        if float(result).is_integer():
            result = int(result)
            return '%d \n' % result
        return '%.2f \n' % result

@app.route('/sub')
def substraction():
    try:
        num1, num2 = take_inputs()
        result = num1 - num2
    except ValueError:
        warning_msg = take_inputs()
        return warning_msg
    else:
        if float(result).is_integer():
            result = int(result)
            return '%d \n' % result
        return '%.2f \n' % result

@app.route('/mul')
def multiplication():
    try:
        num1, num2 = take_inputs()
        result = num1 * num2
    except ValueError:
        warning_msg = take_inputs()
        return warning_msg
    else:
        if float(result).is_integer():
            result = int(result)
            return '%d \n' % result
        return '%.2f \n' % result


@app.route('/div')
def division():
    try:
        num1, num2 = take_inputs()
        result = num1 / num2
    except ValueError:
        warning_msg = take_inputs()
        return warning_msg
    else:
        if float(result).is_integer():
            result = int(result)
            return '%d \n' % result
        return '%.2f \n' % result


if __name__ == "__main__":
    app.run()