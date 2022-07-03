/*
SQLyog Ultimate v11.11 (64 bit)
MySQL - 5.5.5-10.4.10-MariaDB : Database - online_aquarium_shop
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`online_aquarium_shop` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `online_aquarium_shop`;

/*Table structure for table `booking` */

DROP TABLE IF EXISTS `booking`;

CREATE TABLE `booking` (
  `booking_id` int(11) NOT NULL AUTO_INCREMENT,
  `customer_id` int(11) DEFAULT NULL,
  `total` decimal(10,0) DEFAULT NULL,
  `date` varchar(200) DEFAULT NULL,
  `status` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`booking_id`)
) ENGINE=MyISAM AUTO_INCREMENT=23 DEFAULT CHARSET=latin1;

/*Data for the table `booking` */

insert  into `booking`(`booking_id`,`customer_id`,`total`,`date`,`status`) values (22,2,400,'2022-04-06','pending'),(21,2,400,'2022-04-06','cancel'),(20,2,2800,'2022-04-05','cancel'),(19,2,2800,'2022-04-05','cancel');

/*Table structure for table `booking_detail` */

DROP TABLE IF EXISTS `booking_detail`;

CREATE TABLE `booking_detail` (
  `bdetail_id` int(11) NOT NULL AUTO_INCREMENT,
  `booking_id` int(11) DEFAULT NULL,
  `item_id` int(11) DEFAULT NULL,
  `quantity` decimal(10,0) DEFAULT NULL,
  `amount` decimal(10,0) DEFAULT NULL,
  PRIMARY KEY (`bdetail_id`)
) ENGINE=MyISAM AUTO_INCREMENT=61 DEFAULT CHARSET=latin1;

/*Data for the table `booking_detail` */

insert  into `booking_detail`(`bdetail_id`,`booking_id`,`item_id`,`quantity`,`amount`) values (60,22,37,2,400),(59,21,37,2,400),(57,20,36,2,2800),(55,19,36,2,1200),(56,19,37,2,400),(51,18,36,2,1200);

/*Table structure for table `breeds` */

DROP TABLE IF EXISTS `breeds`;

CREATE TABLE `breeds` (
  `breed_id` int(11) NOT NULL AUTO_INCREMENT,
  `subcategory_id` varchar(200) DEFAULT NULL,
  `breed` varchar(200) DEFAULT NULL,
  `b_status` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`breed_id`)
) ENGINE=MyISAM AUTO_INCREMENT=12 DEFAULT CHARSET=latin1;

/*Data for the table `breeds` */

insert  into `breeds`(`breed_id`,`subcategory_id`,`breed`,`b_status`) values (9,'6','vbnbvvbn',NULL),(8,'8','xxxx','active'),(7,'7','asd','active'),(10,'6','w','active'),(11,'11','fffffff',NULL);

/*Table structure for table `category` */

DROP TABLE IF EXISTS `category`;

CREATE TABLE `category` (
  `category_id` int(11) NOT NULL AUTO_INCREMENT,
  `category` varchar(200) DEFAULT NULL,
  `c_status` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`category_id`)
) ENGINE=MyISAM AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

/*Data for the table `category` */

insert  into `category`(`category_id`,`category`,`c_status`) values (1,'Cat one s','active'),(3,'aquarium','active'),(4,'dfghjrfgh','active'),(5,'qqq','active'),(6,'wddddd','active');

/*Table structure for table `customer` */

DROP TABLE IF EXISTS `customer`;

