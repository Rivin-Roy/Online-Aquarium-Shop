from flask import *
from database import *
import random
import smtplib
from email.mime.text import MIMEText
from flask_mail import Mail

public=Blueprint('public',__name__)
@public.route('/')
def index():
	return render_template('index.html')

@public.route('/public_home')
def public_home():
	session.clear()
	data={}
	q="SELECT * FROM `items` "
	data['items']=select(q)
	return render_template('public_home.html',data=data)

@public.route('/public_login',methods=['get','post'])
def public_login():
	session.clear()
	if 'submit' in request.form:
		uname=request.form['uname']
		pword=request.form['pword']

		q="SELECT * FROM `login` WHERE `username`='%s' AND PASSWORD='%s'"%(uname,pword)
		res=select(q)

		if res:

			session['username']=res[0]['username']


			if res[0]['usertype']=='admin':

				flash('WELCOME ADMIN')

				return redirect(url_for('admin.admin_home'))

			if res[0]['usertype']=='staff':
				print(".........................")

				q="SELECT * FROM staff WHERE `username`='%s'"%(session['username'])
				res=select(q)

				session['sid']=res[0]['staff_id']

				return redirect(url_for('staff.staff_home'))

			if res[0]['usertype']=='customer':

				q="SELECT * FROM customer WHERE `username`='%s'"%(session['username'])
				res=select(q)

				session['cid']=res[0]['customer_id']

				return redirect(url_for('customer.customer_home'))
		else:

			flash('INVALID USERNAME OR PASSWORD')

			return redirect(url_for('public.public_login'))

	if 'forgott' in request.form:
		return redirect(url_for('public.forgotpassword'))
	return render_template('public_login.html')

@public.route('/customer_register',methods=['get','post'])
def customer_register():
	session.clear()
	if 'submit' in request.form:
		fname=request.form['fname']
		lname=request.form['lname']
		phone=request.form['phone']
		hname=request.form['hname']
		place=request.form['place']
		district=request.form['district']
		pin=request.form['pin']
		email=request.form['email']
		pword=request.form['pword']

		q="select * from customer where email='%s'"%(email)
		res=select(q)
		if res:
			flash('username already exists')
		else:

			q="INSERT INTO `login`(`username`,`password`,`usertype`) VALUES('%s','%s','customer')"%(email,pword)
			insert(q)
			q1="INSERT INTO `customer`(`username`,`first_name`,`last_name`,`phone`,`house`,`place`,`district`,`pincode`,`email`) VALUES('%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(email,fname,lname,phone,hname,place,district,pin,email)
			insert(q1)
			
			flash("REGISTERED SUCCESSFULLY")
			return redirect(url_for('public.customer_register'))

	return render_template('customer_register.html')

@public.route('/forgotpassword',methods=['get','post'])
def forgotpassword():
	data={}
	if 'next' in request.form:
		ph=request.form['ph']
		uname=request.form['uname']
		q="select email,username from login inner join customer using(username) where username='%s' and phone='%s' union select email,username from login inner join staff using(username) where username='%s' and phone='%s' "%(uname,ph,uname,ph)
		print(q)
		res=select(q)
		print(res)
		if res:
			print(res)
			session['uname']=res[0]['username']
			# email=res[0]['email']
			email=res[0]['email']
			print(email)
			rd=random.randrange(1000,9999,4)
			msg=str(rd)
			data['rd']=rd
			print(rd)
			try:
				gmail = smtplib.SMTP('smtp.gmail.com', 587)
				gmail.ehlo()
				gmail.starttls()
				gmail.login('annababykp@gmail.com','Anna@1998')
			except Exception as e:
				print("Couldn't setup email!!"+str(e))

			msg = MIMEText(msg)

			msg['Subject'] = 'OTP FOR PASSWORD RECOVRY'

			msg['To'] = email

			msg['From'] = 'annababykp@gmail.com'

			try:

				gmail.send_message(msg)
				print(msg)
				flash("EMAIL SEND SUCCESFULLY")
				session['rd']=rd
				return redirect(url_for('public.enterotp'))


			except Exception as e:
				print("COULDN'T SEND EMAIL", str(e))
				return redirect(url_for('public.forgotpassword'))
		else:
			flash("INVALID DETAILS")
			return redirect(url_for('public.forgotpassword'))
	return render_template("forgotpassword.html",data=data)



@public.route('/enterotp',methods=['get','post'])
def enterotp():
	rd=session['rd']
	uname=session['uname']
	data={}
	if "otp" in request.form:
		otp=request.form['otp']
		if int(otp)==int(rd):
			data['chp']=uname
		else:
			flash("invalid otp")
			return redirect(url_for('public.forgotpassword'))


	if 'update' in request.form:
		uname=request.form['uname']
		p=request.form['pwd']
		cp=request.form['pwds']
		if p==cp:
			print("+++++++++++")
			q="update login set password='%s' where username='%s'"%(p,uname)
			update(q)
			flash("UPDATED SUCCESSFULLY")
			return redirect(url_for('public.public_login'))
		else:
			flash("PASSWORD MISMATCH")
			data['chp']=uname
	return render_template("enterotp.html",data=data)		