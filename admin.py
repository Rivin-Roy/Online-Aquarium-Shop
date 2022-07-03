from flask import *
from database import *
import uuid

admin=Blueprint('admin',__name__)

@admin.route('/admin_home')
def admin_home():
	if session.get('username'):
		return render_template('admin_home.html')
	else:
		return redirect(url_for('public.public_login'))


@admin.route('/admin_manage_staff',methods=['get','post'])
def admin_manage_staff():

	if session.get('username'):

		data={}

		if 'submit' in request.form:
			fname=request.form['fname']
			lname=request.form['lname']
			phone=request.form['phone']
			email=request.form['email']
			hname=request.form['hname']
			city=request.form['city']
			state=request.form['state']
			pin=request.form['pin']
			# quali=request.form['quali']
			# designation=request.form['designation']
			pword=request.form['pword']

			q="select * from staff where email='%s'"%(email)
			res=select(q)
			if res:
				flash('username already exists')
			else:

				q="INSERT INTO `login`(`username`,`password`,`usertype`)VALUES('%s','%s','staff')"%(email,pword)
				insert(q)
				q1="INSERT INTO `staff`(`username`,`first_name`,`last_name`,`phone`,`email`,`house`,`city`,`state`,`pin`,`qualification`,`doj`,`designation`,s_status)VALUES('%s','%s','%s','%s','%s','%s','%s','%s','%s','none',curdate(),'none','active')"%(email,fname,lname,phone,email,hname,city,state,pin)
				insert(q1)

				flash("REGISTERED SUCCESSFULLY ")

			return redirect(url_for('admin.admin_manage_staff'))

		q="SELECT * FROM `staff`"
		res=select(q)
		data['staff']=res

		if 'action' in request.args:
			action=request.args['action']
			ids=request.args['ids']
			
		else:
			action=None

		if action=='update':
			q="SELECT * FROM `staff` WHERE username='%s'"%(ids)
			res=select(q)
			data['upstaff']=res

		if 'submits' in request.form:
			fname=request.form['fname']
			lname=request.form['lname']
			phone=request.form['phone']
			email=request.form['email']
			hname=request.form['hname']
			city=request.form['city']
			state=request.form['state']
			pin=request.form['pin']
			# quali=request.form['quali']
			# designation=request.form['designation']
			
			q="UPDATE `staff` SET username='%s',`first_name`='%s',`last_name`='%s',`phone`='%s',`email`='%s',`house`='%s',`city`='%s',`state`='%s',`pin`='%s' WHERE `username`='%s'"%(email,fname,lname,phone,email,hname,city,state,pin,ids)
			update(q)
			q1="UPDATE `login` SET `username`='%s' WHERE username='%s'"%(email,ids)
			update(q1)

			flash("UPDATED SUCCESSFULLY")

			return redirect(url_for('admin.admin_manage_staff'))

		if action=='active':
			q="update staff set s_status='active' WHERE `username`='%s'"%(ids)
			update(q)
			flash("Activated")

			return redirect(url_for('admin.admin_manage_staff'))
		if action=='inactive':	
			q1="update staff set s_status='inactive' WHERE `username`='%s'"%(ids)
			update(q1)

			flash("Inactivated")

			return redirect(url_for('admin.admin_manage_staff'))

		return render_template('admin_manage_staff.html',data=data)

	else:
		return redirect(url_for('public.public_login'))

