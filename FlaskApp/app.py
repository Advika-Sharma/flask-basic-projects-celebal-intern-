from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello World</h1>'

@app.route('/hello/<user>')
def hello_name(user):
    return render_template('hello.html', name=user)

@app.route('/score/<int:score>')
def hello_score(score):
    return render_template('hello.html', marks=score)

@app.route('/result')
def result():
    result_dict = {'phy': 50, 'che': 60, 'maths': 70}
    return render_template('result.html', result=result_dict)

if __name__ == '__main__':
    app.run(debug=True)
    
#to run use the following command 
#http://127.0.0.1:5000/hello/Advika → dynamic name
#http://127.0.0.1:5000/score/75 → conditional logic
#http://127.0.0.1:5000/result → loop and table output
