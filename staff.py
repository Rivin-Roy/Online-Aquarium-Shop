from flask import *
from database import *
import uuid

staff=Blueprint('staff',__name__)

@staff.route('/staff_home')
def staff_home():
	if session.get('username'):
		return render_template('staff_home.html')
	else:
		return redirect(url_for('public.public_login'))

@staff.route('/staff_manage_category',methods=['get','post'])
def staff_manage_category():

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
			return redirect(url_for('staff.staff_manage_category'))
		if action=='active':
			q="update `category` set c_status='active' WHERE `category_id`='%s'"%(ids)
			update(q)
			flash("Activated")
			return redirect(url_for('staff.staff_manage_category'))
			

		if 'submit' in request.form:
			cat=request.form['cat']

			q="INSERT INTO `category`(`category`,c_status) VALUES('%s','active')"%(cat)
			insert(q)
			flash(" ADDED SUCCESSFULLY")
			return redirect(url_for('staff.staff_manage_category'))

		q="SELECT * FROM `category`"
		res=select(q)
		data['cat']=res
		return render_template('staff_manage_category.html',data=data)
	else:
		return redirect(url_for('public.public_login'))

@staff.route('/staff_manage_subcategory',methods=['get','post'])
def staff_manage_subcategory():
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
			return redirect(url_for('staff.staff_manage_subcategory',ids=ids))
		if action=='active':
			q1="update `subcategory` set sub_status='active' WHERE `subcategory_id`='%s'"%(ids1)
			update(q1)
			flash("Activated")
			return redirect(url_for('staff.staff_manage_subcategory',ids=ids))
			

		if 'submit' in request.form:
			sname=request.form['sname']

			q="INSERT INTO `subcategory`(`category_id`,`subcategory`,sub_status) VALUES('%s','%s','active')"%(ids,sname)
			insert(q)

			flash(" ADDED SUCCESSFULLY")
			return redirect(url_for('staff.staff_manage_subcategory',ids=ids))

		q="SELECT * FROM `subcategory` INNER JOIN `category` USING(`category_id`) WHERE `category_id`='%s'"%(ids)
		res=select(q)
		data['subcat']=res

		return render_template('staff_manage_subcategory.html',data=data)
	else:
		return redirect(url_for('public.public_login'))

@staff.route('/staff_manage_breeds',methods=['get','post'])
def staff_manage_breeds():

	if session.get('username'):

		data={}

		q="SELECT * FROM `subcategory`"
		res=select(q)
		data['sub']=res

		if 'submit' in request.form:
			subcat=request.form['subcat']
			breed=request.form['breed']

			q="insert into breeds values(null,'%s','%s','active')"%(subcat,breed)
			insert(q)

			flash("ADDED SUCCESSFULLY")

			return redirect(url_for('staff.staff_manage_breeds'))

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
			return redirect(url_for('staff.staff_manage_breeds'))
		if action=='active':
			q="update `breeds` set b_status='active' WHERE `breed_id`='%s'"%(bid)
			update(q)
			flash("Activated")
			return redirect(url_for('staff.staff_manage_breeds'))

			


		return render_template('staff_manage_breeds.html',data=data)

	else:

		return redirect(url_for('public.public_login'))