@admin.route('/admin_manage_category',methods=['get','post'])
def admin_manage_category():

	if session.get('username'):
		data={}

		if 'action' in request.args:
			action=request.args['action']
			ids=request.args['ids']
			
		else:
			action=None

		if action=='inactive':
			q="update `category` set c_status='inactive' WHERE `category_id`='%s'"%(ids)
			update(q)
			flash("Inactivated")
			return redirect(url_for('admin.admin_manage_category'))
		if action=='active':
			q="update `category` set c_status='active' WHERE `category_id`='%s'"%(ids)
			update(q)
			flash("Activated")
			return redirect(url_for('admin.admin_manage_category'))	

		if action=='update':
			q="select * from category WHERE `category_id`='%s'"%(ids)
			data['update_view']=select(q)

		if 'update_submit' in request.form:
			cat=request.form['cat']

			q="UPDATE `category` set `category`='%s' where category_id='%s'"%(cat,ids)
			insert(q)
			flash("Updated Successfully")
			return redirect(url_for('admin.admin_manage_category'))

		if 'submit' in request.form:
			cat=request.form['cat']

			q="INSERT INTO `category`(`category`,c_status) VALUES('%s','active')"%(cat)
			insert(q)
			flash("ADDED SUCCESSFULLY")
			return redirect(url_for('admin.admin_manage_category'))

		q="SELECT * FROM `category`"
		res=select(q)
		data['cat']=res
		return render_template('admin_manage_category.html',data=data)
	else:
		return redirect(url_for('public.public_login'))

@admin.route('/admin_manage_subcategory',methods=['get','post'])
def admin_manage_subcategory():
	if session.get('username'):

		data={}
		ids=request.args['ids']
		data['ids']=ids

		if 'action' in request.args:
			action=request.args['action']
			ids1=request.args['ids1']
			
		else:
			action=None

		if action=='inactive':
			q1="update `subcategory` set sub_status='inactive' WHERE `subcategory_id`='%s'"%(ids1)
			update(q1)
			flash("Inactivated")
			return redirect(url_for('admin.admin_manage_subcategory',ids=ids))
		if action=='active':
			q1="update `subcategory` set sub_status='active' WHERE `subcategory_id`='%s'"%(ids1)
			update(q1)
			flash("Activated")
			return redirect(url_for('admin.admin_manage_subcategory',ids=ids))	

		if action=='update':
			q1="select * FROM `subcategory` WHERE `subcategory_id`='%s'"%(ids1)
			data['update_view']=select(q1)

		if 'update_submit' in request.form:
			sname=request.form['sname']

			q="Update `subcategory` set `subcategory`='%s' where `category_id`='%s'"%(sname,ids)
			update(q)
			flash("UPDATED SUCCESSFULLY")
			return redirect(url_for('admin.admin_manage_subcategory',ids=ids))

		if 'submit' in request.form:
			sname=request.form['sname']

			q="INSERT INTO `subcategory`(`category_id`,`subcategory`,sub_status) VALUES('%s','%s','active')"%(ids,sname)
			insert(q)
			flash("ADDED SUCCESSFULLY")
			return redirect(url_for('admin.admin_manage_subcategory',ids=ids))

		q="SELECT * FROM `subcategory` INNER JOIN `category` USING(`category_id`) WHERE `category_id`='%s'"%(ids)
		res=select(q)
		data['subcat']=res

		return render_template('admin_manage_subcategory.html',data=data)
	else:
		return redirect(url_for('public.public_login'))


@admin.route('/admin_manage_breeds',methods=['get','post'])
def admin_manage_breeds():

	if session.get('username'):

		data={}

		q="SELECT * FROM `subcategory` where sub_status='active'"
		res=select(q)
		data['sub']=res

		if 'submit' in request.form:
			subcat=request.form['subcat']
			breed=request.form['breed']

			q="INSERT INTO `breeds`(subcategory_id,`breed`,b_status)VALUES('%s','%s','active')"%(subcat,breed)
			insert(q)

			flash("ADDED SUCCESSFULLY")

			return redirect(url_for('admin.admin_manage_breeds'))

		q="SELECT * FROM `breeds` inner join subcategory using(subcategory_id)"
		res=select(q)
		data['breeds']=res

		if 'action' in request.args:
			action=request.args['action']
			bid=request.args['bid']
		else:
			action=None

		if action=='inactive':
			q="update `breeds` set b_status='inactive' WHERE `breed_id`='%s'"%(bid)
			update(q)
			flash("Inactivated")
			return redirect(url_for('admin.admin_manage_breeds'))
		if action=='active':
			q="update `breeds` set b_status='active' WHERE `breed_id`='%s'"%(bid)
			update(q)
			flash("Activated")
			return redirect(url_for('admin.admin_manage_breeds'))	

		if action=='update':
			q="SELECT * FROM breeds WHERE breed_id='%s'"%(bid)
			res=select(q)
			data['upbreed']=res

		if 'submits' in request.form:
			subcat=request.form['subcat']
			breed=request.form['breed']
			print(subcat)
			q="UPDATE `breeds` SET breed='%s',subcategory_id='%s' WHERE breed_id='%s'"%(breed,subcat,bid)
			update(q)
			
			flash("UPDATED SUCCESSFULLY")

			return redirect(url_for('admin.admin_manage_breeds'))


		return render_template('admin_manage_breeds.html',data=data)

	else:

		return redirect(url_for('public.public_login'))