CREATE TABLE `customer` (
  `customer_id` int(200) NOT NULL AUTO_INCREMENT,
  `username` varchar(200) DEFAULT NULL,
  `first_name` varchar(200) DEFAULT NULL,
  `last_name` varchar(200) DEFAULT NULL,
  `phone` varchar(200) DEFAULT NULL,
  `house` varchar(200) DEFAULT NULL,
  `place` varchar(200) DEFAULT NULL,
  `district` varchar(200) DEFAULT NULL,
  `pincode` varchar(200) DEFAULT NULL,
  `email` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`customer_id`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `customer` */

insert  into `customer`(`customer_id`,`username`,`first_name`,`last_name`,`phone`,`house`,`place`,`district`,`pincode`,`email`) values (1,'ann','staff','new','9074802591','sdfghj ghjk','chalakudy','Thrissur','688534','annregina@gmail.com'),(2,'snehathannikkal@gmail.com','anns','a','9956421563','chirakkal','kottayam','kottayam','680124','snehathannikkal@gmail.com'),(3,'zs@gmail.com','aleena','s','7451236985','sdfgh','asdf','eranakulam','896231','zs@gmail.com'),(4,'as@gmail.com','ammu','a','7451236985','ffgfg','ekm','eranakulam','230231','as@gmail.com');

/*Table structure for table `feedback` */

DROP TABLE IF EXISTS `feedback`;

CREATE TABLE `feedback` (
  `feedback_id` int(11) NOT NULL AUTO_INCREMENT,
  `customer_id` int(11) DEFAULT NULL,
  `feedback` varchar(200) DEFAULT NULL,
  `date` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`feedback_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `feedback` */

insert  into `feedback`(`feedback_id`,`customer_id`,`feedback`,`date`) values (1,2,'sdfghj','2022-03-01');

/*Table structure for table `items` */

DROP TABLE IF EXISTS `items`;

CREATE TABLE `items` (
  `item_id` int(11) NOT NULL AUTO_INCREMENT,
  `selected_id` int(11) DEFAULT NULL,
  `type` varchar(200) DEFAULT NULL,
  `product` varchar(200) DEFAULT NULL,
  `brand` varchar(200) DEFAULT NULL,
  `quantity` varchar(200) DEFAULT NULL,
  `amount` varchar(200) DEFAULT NULL,
  `image` varchar(500) DEFAULT NULL,
  `description` varchar(200) DEFAULT NULL,
  `i_status` varchar(200) DEFAULT NULL,
  `cost_price` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`item_id`)
) ENGINE=MyISAM AUTO_INCREMENT=39 DEFAULT CHARSET=latin1;

/*Data for the table `items` */

insert  into `items`(`item_id`,`selected_id`,`type`,`product`,`brand`,`quantity`,`amount`,`image`,`description`,`i_status`,`cost_price`) values (36,8,'fish','product',NULL,'7','2200','static/36c3a4a6-7b27-42bb-a85d-644843d134ca11.PNG','uyfuyghghhjh','active','2000'),(37,9,'fish','fhjj','bfsssss','8','200','static/18afe214-faa9-4136-84b3-69b4dbb88918Welcome Scan.jpg','asdsefdrgr','active','250'),(38,8,'equipments','trtrytyuuihiujh','yyyyyyy','10','100','static/3c266f49-90f2-42c9-82df-d4481e17f8b7Welcome Scan.jpg','dfyuiojhgf','active','0');

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `username` varchar(200) NOT NULL,
  `password` varchar(200) DEFAULT NULL,
  `usertype` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`username`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`username`,`password`,`usertype`) values ('admin','admin','admin'),('ann','ann','customer'),('t@mail.com','treata','staff'),('snehathannikkal@gmail.com','zzz','customer'),('zs@gmail.com','xxx','customer'),('a@gmail.com','123456789','staff'),('as@gmail.com','ammu','customer'),('alee@gmail.com','aleena','staff');

/*Table structure for table `message` */

DROP TABLE IF EXISTS `message`;

CREATE TABLE `message` (
  `message_id` int(11) NOT NULL AUTO_INCREMENT,
  `customer_id` int(11) DEFAULT NULL,
  `staff_id` int(11) DEFAULT NULL,
  `message` varchar(200) DEFAULT NULL,
  `reply` varchar(200) DEFAULT NULL,
  `date` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`message_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `message` */

insert  into `message`(`message_id`,`customer_id`,`staff_id`,`message`,`reply`,`date`) values (1,1,0,'Hai','adfdghjk','2021-04-05'),(2,2,0,'dfghj','pending','2022-03-01');

/*Table structure for table `payment` */

DROP TABLE IF EXISTS `payment`;

CREATE TABLE `payment` (
  `payment_id` int(11) NOT NULL AUTO_INCREMENT,
  `booking_id` int(11) DEFAULT NULL,
  `amount` varchar(200) DEFAULT NULL,
  `date` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`payment_id`)
) ENGINE=MyISAM AUTO_INCREMENT=14 DEFAULT CHARSET=latin1;

/*Data for the table `payment` */

insert  into `payment`(`payment_id`,`booking_id`,`amount`,`date`) values (1,1,'130','2021-04-05'),(2,2,'340','2021-04-05'),(4,3,'900','2021-04-11'),(5,4,'170','2021-04-11'),(6,4,'170','2021-04-11'),(7,8,'16000','2022-02-18'),(8,9,'2000','2022-02-24'),(9,10,'26000','2022-02-24'),(10,11,'2500','2022-03-01'),(11,12,'3200','2022-03-04'),(12,13,'800','2022-03-07'),(13,14,'400','2022-03-07');

/*Table structure for table `purchasechild` */

DROP TABLE IF EXISTS `purchasechild`;

CREATE TABLE `purchasechild` (
  `pchild_id` int(11) NOT NULL AUTO_INCREMENT,
  `pmaster_id` int(11) DEFAULT NULL,
  `item_id` int(11) DEFAULT NULL,
  `amount` varchar(100) DEFAULT NULL,
  `cost_price` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`pchild_id`)
) ENGINE=MyISAM AUTO_INCREMENT=28 DEFAULT CHARSET=latin1;

