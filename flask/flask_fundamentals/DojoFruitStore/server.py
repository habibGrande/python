from flask import Flask, render_template, request, redirect
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    print(request.form)
    apple = request.form['apple']
    raspberry = request.form['raspberry']
    Strawberry = request.form['strawberry']
    name = request.form['first_name']
    lastName = request.form['last_name']
    id = request.form['student_id']
    print(name,lastName,raspberry,Strawberry,apple)
    
    return render_template("checkout.html",name = name, lastName= lastName,id = id, newapple = apple,newraspberry=raspberry,newStrawberry=Strawberry )

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    