@admin.route('/admin_manage_vendor',methods=['get','post'])
def admin_manage_vendor():

	if session.get('username'):

		data={}

		if 'submit' in request.form:
			companyname=request.form['company_name']
			email=request.form['email']
			phone=request.form['phone']
			hname=request.form['hname']
			place=request.form['place']
			pin=request.form['pin']
			dist=request.form['dist']

			q="INSERT INTO `vendor`(`company_name`,`email`,`phone`,`house`,`place`,`pincode`,`district`,v_status)VALUES('%s','%s','%s','%s','%s','%s','%s','active')"%(companyname,email,phone,hname,place,pin,dist)
			insert(q)

			flash("ADDED SUCCESSFULLY")

			return redirect(url_for('admin.admin_manage_vendor'))

		q1="select * from vendor"
		res=select(q1)
		data['vendor']=res

		if 'action' in request.args:
			action=request.args['action']
			ids=request.args['ids']
		else:
			action=None

		if action=='update':
			q="SELECT * FROM `vendor` WHERE `vendor_id`='%s'"%(ids)
			res=select(q)
			data['upvendor']=res

		if 'submits' in request.form:
			companyname=request.form['company_name']
			email=request.form['email']
			phone=request.form['phone']
			hname=request.form['hname']
			place=request.form['place']
			pin=request.form['pin']
			dist=request.form['dist']

			qry="UPDATE `vendor` SET `company_name`='%s',`email`='%s',`phone`='%s',`house`='%s',`place`='%s',`pincode`='%s',`district`='%s' WHERE `vendor_id`='%s'"%(companyname,email,phone,hname,place,pin,dist,ids)
			update(qry)

			flash("UPDATED SUCCESSFULLY")

			return redirect(url_for('admin.admin_manage_vendor'))

		if action=='inactive':
			q="update vendor set v_status='inactive'  WHERE `vendor_id`='%s'"%(ids)
			update(q)
			flash("Inactivated")
			return redirect(url_for('admin.admin_manage_vendor'))
		if action=='active':
			q="update vendor set v_status='active'  WHERE `vendor_id`='%s'"%(ids)
			update(q)
			flash("Activated")
			return redirect(url_for('admin.admin_manage_vendor'))	

		return render_template('admin_manage_vendor.html',data=data)

	else:

		return redirect(url_for('public.public_login'))

