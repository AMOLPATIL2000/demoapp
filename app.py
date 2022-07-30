from flask import Flask  
app = Flask('demo') #creating the Flask class object  
 
@app.route('/') #decorator drfines the   
def home():  
    return "hello";  
  
app.run(debug = True)  