/*Data for the table `purchasechild` */

insert  into `purchasechild`(`pchild_id`,`pmaster_id`,`item_id`,`amount`,`cost_price`) values (25,5,37,'250','250'),(24,4,37,'300','300'),(23,6,36,'240','240'),(22,5,36,'200','200'),(21,5,36,'150','150'),(20,4,36,'400','400'),(19,4,36,'450','450'),(18,3,36,'400','400'),(17,3,36,'100','100'),(26,3,36,'1000','1000'),(27,3,36,'4000','4000');

/*Table structure for table `purchasemaster` */

DROP TABLE IF EXISTS `purchasemaster`;

CREATE TABLE `purchasemaster` (
  `pmaster_id` int(11) NOT NULL AUTO_INCREMENT,
  `vendor_id` int(11) DEFAULT NULL,
  `amount` varchar(100) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`pmaster_id`)
) ENGINE=MyISAM AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

/*Data for the table `purchasemaster` */

insert  into `purchasemaster`(`pmaster_id`,`vendor_id`,`amount`,`date`,`status`) values (4,2,'1150','2022-03-04','active'),(3,1,'5500','2022-03-04','pending'),(5,3,'600','2022-03-04','inactive'),(6,4,'240','2022-03-07','pending');

/*Table structure for table `staff` */

DROP TABLE IF EXISTS `staff`;

CREATE TABLE `staff` (
  `staff_id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(200) DEFAULT NULL,
  `first_name` varchar(200) DEFAULT NULL,
  `last_name` varchar(200) DEFAULT NULL,
  `phone` varchar(200) DEFAULT NULL,
  `email` varchar(200) DEFAULT NULL,
  `house` varchar(200) DEFAULT NULL,
  `city` varchar(200) DEFAULT NULL,
  `state` varchar(200) DEFAULT NULL,
  `pin` varchar(200) DEFAULT NULL,
  `qualification` varchar(200) DEFAULT NULL,
  `doj` varchar(200) DEFAULT NULL,
  `designation` varchar(200) DEFAULT NULL,
  `s_status` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`staff_id`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `staff` */

insert  into `staff`(`staff_id`,`username`,`first_name`,`last_name`,`phone`,`email`,`house`,`city`,`state`,`pin`,`qualification`,`doj`,`designation`,`s_status`) values (4,'alee@gmail.com','aleena','s','7451236985','alee@gmail.com','sdfgh','ekm','fghjkefth','896231','bca','2022-02-17','asdfgh','active'),(3,'a@gmail.com','anu','a','2563201478','a@gmail.com','fdfferr','ekm','kerala','682036','bca','2022-02-17','qswert','active');

/*Table structure for table `subcategory` */

DROP TABLE IF EXISTS `subcategory`;

CREATE TABLE `subcategory` (
  `subcategory_id` int(11) NOT NULL AUTO_INCREMENT,
  `category_id` varchar(200) DEFAULT NULL,
  `subcategory` varchar(200) DEFAULT NULL,
  `sub_status` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`subcategory_id`)
) ENGINE=MyISAM AUTO_INCREMENT=12 DEFAULT CHARSET=latin1;

/*Data for the table `subcategory` */

insert  into `subcategory`(`subcategory_id`,`category_id`,`subcategory`,`sub_status`) values (8,'1','wertyui','active'),(7,'6','aaaa','active'),(10,'5','qsubbb','active'),(6,'3','bbbb','active'),(9,'8','cccccc','active'),(11,'6','qwqqww','active');

/*Table structure for table `vendor` */

DROP TABLE IF EXISTS `vendor`;

CREATE TABLE `vendor` (
  `vendor_id` int(11) NOT NULL AUTO_INCREMENT,
  `company_name` varchar(200) DEFAULT NULL,
  `email` varchar(200) DEFAULT NULL,
  `phone` varchar(200) DEFAULT NULL,
  `house` varchar(200) DEFAULT NULL,
  `place` varchar(200) DEFAULT NULL,
  `pincode` varchar(200) DEFAULT NULL,
  `district` varchar(200) DEFAULT NULL,
  `v_status` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`vendor_id`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `vendor` */

insert  into `vendor`(`vendor_id`,`company_name`,`email`,`phone`,`house`,`place`,`pincode`,`district`,`v_status`) values (1,'comp','annregina@gmail.com','7012758728','sdfghj ghjkfrghg','chalakudy','688534','jjjj','inactive'),(2,'company1','a@gmail.com','2563201478','fdff','wertyui','682036','thrissur','active'),(3,'fech','f@gmail.com','8962365412','fhousesss','chalakudi','652301','thrissur','active'),(4,'infotech','info@gmail.com','8965412365','fghjkl','ekm','7856+32','thrissur','active');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