@admin.route('/admin_manage_fish',methods=['get','post'])
def admin_manage_fish():
	data={}
	brid=request.args['brid']
	data['brid']=brid
	# vid=request.args['vid']
	# data['vid']=vid
	if session.get('username'):
		

		# q="SELECT * FROM `breeds` where b_status='active'"
		# res=select(q)
		# data['breed']=res

		# q1="SELECT * FROM `vendor` where v_status='active'"
		# res=select(q1)
		# data['vendor']=res

		if 'action' in request.args:
			action=request.args['action']
			ids=request.args['ids']

			
		else:
			action=None

		if action=='inactive':
			q="update `items` set i_status='inactive' WHERE `item_id`='%s'"%(ids)
			update(q)
			flash("Inactivated")
			return redirect(url_for('admin.admin_manage_fish',bid=bid))
		if action=='active':
			q="update `items` set i_status='active' WHERE `item_id`='%s'"%(ids)
			update(q)
			flash("Activated")
			return redirect(url_for('admin.admin_manage_fish',bid=bid))	

		if action=='update':
			q="SELECT * FROM `items` INNER JOIN `breeds` ON `breed_id`=`items`.`selected_id`  WHERE `item_id`='%s'"%(ids)
			res=select(q)
			data['upfish']=res

		if 'submits' in request.form:
			
			product=request.form['product']
			# brand=request.form['brand']
			# amount=request.form['amount']
			image=request.files['image']
			path="static/"+str(uuid.uuid4())+image.filename
			image.save(path)
			desc=request.form['desc']
			if image.filename:
				q="UPDATE `items` SET `product`='%s',brand='hju',image='%s',description='%s' WHERE `item_id`='%s'"%(product,path,desc,ids)
				update(q)
				flash("UPDATED SUCCESSFULLY")
				return redirect(url_for('admin.admin_manage_fish',brid=brid))
			else:
				q="UPDATE `items` SET `product`='%s',brand='hju',`quantity`='%s',`amount`='%s',description='%s' WHERE `item_id`='%s'"%(product,quantity,amount,desc,ids)
				update(q)
				flash("UPDATED SUCCESSFULLY")
				return redirect(url_for('admin.admin_manage_fish',ids=ids))


		if 'submit' in request.form:
			
			product=request.form['product']
			# brand=request.form['brand']
			# quantity=request.form['quantity']
			# amount=request.form['amount']
			image=request.files['image']
			path="static/"+str(uuid.uuid4())+image.filename
			image.save(path)
			desc=request.form['desc']

			q="insert into items VALUES(null,'%s','fish','%s','hju','0','0','%s','%s','active','0')"%(brid,product,path,desc)
			insert(q)
			flash("ADDED SUCCESSFULLY")
			return redirect(url_for('admin.admin_manage_fish',brid=brid))

		q="SELECT * FROM `items` INNER JOIN `breeds` ON `breed_id`=`items`.`selected_id`  where type='fish'"
		res=select(q)
		data['fish']=res
		return render_template('admin_manage_fish.html',data=data)
	else:
		return redirect(url_for('public.public_login'))

@admin.route('/admin_manage_equipments',methods=['get','post'])
def admin_manage_equipments():
	data={}
	subid=request.args['subid']
	data['subid']=subid
	
	if session.get('username'):
		data={}
		qry="SELECT * FROM `subcategory` where sub_status='active'"
		res=select(qry)
		data['subcategory']=res
		
		if 'action' in request.args:
			action=request.args['action']
			ids=request.args['ids']
			
		else:
			action=None

		if action=='inactive':
			q="update `items` set i_status='inactive' WHERE `item_id`='%s'"%(ids)
			update(q)
			flash("Inactivated")
			return redirect(url_for('admin.admin_manage_equipments',subid=subid))
		if action=='active':
			q="update `items` set i_status='active' WHERE `item_id`='%s'"%(ids)
			update(q)
			flash("Activated")
			return redirect(url_for('admin.admin_manage_equipments',subid=subid))	

		if action=='update':
			q="SELECT * FROM `items` INNER JOIN `subcategory` ON `subcategory_id`=`items`.`selected_id`  WHERE `item_id`='%s'"%(ids)
			res=select(q)
			data['update_view']=res

		if 'update_submit' in request.form:
			
			product=request.form['product']
			brand=request.form['brand']
			# amount=request.form['amount']
			image=request.files['image']
			path="static/"+str(uuid.uuid4())+image.filename
			image.save(path)
			desc=request.form['desc']
			if image.filename:
				q="UPDATE `items` SET `product`='%s',brand='%s',image='%s',description='%s' WHERE `item_id`='%s'"%(product,brand,path,desc,ids)
				print(q)
				update(q)
				flash("UPDATED SUCCESSFULLY")
				return redirect(url_for('admin.admin_manage_equipments',subid=subid))
			else:
				q="UPDATE `items` SET `product`='%s',brand='%s',`description`='%s' WHERE `item_id`='%s'"%(product,brand,desc,ids)
				update(q)
				flash("UPDATED SUCCESSFULLY")
				return redirect(url_for('admin.admin_manage_equipments',subid=subid))


		if 'submit' in request.form:
			
			
			product=request.form['product']
			brand=request.form['brand']
			image=request.files['image']
			path="static/"+str(uuid.uuid4())+image.filename
			image.save(path)
			desc=request.form['desc']

			q="insert into items VALUES(null,'%s','equipments','%s','%s','0','0','%s','%s','active','0')"%(subid,product,brand,path,desc)
			insert(q)
			flash("ADDED")
			return redirect(url_for('admin.admin_manage_equipments',subid=subid))

		q="SELECT * FROM `items` INNER JOIN `subcategory` ON `subcategory_id`=`items`.`selected_id` where type='equipments'"
		res=select(q)
		data['equip']=res
		return render_template('admin_manage_equipments.html',data=data)
	else:
		return redirect(url_for('public.public_login'))