@staff.route('/staff_manage_fish',methods=['get','post'])
def staff_manage_fish():
	data={}
	bid=request.args['bid']
	data['bid']=bid
	
	if session.get('username'):
		

		q="SELECT * FROM `breeds`"
		res=select(q)
		data['breed']=res

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
			return redirect(url_for('staff.staff_manage_fish'))
		if action=='active':
			q="update `items` set i_status='active' WHERE `item_id`='%s'"%(ids)
			update(q)
			flash("Activated")
			return redirect(url_for('staff.staff_manage_fish'))
			

		if action=='update':
			q="SELECT * FROM `items` INNER JOIN `breeds` ON breeds.`breed_id`=`items`.`selected_id`  WHERE `item_id`='%s'"%(ids)
			res=select(q)
			data['upfish']=res

		if 'submits' in request.form:
			
			
			product=request.form['product']
			# quantity=request.form['quantity']
			# amount=request.form['amount']
			image=request.files['image']
			path="static/"+str(uuid.uuid4())+image.filename
			image.save(path)
			desc=request.form['desc']
			if image.filename:
				q="UPDATE `items` SET `product`='%s',image='%s',description='%s' WHERE `item_id`='%s'"%(product,path,desc,ids)
				update(q)
				flash("UPDATED SUCCESSFULLY")
				return redirect(url_for('staff.staff_manage_fish',bid=bid))
			else:
				q="UPDATE `items` SET `product`='%s',image='%s',description='%s' WHERE `item_id`='%s'"%(product,path,desc,ids)
				update(q)
				flash("UPDATED SUCCESSFULLY")
				return redirect(url_for('staff.staff_manage_fish',bid=bid))


		if 'submit' in request.form:
			
			
			product=request.form['product']
			#brand=request.form['brand']
			# amount=request.form['amount']
			image=request.files['image']
			path="static/"+str(uuid.uuid4())+image.filename
			image.save(path)
			desc=request.form['desc']
			q="insert into items values(null,'%s','fish','vj','%s','0','0','%s','%s','active','0')"%(bid,product,path,desc)
			insert(q)
			return redirect(url_for('staff.staff_manage_fish',bid=bid))

		q="SELECT * FROM `items` INNER JOIN `breeds` ON `breed_id`=`items`.`selected_id` where type='fish'"
		res=select(q)
		data['fish']=res
		return render_template('staff_manage_fish.html',data=data)
	else:
		return redirect(url_for('public.public_login'))

@staff.route('/staff_manage_equipments',methods=['get','post'])
def staff_manage_equipments():
	data={}
	sid=request.args['sid']
	data['sid']=sid
	vid=request.args['vid']
	data['vid']=vid
	if session.get('username'):
		

		# qry="SELECT * FROM `subcategory` where sub_status='active'"
		# res=select(qry)
		# data['subcategory']=res

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
			return redirect(url_for('staff.staff_manage_equipments'))
		if action=='active':
			q="update `items` set i_status='active' WHERE `item_id`='%s'"%(ids)
			update(q)
			flash("Activated")
			return redirect(url_for('staff.staff_manage_equipments'))
			

		if action=='update':
			q="SELECT * FROM `items` INNER JOIN `subcategory` ON `subcategory_id`=`items`.`selected_id` INNER JOIN `vendor` USING(`vendor_id`) WHERE `item_id`='%s'"%(ids)
			res=select(q)
			data['upequip']=res

		if 'submits' in request.form:
			# subcat=request.form['subcat']
			# vendor=request.form['vendor']
			product=request.form['product']
			quantity=request.form['quantity']
			amount=request.form['amount']
			image=request.files['image']
			path="static/"+str(uuid.uuid4())+image.filename
			image.save(path)
			desc=request.form['desc']
			if image.filename:
				q="UPDATE `items` SET `product`='%s',`quantity`='%s',`amount`='%s',image='%s',description='%s' WHERE `item_id`='%s'"%(product,quantity,amount,path,desc,ids)
				print(q)
				update(q)
				flash("UPDATED SUCCESSFULLY")
				return redirect(url_for('staff.staff_manage_equipments',sid=sid,vid=vid))
			else:
				q="UPDATE `items` SET `product`='%s',`quantity`='%s',`amount`='%s',description='%s' WHERE `item_id`='%s'"%(product,quantity,amount,desc,ids)
				update(q)
				flash("UPDATED SUCCESSFULLY")
				return redirect(url_for('staff.staff_manage_equipments',sid=sid,vid=vid))


		if 'submit' in request.form:
			
			product=request.form['product']
			quantity=request.form['quantity']
			amount=request.form['amount']
			image=request.files['image']
			path="static/"+str(uuid.uuid4())+image.filename
			image.save(path)
			desc=request.form['desc']

			q="INSERT INTO `items`(`selected_id`,`type`,`vendor_id`,`product`,`quantity`,`amount`,image,description,i_status) VALUES('%s','equipments','%s','%s','%s','%s','%s','%s','active')"%(sid,vid,product,quantity,amount,path,desc)
			insert(q)

			flash("ADDED SUCCESSFULLY")
			return redirect(url_for('staff.staff_manage_equipments',sid=sid,vid=vid))

		q="SELECT * FROM `items` INNER JOIN `subcategory` ON `subcategory_id`=`items`.`selected_id` INNER JOIN `vendor` USING(`vendor_id`) where type='equipments'"
		res=select(q)
		data['equip']=res
		return render_template('staff_manage_equipments.html',data=data)
	else:
		return redirect(url_for('public.public_login'))

