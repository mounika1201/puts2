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


@app.route('/sub')
def subtraction():
    elif operation == 'subtract':
            sum = float(num1) - float(num2)
    
            return '%d \n' % result
        return '%.2f \n' % result

if __name__ == "__main__":
    app.run()