@admin.route('/admin_view_booking')
def admin_view_booking():

	if session.get('username'):

		data={}

		if 'action' in request.args:
			action=request.args['action']
			ids=request.args['ids']
			
		else:
			action=None

		if action=='ship':
			q="update booking set `status`='shipped' WHERE `booking_id`='%s'"%(ids)
			update(q)
			flash('Shipped')
			return redirect(url_for('admin.admin_view_booking'))
		if action=='deliver':
			q="update booking set `status`='delivered' WHERE `booking_id`='%s'"%(ids)
			update(q)
			flash('Delivered')
			return redirect(url_for('admin.admin_view_booking'))

		q="SELECT *,CONCAT(`first_name`,' ',`last_name`) AS customer_name FROM `booking` INNER JOIN `customer` USING (`customer_id`)"
		res=select(q)
		data['bookings']=res

		return render_template('admin_view_booking.html',data=data)

	else:

		return redirect(url_for('public.public_login'))

@admin.route('/admin_view_feedback')
def admin_view_feedback():

	if session.get('username'):

		data={}

		q="SELECT *,CONCAT(`first_name`,' ',`last_name`) AS customer_name FROM `feedback` INNER JOIN `customer` USING (`customer_id`)"
		res=select(q)
		data['feedback']=res
		
		return render_template('admin_view_feedback.html',data=data)

	else:

		return redirect(url_for('public.public_login'))


@admin.route('/admin_view_customer')
def admin_view_customer():

	if session.get('username'):

		data={}

		q="SELECT * FROM `customer` ORDER BY first_name ASC"
		res=select(q)
		session['q']=q
		data['customer']=res
		
		return render_template('admin_view_customer.html',data=data)

	else:

		return redirect(url_for('public.public_login'))

@admin.route('/admin_customer_print',methods=['get','post'])
def admin_customer_print():
	data={}
	res=select(session['q'])
	data['customer']=res
	return render_template('admin_customer_print.html',data=data)		


@admin.route('/admin_view_vendor')
def admin_view_vendor():

	if session.get('username'):

		data={}

		q="SELECT *,CONCAT(`first_name`,' ',`last_name`) AS vname FROM `vendor`"
		res=select(q)
		data['vendor']=res
		
		return render_template('admin_view_vendor.html',data=data)

	else:

		return redirect(url_for('public.public_login'))


@admin.route('/admin_view_staffreport',methods=['get','post'])
def admin_view_staffreport():

	if session.get('username'):

		data={}

		if 'submit' in request.form:
			fdate=request.form['fdate']
			tdate=request.form['tdate']
			q="SELECT * FROM `staff`  WHERE `doj` BETWEEN '%s' AND '%s'"%(fdate,tdate)
			res=select(q)
			data['staff']=res
			session['q']=q
		
		return render_template('admin_view_staffreport.html',data=data)

	else:

		return redirect(url_for('public.public_login'))

@admin.route('/admin_staff_print',methods=['get','post'])
def admin_staff_print():
	data={}
	res=select(session['q'])
	data['staff']=res
	return render_template('admin_staff_print.html',data=data)		

@admin.route('/admin_view_item_report',methods=['get','post'])
def admin_view_item_report():

	if session.get('username'):

		data={}
		q="SELECT * FROM `items` INNER JOIN `breeds` ON `breeds`.`breed_id`=`items`.`selected_id`"
		res=select(q)
		data['item']=res
		session['q']=q
		return render_template('admin_view_item_report.html',data=data)
	else:
		return redirect(url_for('public.public_login'))		


