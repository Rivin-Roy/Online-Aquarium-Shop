from flask import *
from database import *

customer=Blueprint('customer',__name__)

@customer.route('/customer_home')
def customer_home():
	if session.get('username'):
		return render_template('customer_home.html')
	else:
		return redirect(url_for('public.public_login'))

@customer.route('/customer_view_fish',methods=['get','post'])
def customer_view_fish():
	if session.get('username'):
		data={}
		
		if 'search' in request.form:
			srch=request.form['srch']
			sr="%"+srch+"%"
			q="select * from `items` where `product` like '%s'"%(sr)
			print(q)
			res=select(q)
			data['fish']=res
		else:
			q="SELECT * FROM items INNER JOIN `breeds` ON `breeds`.`breed_id`=`items`.`selected_id`  WHERE `type`='fish' and cost_price!=0"
			res=select(q)
			data['fish']=res	
		return render_template('customer_view_fish.html',data=data)
	else:
		return redirect(url_for('public.public_login'))

@customer.route('/customer_view_fish_details')
def customer_view_fish_details():
	if session.get('username'):
		data={}
		ids=request.args['ids']

		q="SELECT * FROM items INNER JOIN `breeds` ON `breed_id`=`items`.`selected_id` WHERE `type`='fish' and item_id='%s'"%(ids)
		res=select(q)
		data['fish']=res
		return render_template('customer_view_fish_details.html',data=data)
	else:
		return redirect(url_for('public.public_login'))

@customer.route('/customer_view_equipments')
def customer_view_equipments():
	if session.get('username'):
		data={}

		q="SELECT * FROM items INNER JOIN `subcategory` ON `subcategory_id`=`items`.`selected_id`  WHERE `type`='equipments' and amount!='0' "
		res=select(q)
		data['equip']=res

		return render_template('customer_view_equipments.html',data=data)
	else:
		return redirect(url_for('public.public_login'))

@customer.route('/customer_view_equipment_details')
def customer_view_equipment_details():
	if session.get('username'):
		data={}

		ids=request.args['ids']

		q="SELECT * FROM items INNER JOIN `subcategory` ON `subcategory_id`=`items`.`selected_id`  WHERE `type`='equipments' and item_id='%s'"%(ids)
		res=select(q)
		data['equip']=res

		return render_template('customer_view_equipment_details.html',data=data)
	else:
		return redirect(url_for('public.public_login'))

@customer.route('/customer_make_payment',methods=['get','post'])
def customer_make_payment():
	if session.get('username'):
		data={}
		id=request.args['id']
		data['id']=id
		if 'pay' in request.form:
			q="SELECT * FROM booking INNER JOIN booking_detail using(booking_id)  where booking_id='%s'"%(id)
			res=select(q)
			q="update booking set status='paid' where booking_id='%s'"%(id)
			update(q)
			
			for row in res:
				q="update items set quantity=quantity-'%s' where item_id='%s'" %(row['quantity'],row['item_id'])
				update(q)

			w="INSERT INTO payment(`booking_id`,`amount`,`date`) VALUES('%s','%s',CURDATE())"%(id,res[0]['total'])
			insert(w)
			flash("Payment Successfull")
			return redirect(url_for("customer.customer_home"))
		else:
			q="select * from booking where booking_id='%s'"%(id)
			data['view']=select(q)
		return render_template('customer_make_payment.html',data=data)
	else:
		return redirect(url_for('public.public_login'))

@customer.route('/customer_make_another_pay',methods=['get','post'])
def customer_make_another_pay():
	if session.get('username'):
		data={}
		id=request.args['id']
		if 'pay' in request.form:
			q="update booking set status='paid' where booking_id='%s'"%(id)
			update(q)
			q="SELECT * FROM booking INNER JOIN booking_detail USING(booking_id) where customer_id='%s' and booking_id='%s'"%(session['cid'],id)
			res=select(q)
			w="INSERT INTO payment(`booking_id`,`amount`,`date`) VALUES('%s','%s',CURDATE())"%(id,res[0]['total'])
			insert(w)
			flash("Payment Successfull")
			return redirect(url_for("customer.customer_home"))
		else:
			q="select * from booking where booking_id='%s'"%(id)
			data['view']=select(q)
		return render_template('customer_make_payment.html',data=data)
	else:
		return redirect(url_for('public.public_login'))		

@customer.route('/customer_view_orders')
def customer_view_orders():
	if session.get('username'):
		data={}

		q="SELECT * FROM `booking` where customer_id='%s' and status='pending' "%(session['cid'])
		print(q)
		res=select(q)
		if res:
			data['orders']=res
		else:
			data['val']="ss"

		return render_template('customer_view_orders.html',data=data)
	else:
		return redirect(url_for('public.public_login'))


# @customer.route('/customer_view_orders_history')
# def customer_view_orders_history():
# 	if session.get('username'):
# 		data={}

