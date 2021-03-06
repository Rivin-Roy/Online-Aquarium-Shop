from flask import *
from public import *
from admin import *
from staff import *
from customer import *

import smtplib
from email.mime.text import MIMEText
from flask_mail import Mail
from flask import *

app=Flask(__name__)
app.secret_key='secret_key'

app.register_blueprint(public)
app.register_blueprint(admin,url_prefix='/admin')
app.register_blueprint(staff,url_prefix='/staff')
app.register_blueprint(customer,url_prefix='/customer')

mail=Mail(app)
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'lucapaul1690@gmail.com'
app.config['MAIL_PASSWORD'] = 'lucap1690@'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

app.run(debug=True,port=5123)