@admin.route('/admin_view_payment_report',methods=['get','post'])
def admin_view_payment_report():

	if session.get('username'):

		data={}

		if 'submit' in request.form:
			fdate=request.form['fdate']
			tdate=request.form['tdate']
			q="SELECT * FROM `payment` inner join booking using(booking_id) INNER JOIN `customer` USING(`customer_id`) WHERE payment.`date` BETWEEN '%s' AND '%s'"%(fdate,tdate)
			res=select(q)
			session['q']=q
			data['payment']=res
		
		return render_template('admin_view_payment_report.html',data=data)

	else:

		return redirect(url_for('public.public_login'))

@admin.route('/admin_payment_print',methods=['get','post'])
def admin_payment_print():
	data={}
	res=select(session['q'])
	data['payment']=res
	return render_template('admin_payment_print.html',data=data)		

@admin.route('/admin_view_order_report',methods=['get','post'])
def admin_view_order_report():

	if session.get('username'):

		data={}

		if 'submit' in request.form:
			fdate=request.form['fdate']
			tdate=request.form['tdate']
			q="SELECT *,CONCAT(`first_name`,' ',`last_name`) AS customer_name FROM `booking` INNER JOIN `customer` USING (`customer_id`) WHERE `booking`.`date` BETWEEN '%s' AND '%s'"%(fdate,tdate)
			res=select(q)
			session['q']=q
			data['bookings']=res
		return render_template('admin_view_order_report.html',data=data)

	else:

		return redirect(url_for('public.public_login'))	


@admin.route('/admin_order_print',methods=['get','post'])
def admin_order_print():
	data={}
	res=select(session['q'])
	data['bookings']=res
	return render_template('admin_order_print.html',data=data)

@admin.route('/admin_view_purchase_report',methods=['get','post'])
def admin_view_purchase_report():

	if session.get('username'):

		data={}

		if 'submit' in request.form:
			fdate=request.form['fdate']
			tdate=request.form['tdate']
			q="SELECT *,`purchasemaster`.`amount` AS pamount,`purchasechild`.`amount` AS camount FROM `purchasemaster` INNER JOIN `purchasechild` USING(pmaster_id) INNER JOIN `vendor` USING(vendor_id) INNER JOIN `items` USING(item_id) WHERE `purchasemaster`.`date` BETWEEN '%s' AND '%s'"%(fdate,tdate)
			res=select(q)
			session['q']=q
			
			data['purchase']=res
		
		return render_template('admin_view_purchase_report.html',data=data)

	else:

		return redirect(url_for('public.public_login'))

@admin.route('/admin_purchase_print',methods=['get','post'])
def admin_purchase_print():
	data={}
	res=select(session['q'])
	data['purchase']=res
	return render_template('admin_purchase_print.html',data=data)		

# @admin.route('/admin_order_print',methods=['get','post'])
# def admin_order_print():
# 	data={}
# 	res=select(session['q'])
# 	data['bookings']=res
# 	return render_template('admin_order_print.html',data=data)


@admin.route('/admin_view_category')
def admin_view_category():
	data={}
	q="SELECT * FROM `category` where c_status='active'"
	res=select(q)
	data['cat']=res
	return render_template('admin_view_category.html',data=data)

@admin.route('/admin_select_subcategory')
def admin_select_subcategory():
	cat_id=request.args['cat_id']
	data={}
	q="SELECT * FROM `subcategory` inner join category using(category_id) where category_id='%s'"%(cat_id)
	res=select(q)
	data['subcat']=res
	return render_template('admin_view_subcategory.html',data=data)

@admin.route('/admin_select_breed')
def admin_select_breed():
	subid=request.args['subid']
	data={}
	q="SELECT * FROM `breeds` inner join subcategory using(subcategory_id) where subcategory_id='%s'"%(subid)
	res=select(q)
	data['breed']=res
	return render_template('admin_select_breed.html',data=data)