# 		q="SELECT *,booking_detail.quantity as bq,booking_detail.amount as ba FROM `booking_detail` INNER JOIN `booking` USING(`booking_id`) where customer_id='%s' ORDER BY DATE DESC "%(session['cid'])
# 		print(q)
# 		res=select(q)

# 		data['odetails']=res

# 		return render_template('customer_view_orders_history.html',data=data)
# 	else:
# 		return redirect(url_for('public.public_login'))
@customer.route('/customer_view_history')
def customer_view_history():
	if session.get('username'):
		data={}
		q="select * from booking where customer_id='%s'"%(session['cid'])
		res=select(q)
		data['book']=res
		# if 'action' in request.args:
		# 	bid=request.args['bid']
		# else:
		# 	action=None
		# if action=="cancel":
		# 	q=""		
		return render_template('customer_view_orders_history.html',data=data)
	else:
		return redirect(url_for('public.public_login'))
@customer.route('/customer_view_history_details')
def customer_view_history_details():
	if session.get('username'):
		data={}
		q="select * from booking_detail inner join booking using(booking_id) inner join items using(item_id) where customer_id='%s'"%(session['cid'])
		res=select(q)
		data['book']=res
		return render_template('customer_view_history_details.html',data=data)
	else:
		return redirect(url_for('public.public_login'))			
@customer.route('/customer_view_orderdetails',methods=['get','post'])
def customer_view_orderdetails():
	if session.get('username'):
		data={}
		ids=request.args['ids']
		data['ids']=ids
		q="SELECT *,`booking_detail`.quantity as bq,booking_detail.amount as ba FROM `booking_detail` INNER JOIN `booking` USING(`booking_id`) INNER JOIN `items` USING(`item_id`) where booking_id='%s'"%(ids)		
		print(q)
		res=select(q)
		data['odetails']=res
		if 'action' in request.args:
			action=request.args['action']
			bid=request.args['bid']
			bd_id=request.args['bd_id']
			amount=request.args['amount']
			i_id=request.args['i_id']
			quantity=request.args['q']
		else:
			action=None

		if 'actions' in request.args:
			actions=request.args['actions']
			id=request.args['id']
		else:
			actions=None

		if actions=="makepayment":
			
			flag="0"
			q="SELECT * FROM booking INNER JOIN booking_detail using(booking_id)  where booking_id='%s'"%(id)
			res=select(q)
			print(res)
			for row in res:
				q1="select * from items where item_id='%s'" %(row['item_id'])
				print(q1)
				res11=select(q1)
				if res11:
				
					if int(res11[0]['quantity'])< int(row['quantity']):
						flag="1"
			if flag=="1": 
				flash("Out of Stock")
				return redirect(url_for("customer.customer_home"))
			else:
				return redirect(url_for("customer.customer_make_payment",id=id))
			
		if action=="cancel":
			q="delete from booking_detail where bdetail_id='%s'"%(bd_id)
			delete(q)
			q="select * from booking_detail where bdetail_id='%s'"%(bd_id)
			res=select(q)
			if not res:
				z="update booking set status='cancel',total=total-'%s'  where booking_id='%s'"%(amount,bid)
				update(z)
			else:
				z="update booking set total=total-'%s' where booking_id='%s'"%(amount,bid)
				update(z)
			x="update items set quantity=quantity+'%s' where item_id='%s'"%(quantity,i_id)
			update(x)
			return redirect(url_for('customer.customer_view_orderdetails',ids=ids))
		return render_template('customer_view_orderdetails.html',data=data)
	else:
		return redirect(url_for('public.public_login'))

@customer.route('/customer_send_message',methods=['get','post'])
def customer_send_message():
	if session.get('username'):
		data={}
		cid=session['cid']

		if 'submit' in request.form:
			msg=request.form['msg']

			q=" INSERT INTO `message`(`customer_id`,`staff_id`,`message`,`reply`,`date`) VALUES('%s','0','%s','pending',CURDATE())"%(cid,msg)
			insert(q)
			return redirect(url_for('customer.customer_send_message'))

		q="SELECT * FROM `message`"
		res=select(q)
		data['msg']=res

		return render_template('customer_send_message.html',data=data)
	else:
		return redirect(url_for('public.public_login'))


@customer.route('/customer_send_feedback',methods=['get','post'])
def customer_send_feedback():
	if session.get('username'):
		data={}
		cid=session['cid']

		if 'submit' in request.form:
			feed=request.form['feed']

			q=" INSERT INTO `feedback`(`customer_id`,`feedback`,`date`) VALUES('%s','%s',CURDATE())"%(cid,feed)
			insert(q)
			return redirect(url_for('customer.customer_send_feedback'))

		q="SELECT * FROM `feedback`"
		res=select(q)
		data['fbk']=res

		return render_template('customer_send_feedback.html',data=data)
	else:
		return redirect(url_for('public.public_login'))