@staff.route('/staff_manage_vendor',methods=['get','post'])
def staff_manage_vendor():

	if session.get('username'):

		data={}

		

		if 'submit' in request.form:

			
			company_name=request.form['company_name']
			email=request.form['email']
			phone=request.form['phone']
			hname=request.form['hname']
			place=request.form['place']
			pin=request.form['pin']
			dist=request.form['dist']

			q="INSERT INTO `vendor`(`company_name`,`email`,`phone`,`house`,`place`,`pincode`,`district`,v_status)VALUES('%s','%s','%s','%s','%s','%s','%s','active')"%(company_name,email,phone,hname,place,pin,dist)
			insert(q)

			flash("ADDED SUCCESSFULLY")

			return redirect(url_for('staff.staff_manage_vendor'))

		q1="SELECT * from vendor"
		print(q1)
		res=select(q1)
		print(res)
		data['vendor']=res

		if 'action' in request.args:
			action=request.args['action']
			ids=request.args['ids']
		else:
			action=None

		if action=='update':
			q="SELECT *  FROM `vendor`  WHERE `vendor_id`='%s'"%(ids)
			res=select(q)
			data['upvendor']=res

		if 'submits' in request.form:

			
			company_name=request.form['company_name']
			email=request.form['email']
			phone=request.form['phone']
			hname=request.form['hname']
			place=request.form['place']
			pin=request.form['pin']
			dist=request.form['dist']

			qry="UPDATE `vendor` SET `company_name`='%s',`email`='%s',`phone`='%s',`house`='%s',`place`='%s',`pincode`='%s',`district`='%s' WHERE `vendor_id`='%s'"%(company_name,email,phone,hname,place,pin,dist,ids)
			update(qry)

			flash("UPDATED SUCCESSFULLY")

			return redirect(url_for('staff.staff_manage_vendor'))

		if action=='inactive':
			q="update vendor set v_status='inactive'  WHERE `vendor_id`='%s'"%(ids)
			update(q)
			flash("Inactivated")
			return redirect(url_for('staff.staff_manage_vendor'))
		if action=='active':
			q="update vendor set v_status='active'  WHERE `vendor_id`='%s'"%(ids)
			update(q)
			flash("Activated")
			return redirect(url_for('staff.staff_manage_vendor'))
			

		return render_template('staff_manage_vendor.html',data=data)

	else:

		return redirect(url_for('public.public_login'))

@staff.route('/staff_view_booking')
def staff_view_booking():

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
			return redirect(url_for('staff.staff_view_booking'))

		if action=='deliver':
			q="update booking set `status`='delivered' WHERE `booking_id`='%s'"%(ids)
			update(q)
			flash('Delivered')
			return redirect(url_for('staff.staff_view_booking'))

		q="SELECT *,CONCAT(`first_name`,' ',`last_name`) AS customer_name FROM `booking` INNER JOIN `customer` USING (`customer_id`)"
		res=select(q)
		data['bookings']=res

		return render_template('staff_view_booking.html',data=data)

	else:

		return redirect(url_for('public.public_login'))

@staff.route('/staff_view_payment')
def staff_view_payment():

	if session.get('username'):

		data={}

		q="SELECT *,CONCAT(`first_name`,' ',`last_name`) AS customer_name,payment.`date` AS pdate FROM `payment` INNER JOIN `booking` USING (`booking_id`) inner join customer using(customer_id)"
		res=select(q)
		data['payment']=res

		return render_template('staff_view_payment.html',data=data)

	else:

		return redirect(url_for('public.public_login'))

