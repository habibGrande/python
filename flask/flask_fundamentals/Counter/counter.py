from flask import Flask, render_template, session
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'
@app.route('/')
def main():
    if 'counter' not in session:
        session['counter'] = 1
    else:
        session['counter'] += 1
    return render_template('index.html',name_on_template=session['counter'])
@app.route('/destroy_session')
def destroy_session():
    session.clear()
    return render_template('index.html')

@app.route('/addTwo', methods=['POST'])
def addTwo():
    if 'counter' not in session:
        session['counter'] = 1
    else:
        session['counter'] += 2
    return render_template('index.html') 

@app.route('/remove', methods=['POST'])
def remove():
    session.clear()
    return render_template('index.html') 


# @app.route('/form', methods=['POST'])
# def form():
#     if 'counter' not in session:
#             session['counter'] = 1
#     else:
#         session['counter'] += 1
#     count_val = count_val+1
#     return render_template('index.html',name_on_template=session['counter'],count = count_val)
 

if __name__=="__main__":
    app.run(debug=True)