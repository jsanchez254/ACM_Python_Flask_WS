from flask import Flask, render_template, request, url_for 
from flask_cors import CORS
from flask_mail import Message, Mail

app = Flask(__name__)
CORS(app)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'thehedgehogs620@gmail.com'
app.config['MAIL_PASSWORD'] = 'acm12345%'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)

@app.route("/")
def home():
       return render_template('./home.html')   

@app.route("/sendEmail", methods = ['POST', 'GET'])
def sendEmail():
       return render_template('./sendEmail.html')

@app.route("/sendEmail1", methods = ['POST', 'GET'])        
def sendEmail1():
       email = request.args.get("email")
       message = request.args.get("message")
      
       msg = Message("wow", sender="thehedgehogs620@gmail.com", recipients=[str(email)])
       msg.body = message
       mail.send(msg)
       return render_template('./emailSent.html')       

if __name__ == '__main__':
    app.run(debug = True)