@staff.route('/staff_view_message',methods=['get','post'])
def staff_view_message():

	if session.get('username'):

		data={}

		q="SELECT *,CONCAT(`first_name`,' ',`last_name`) AS customer_name FROM `message` INNER JOIN `customer` USING(`customer_id`) "
		res=select(q)
		data['msg']=res
		j=0

		for i in range(1,len(res)+1):
			if 'submit'+str(i) in request.form:
				reply=request.form['reply'+str(i)]
				q="UPDATE `message` SET `reply`='%s' WHERE `message_id`='%s'"%(reply,res[j]['message_id'])
				update(q)
				flash('reply sent')
				return redirect(url_for('staff.staff_view_message'))
			j=j+1

		return render_template('staff_view_message.html',data=data)

	else:

		return redirect(url_for('public.public_login'))





@staff.route('/staff_manage_types')
def staff_manage_types():
	if session.get('username'):
		data={}
		q="SELECT * FROM `subcategory` "
		data['subcategory']=select(q)
		return render_template('staff_manage_types.html',data=data)
	else:
		return redirect(url_for('public.public_login'))

@staff.route('/staffmanagepurchase',methods=['get','post'])
def staffmanagepurchase():
	data={}
	vid=request.args['vid']
	data['vid']=vid
	item_id=request.args['item_id']

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
			q="update items set quantity=quantity+'%s',amount='%s',cost_price='%s' where item_id='%s'"%(quantity,sp,amount,item_id)
			update(q)

			return redirect(url_for('staff.staffmanagepurchase',vid=vid,item_id=item_id))


		return render_template("staffmanagepurchase.html",data=data)
	else:
		return redirect(url_for("public.login"))		

@staff.route('/staff_view_category')
def staff_view_category():
	data={}
	q="SELECT * FROM `category` where c_status='active'"
	res=select(q)
	data['cat']=res
	return render_template('staff_view_category.html',data=data)

@staff.route('/staff_select_subcategory')
def staff_select_subcategory():
	ids=request.args['ids']
	data={}
	q="SELECT * FROM `subcategory` inner join category using(category_id) where category_id='%s'"%(ids)
	res=select(q)
	data['subcat']=res
	return render_template('staff_select_subcategory.html',data=data)

@staff.route('/staff_select_breed')
def staff_select_breed():
	id=request.args['id']
	data={}
	q="SELECT * FROM `breeds` inner join subcategory using(subcategory_id) where subcategory_id='%s'"%(id)
	res=select(q)
	data['breed']=res
	return render_template('staff_select_breed.html',data=data)

@staff.route('/staff_select_vendor')
def staff_select_vendor():
	id=request.args['id']
	data={}
	data['sid']=id
	
	q="select * from vendor"
	res=select(q)
	data['vendor']=res
	return render_template('staff_view_vendor.html',data=data,sid=id)

@staff.route('/staff_select_vendor1')
def staff_select_vendor1():
	data={}
	q="select * from vendor"
	res=select(q)
	data['vendor']=res
	return render_template('staff_view_vendor.html',data=data)

@staff.route('/staff_select_item')
def staff_select_item():
	data={}
	vid=request.args['vid']
	data['vid']=vid
	
	q="select * from items"
	res=select(q)
	data['items']=res
	return render_template('staff_select_item.html',data=data)


@staff.route('/profile',methods=['get','post'])
def profile():
	data={}
	sid=session['sid']
	q="select * from staff where staff_id='%s'"%(sid)
	res=select(q)
	data['staff']=res
	if 'action' in request.args:
			action=request.args['action']
			ids=request.args['ids']
			
	else:
		action=None

	if action=='edit':
		q="SELECT * FROM `staff` WHERE staff_id='%s'"%(sid)
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
				
			q="UPDATE `staff` SET username='%s',`first_name`='%s',`last_name`='%s',`phone`='%s',`email`='%s',`house`='%s',`city`='%s',`state`='%s',`pin`='%s' WHERE `staff_id`='%s'"%(email,fname,lname,phone,email,hname,city,state,pin,sid)
			update(q)
			q1="UPDATE `login` SET `username`='%s' WHERE username='%s'"%(email,ids)
			update(q1)

			flash("UPDATED SUCCESSFULLY")
			return redirect(url_for('staff.profile'))
	return render_template('staff_edit_profile.html',data=data)	

@staff.route('/staff_view_cancelled_order')
def staff_view_cancelled_order():
	data={}
	q="SELECT * FROM `booking` inner join customer using(customer_id) where status='cancel'"
	res=select(q)
	data['bookings']=res
	return render_template('staff_view_cancelled_order.html',data=data)

