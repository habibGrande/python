from flask import Flask , render_template
app = Flask(__name__)
@app.route("/")
def main():
    return render_template('index.html')


@app.route('/<number>')
def pageWithNumber(number,col=8):
    number = int(number)
    col = int(col)
    return render_template('pageWithNumber.html', boxNumber = number,colums = col)

@app.route('/<x>/<y>')
def cal(x,y):
    x = int(x)
    y = int(y)
    return render_template('multPage.html', firstNum = x, secNum = y)
if __name__=="__main__":
    app.run(debug=True)    