@customer.route('/customer_view_itemdetails',methods=['get','post'])
def customer_view_itemdetails():
	if session.get('username'):
		data={}
		cid=session['cid']

		q=" SELECT * FROM `items` INNER JOIN `breeds` ON `breeds`.`breed_id`=`items`.`selected_id`"
		res=select(q)
		data['idet']=res

		if 'submit' in request.form:
			feed=request.form['feed']

			q=" INSERT INTO `feedback`(`customer_id`,`feedback`,`date`) VALUES('%s','%s',CURDATE())"%(cid,feed)
			insert(q)
			return redirect(url_for('customer.customer_send_feedback'))

		return render_template('customer_view_itemdetails.html',data=data)
	else:
		return redirect(url_for('public.public_login'))

@customer.route('/customer_add_to_cart',methods=['get','post'])
def customer_add_to_cart():
	if session.get('username'):
		data={}
		pid=request.args['id']

		if 'submit' in request.form:
			oq=request.form['order_quantity']
			a=request.form['amount']

			q="select * from booking where customer_id='%s' and status='pending'" %(session['cid'])
			res=select(q)
			if res:
				id=res[0]['booking_id']
			else:
				q="INSERT INTO booking (`customer_id`,`date`,`total`,`status`) VALUES('%s',curdate(),'0','pending')" %(session['cid'])
				id=insert(q)
				
			q="select * from booking_detail where booking_id='%s' and item_id='%s'"%(id,pid)
			res=select(q)
			if res:
				q="update booking_detail set quantity=quantity+'%s',amount=amount+'%s' where booking_id='%s' and item_id='%s'"%(oq,a,id,pid)
				update(q)
				q="update items set quantity=quantity-'%s' where item_id='%s'"%(oq,pid)
				update(q)
			else:
				q1="INSERT INTO `booking_detail` (`booking_id`,`item_id`,`quantity`,`amount`) VALUES('%s','%s','%s','%s')" %(id,pid,oq,a)
				insert(q1)
				print(q1)
			q2="update booking set total=total+'%s' where booking_id='%s' and status='pending'" %(a,id)
			update(q2)
			print(q2)
			
			flash("Added to cart")
			return redirect(url_for("customer.customer_view_orderdetails",ids=id))
		q="select * from items where item_id='%s'" %(pid)
		data['addtocarts']=select(q)
		return render_template('customer_add_to_cart.html',data=data)
	else:
		return redirect(url_for('public.public_login'))

@customer.route('/customer_edit_profile',methods=['get','post'])
def customer_edit_profile():
	if session.get('username'):
		data={}
		q="select * from customer where customer_id='%s'"%(session['cid'])
		res=select(q)
		data['user']=res
		if 'action' in request.args:
			action=request.args['action']
		else:
			action=None
		if action=="edit":
			q="select * from customer where customer_id='%s'"%(session['cid'])
			res=select(q)
			data['cust_updates']=res
			if 'submit' in request.form:
				fname=request.form['fname']
				lname=request.form['lname']
				phone=request.form['phone']
				hname=request.form['hname']
				place=request.form['place']
				district=request.form['district']
				pin=request.form['pin']
				email=request.form['email']
				q="update customer set first_name='%s',last_name='%s',phone='%s',house='%s',place='%s',district='%s',pincode='%s',email='%s' where customer_id='%s'"%(fname,lname,phone,hname,place,district,pin,email,session['cid'])		
				update(q)
				return redirect(url_for('customer.customer_edit_profile'))
		return render_template('customer_edit_profile.html',data=data)
	else:
		return redirect(url_for('public.public_login'))

@customer.route('/user_clear')
def user_clear():
	if session.get('username'):
		data={}
		
		id=request.args['id']
		data['id']=id
		q="update booking set status='cancel' where booking_id='%s'"%(id)
		update(q)
		z="select item_id,quantity from booking inner join booking_detail using(booking_id) where booking_id='%s'"%(id)
		res1=select(z)
		# it=res1[0]['item_id']
		# qu=res1[0]['quantity']
		# x="update items set quantity=quantity+'%s' where item_id='%s'"%(qu,it)
		# update(x)
		flash("Order cancelled and will be refunded within 3 days")
		return redirect(url_for('customer.customer_home',id=id))
	else:
		return redirect(url_for('public.public_login'))	

@customer.route('/customer_view_cancelled',methods=['get','post'])
def customer_view_cancelled():
	cid=session['cid']
	data={}
	q="SELECT * FROM `booking` inner join customer using(customer_id) inner join booking_detail using(booking_id) where booking.status='cancel' and customer_id='%s'"%(cid)
	print(q)
	res=select(q)

	data['bookings']=res
	iid=res[0]['item_id']
	data['iid']=iid
	return render_template('customer_view_cancelled.html',data=data)