@staff.route('/staff_view_order_report',methods=['get','post'])
def staff_view_order_report():

	if session.get('username'):

		data={}

		if 'submit' in request.form:
			fdate=request.form['fdate']
			tdate=request.form['tdate']
			q="SELECT *,CONCAT(`first_name`,' ',`last_name`) AS customer_name FROM `booking` INNER JOIN `customer` USING (`customer_id`) WHERE `booking`.`date` BETWEEN '%s' AND '%s'"%(fdate,tdate)
			res=select(q)
			session['q']=q
			data['bookings']=res
		return render_template('staff_view_order_report.html',data=data)

	else:

		return redirect(url_for('public.public_login'))	

@staff.route('/staff_order_print',methods=['get','post'])
def staff_order_print():
	data={}
	res=select(session['q'])
	data['bookings']=res
	return render_template('staff_order_print.html',data=data)		

@staff.route('/staff_view_purchase_report',methods=['get','post'])
def staff_view_purchase_report():

	if session.get('username'):

		data={}

		if 'submit' in request.form:
			fdate=request.form['fdate']
			tdate=request.form['tdate']
			q="SELECT *,`purchasemaster`.`amount` AS pamount,`purchasechild`.`amount` AS camount FROM `purchasemaster` INNER JOIN `purchasechild` USING(pmaster_id) INNER JOIN `vendor` USING(vendor_id) INNER JOIN `items` USING(item_id) WHERE `purchasemaster`.`date` BETWEEN '%s' AND '%s'"%(fdate,tdate)
			res=select(q)
			session['q']=q
			
			data['purchase']=res
		
		return render_template('staff_view_purchase_report.html',data=data)

	else:

		return redirect(url_for('public.public_login'))	

@staff.route('/staff_purchase_print',methods=['get','post'])
def staff_purchase_print():
	data={}
	res=select(session['q'])
	data['purchase']=res
	return render_template('staff_purchase_print.html',data=data)		

@staff.route('/staff_view_payment_report',methods=['get','post'])
def staff_view_payment_report():

	if session.get('username'):

		data={}

		if 'submit' in request.form:
			fdate=request.form['fdate']
			tdate=request.form['tdate']
			q="SELECT * FROM `payment` INNER JOIN `booking` USING (`booking_id`) INNER JOIN `customer` USING(`customer_id`) WHERE `payment`.`date` BETWEEN '%s' AND '%s'"%(fdate,tdate)
			res=select(q)
			session['q']=q
			data['payment']=res
		
		return render_template('staff_view_payment_report.html',data=data)

	else:

		return redirect(url_for('public.public_login'))

@staff.route('/staff_payment_print',methods=['get','post'])
def staff_payment_print():
	data={}
	res=select(session['q'])
	data['payment']=res
	return render_template('staff_payment_print.html',data=data)		

@staff.route('/staff_view_item_report',methods=['get','post'])
def staff_view_item_report():

	if session.get('username'):

		data={}
		q="SELECT * FROM items INNER JOIN `breeds` ON `breed_id`=`items`.`selected_id`"
		res=select(q)
		data['item']=res
		session['q']=q
		return render_template('staff_view_item_report.html',data=data)
	else:
		return redirect(url_for('public.public_login'))	

@staff.route('/staff_print')
def staff_print():
	data={}
	q="SELECT * FROM `items` INNER JOIN `breeds` ON `breeds`.`breed_id`=`items`.`selected_id`"
	res=select(q)
	data['item']=res
	return render_template('staff_print.html',data=data)				


@staff.route('/staff_view_customer')
def staff_view_customer():

	if session.get('username'):

		data={}

		q="SELECT * FROM `customer` ORDER BY first_name ASC"
		res=select(q)
		session['q']=q
		data['customer']=res
		
		return render_template('staff_view_customer.html',data=data)

	else:

		return redirect(url_for('public.public_login'))	

@staff.route('/staff_customer_print',methods=['get','post'])
def staff_customer_print():
	data={}
	res=select(session['q'])
	data['customer']=res
	return render_template('staff_customer_print.html',data=data)