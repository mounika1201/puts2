from flask import Flask, request
from fractions import Fraction

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('app.html')


@app.route('/add')
def addition():
    def send(sum=sum):
    if request.method == 'POST':
        num1 = request.form['num1']
        num2 = request.form['num2']
        operation = request.form['operation']

        if operation == 'add':
            sum = float(num1) + float(num2)
            return render_template('app.html', sum=sum)

if __name__ == "__main__":
    app.run()
