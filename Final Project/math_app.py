from flask import Flask, render_template, request
import mathhelper
app = Flask(__name__)

global state
state = { 'calulation':'', }

@app.route('/', methods = ['GET'])
def main():
    global state
    return render_template('main.html', state=state)

@app.route('/expression',methods=['GET', 'POST'])
def expression():
    global state
    if request.method == 'POST':
        calculate_expression()
        return render_template('expression.html',state=state)

    return render_template('expression',state=state)

@app.route('/triangle',methods=['GET', 'POST'])
def triangle():
    global state
    if request.method == 'POST':
        calculate_triangle()
        return render_template('triangle.html',state=state)

    return render_template('triangle',state=state)



def calculate_expression():
    global state
    expression = request.form['expression']
    res = mathhelper.calculate(expression)
    if res is None:
        state['calculation'] = 'Invalid expression!'
    else:
        state['calculation'] = f'The result of {expression} is {str(res)}'

def calculate_triangle():
    global state
    res = mathhelper.area_triangle(request.form['triangleBase'], request.form['triangleHeight'])
    if res is None:
        state['triangleArea'] = 'Invalid input'
    else:
        state['triangleArea'] = res
@app.route('/trapezoid', methods=['Get', 'Post']) 
def trapezoid():
    global state
    
    if request.method=='POST':
        calculate_trapezoid()
        return render_template('trapezoid.html',state=state)
    return render_template('trapezoid.html', state=state)
def calculate_expression():
    global state
    expression=request.form['expression']
    res=mathhelper.calculate(expression)
    if res is None:
        state['calculation']='Invalid expression!'
    else:
        state['calculation']=f'The result of {expression} is {str(res)}'

if __name__ == '__main__':
    app.run('0.0.0.0', port=3000, debug=True)

    


