from  flask import Flask,render_template
app = Flask(__name__)
@app.route('/play')
def play():
    return render_template('index.html')  



@app.route('/page/<number>')

def page(number):
    number = int(number)
    return render_template('playground.html', number = number)

@app.route('/pageGraound/<number>/<color>')

def pageGraound(number, color):
    number = int(number)
    return render_template('backGroundPage.html', number = number, color = color)
if __name__=="__main__":
    app.run(debug=True)