@admin.route('/admin_select_vend')
def admin_select_vend():
	data={}
	brid=request.args['brid']
	data['bid']=brid
	
	q="select * from vendor"
	res=select(q)
	data['vendor']=res
	return render_template('admin_view_vendr.html',data=data,bid=brid)

@admin.route('/admin_select_vendor')
def admin_select_vendor():
	subid=request.args['subid']
	data={}
	data['subid']=subid
	
	q="select * from vendor"
	res=select(q)
	data['vendor']=res
	return render_template('admin_view_vendr.html',data=data,subid=subid)



@admin.route('/admin_select_vendor1')
def admin_select_vendor1():
	data={}
	q="select * from vendor"
	res=select(q)
	data['vendor']=res
	return render_template('admin_select_vendor.html',data=data)

@admin.route('/admin_select_item')
def admin_select_item():
	data={}
	vid=request.args['vid']
	data['vid']=vid
	
	q="select * from items"
	res=select(q)
	data['items']=res
	return render_template('admin_select_item.html',data=data)

@admin.route('/adminmanagepurchase',methods=['get','post'])
def adminmanagepurchase():
	data={}
	vid=request.args['vid']
	data['vid']=vid
	item_id=request.args['item_id']
	data['item_id']=item_id

	# amount=request.args['amount']
	# data['amount']=amount
	if not session.get("username") is None:
		
		
		q="select * from items where item_id='%s'"%(item_id)
		res=select(q)
		data['item']=res

		q="SELECT *,`purchasemaster`.`amount` AS pamount,`purchasechild`.`amount` AS camount FROM `purchasemaster` INNER JOIN `purchasechild` USING(pmaster_id) INNER JOIN `vendor` USING(vendor_id) INNER JOIN `items` USING(item_id)"
		res=select(q)
		data['purchase']=res
		if 'action' in request.args:
			action=request.args['action']
			pid=request.args['pid']
			item_id=request.args['item_id']
		else:
			action=None
		if action=="active":
			q="update purchasemaster set status='active' where pmaster_id='%s'"%(pid)
			update(q)
			flash("Activated")
			return redirect(url_for('admin.adminmanagepurchase',vid=vid,item_id=item_id,pid=pid))
		if action=="inactive":
			q="update purchasemaster set status='inactive' where pmaster_id='%s'"%(pid)
			update(q)
			flash("Inactivated")			
			return redirect(url_for('admin.adminmanagepurchase',vid=vid,item_id=item_id,pid=pid))
		if "purchase" in request.form:
			sp=request.form['sp']
			amount=request.form['amount']
			quantity=request.form['quantity']
			total=request.form['total']
			
			
			q="select * from purchasemaster where vendor_id='%s' and status='pending'" %(vid)
			res=select(q)
			if res:	
				ids=res[0]['pmaster_id']
				q="update purchasemaster set amount=amount+'%s' where pmaster_id='%s'" %(total,ids)
				update(q)
				
			else:
				q="insert into purchasemaster values(null,'%s','%s',curdate(),'pending')" %(vid,total)
				ids=insert(q)
			q="insert into purchasechild values(null,'%s','%s','%s','%s')" %(ids,item_id,total,total)
			insert(q)
			flash("ADDED SUCCESSFULLY")
			q="update items set quantity=quantity+'%s',amount='%s',cost_price='%s' where item_id='%s'"%(quantity,sp,amount,item_id)
			update(q)
			flash("UPDATED SUCCESSFULLY")
			return redirect(url_for('admin.adminmanagepurchase',vid=vid,item_id=item_id))


		return render_template("adminmanagepurchase.html",data=data)
	else:
		return redirect(url_for("public.login"))

@admin.route('/admin_view_cancelled_order')
def admin_view_cancelled_order():
	data={}
	q="SELECT * FROM `booking` inner join customer using(customer_id) where status='cancel'"
	res=select(q)
	data['bookings']=res
	return render_template('admin_view_cancelled_order.html',data=data)

@admin.route('/admin_print')
def admin_print():
	data={}
	q="SELECT * FROM `items` INNER JOIN `breeds` ON `breeds`.`breed_id`=`items`.`selected_id`"
	res=select(q)
	data['item']=res
	return render_template('admin_print.html',data=data)


	
