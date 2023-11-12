from flask import Flask  
app = Flask(__name__)    
@app.route('/')          

def hello_world():
    return 'Hello World!'  
    

@app.route('/dojo')
def dojo():
    return 'dojo!'  

@app.route('/say/<name>')
def say(name):

    return 'Hi ' + name +'!'  

@app.route('/repeat/<number>/<word>')
def repeat(number,word):

    return word +''+ str(number) + ' Times' 
if __name__=="__main__":      
    app.run(debug=True)  
