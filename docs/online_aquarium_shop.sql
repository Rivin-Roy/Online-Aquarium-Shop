/*
SQLyog Ultimate v11.11 (64 bit)
MySQL - 5.7.26 : Database - online_aquarium_shop
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
  `total` varchar(200) DEFAULT NULL,
  `date` varchar(200) DEFAULT NULL,
  `status` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`booking_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `booking` */

insert  into `booking`(`booking_id`,`customer_id`,`total`,`date`,`status`) values (1,1,'130','2021-04-05','paid'),(2,1,'340','2021-04-06','pending');

/*Table structure for table `booking_detail` */

DROP TABLE IF EXISTS `booking_detail`;

CREATE TABLE `booking_detail` (
  `bdetail_id` int(11) NOT NULL AUTO_INCREMENT,
  `booking_id` int(11) DEFAULT NULL,
  `item_id` int(11) DEFAULT NULL,
  `quantity` varchar(200) DEFAULT NULL,
  `amount` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`bdetail_id`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `booking_detail` */

insert  into `booking_detail`(`bdetail_id`,`booking_id`,`item_id`,`quantity`,`amount`) values (1,1,1,'11','110'),(2,1,2,'2','20'),(3,2,1,'29','290'),(4,2,3,'5','50');

/*Table structure for table `breeds` */

DROP TABLE IF EXISTS `breeds`;

CREATE TABLE `breeds` (
  `breed_id` int(11) NOT NULL AUTO_INCREMENT,
  `subcategory_id` varchar(200) DEFAULT NULL,
  `breed` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`breed_id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `breeds` */

insert  into `breeds`(`breed_id`,`subcategory_id`,`breed`) values (1,'1','Tr'),(2,'select','fghjkl'),(3,'Select','dfghjk');

/*Table structure for table `category` */

DROP TABLE IF EXISTS `category`;

CREATE TABLE `category` (
  `category_id` int(11) NOT NULL AUTO_INCREMENT,
  `category` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`category_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `category` */

insert  into `category`(`category_id`,`category`) values (1,'Cat one s');

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
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `customer` */

insert  into `customer`(`customer_id`,`username`,`first_name`,`last_name`,`phone`,`house`,`place`,`district`,`pincode`,`email`) values (1,'ann','staff','new','9074802591','sdfghj ghjk','chalakudy','Thrissur','688534','annregina@gmail.com');

/*Table structure for table `feedback` */

DROP TABLE IF EXISTS `feedback`;

CREATE TABLE `feedback` (
  `feedback_id` int(11) NOT NULL AUTO_INCREMENT,
  `customer_id` int(11) DEFAULT NULL,
  `feedback` varchar(200) DEFAULT NULL,
  `date` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`feedback_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `feedback` */

/*Table structure for table `items` */

DROP TABLE IF EXISTS `items`;

CREATE TABLE `items` (
  `item_id` int(11) NOT NULL AUTO_INCREMENT,
  `selected_id` int(11) DEFAULT NULL,
  `type` varchar(200) DEFAULT NULL,
  `vendor_id` varchar(200) DEFAULT NULL,
  `product` varchar(200) DEFAULT NULL,
  `quantity` varchar(200) DEFAULT NULL,
  `amount` varchar(200) DEFAULT NULL,
  `image` varchar(500) DEFAULT NULL,
  PRIMARY KEY (`item_id`)
) ENGINE=MyISAM AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;

/*Data for the table `items` */

insert  into `items`(`item_id`,`selected_id`,`type`,`vendor_id`,`product`,`quantity`,`amount`,`image`) values (1,1,'equipments','1','bb','960','10','static/e3295125-62e5-40ee-8814-58843508d4c3Photo-Editing-Apps-For-Vintage-Camera-Effect.jpg'),(2,1,'equipments','1','dfghnjkl','8','10','static/03217478-97ee-4efe-97da-33a41af2cfc6Darwin-lo-res-1.png'),(3,1,'fish','1','bb','995','10','static/f608df87-635c-43ee-b559-f382b4ef3afedark-vintage-bedroom-paneling.jpg'),(4,1,'fish','1','dfghnjkl','1000','40','static/9673fbf3-50e8-4d22-8bf9-16ccabe868605.png'),(5,1,'equipments','1','dfghnjkl','10','100','static/19421c8e-3161-4d32-82c1-6b9ebc7199a8Photo-Editing-Apps-For-Vintage-Camera-Effect.jpg'),(6,1,'equipments','1','bb','1000','20','static/ce0ddcf0-aa1c-4a16-9e3d-57c8606938c0Photo-Editing-Apps-For-Vintage-Camera-Effect.jpg'),(7,1,'equipments','1','dfghnjkl','1000','20','static/657b25c6-290e-454a-a5a4-a4602becbf62dark-vintage-bedroom-paneling.jpg'),(8,1,'equipments','1','bb','1000','80','static/3dbead24-744d-469e-9584-a6c560c6d196LOsyhJ.jpg'),(9,2,'fish','1','fiiiiiiii','19','10','static/1d1d2ce7-1ef2-4f80-af83-c90ffc9672edAlternative.gif');

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `username` varchar(200) NOT NULL,
  `password` varchar(200) DEFAULT NULL,
  `usertype` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`username`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`username`,`password`,`usertype`) values ('admin','admin','admin'),('ann','ann','customer'),('treata','treata','staff');

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
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `message` */

insert  into `message`(`message_id`,`customer_id`,`staff_id`,`message`,`reply`,`date`) values (1,1,0,'Hai','Reply','2021-04-05');

/*Table structure for table `payment` */

DROP TABLE IF EXISTS `payment`;

CREATE TABLE `payment` (
  `payment_id` int(11) NOT NULL AUTO_INCREMENT,
  `booking_id` int(11) DEFAULT NULL,
  `amount` varchar(200) DEFAULT NULL,
  `date` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`payment_id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `payment` */

insert  into `payment`(`payment_id`,`booking_id`,`amount`,`date`) values (1,1,'130','2021-04-05'),(2,1,'130','2021-04-05'),(3,1,'130','2021-04-06');

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
  PRIMARY KEY (`staff_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `staff` */

insert  into `staff`(`staff_id`,`username`,`first_name`,`last_name`,`phone`,`email`,`house`,`city`,`state`,`pin`,`qualification`,`doj`,`designation`) values (1,'treata','Staff','One','7012758728','anntreataregina@gmail.com','sdfghj ghjk','dfghj','rthyj','688534','Ph.D','2021-04-05','lecturer');

/*Table structure for table `subcategory` */

DROP TABLE IF EXISTS `subcategory`;

CREATE TABLE `subcategory` (
  `subcategory_id` int(11) NOT NULL AUTO_INCREMENT,
  `category_id` varchar(200) DEFAULT NULL,
  `subcategory` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`subcategory_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `subcategory` */

insert  into `subcategory`(`subcategory_id`,`category_id`,`subcategory`) values (1,'1','Equipments');

/*Table structure for table `vendor` */

DROP TABLE IF EXISTS `vendor`;

CREATE TABLE `vendor` (
  `vendor_id` int(11) NOT NULL AUTO_INCREMENT,
  `staff_id` int(11) DEFAULT NULL,
  `first_name` varchar(200) DEFAULT NULL,
  `last_name` varchar(200) DEFAULT NULL,
  `email` varchar(200) DEFAULT NULL,
  `phone` varchar(200) DEFAULT NULL,
  `house` varchar(200) DEFAULT NULL,
  `place` varchar(200) DEFAULT NULL,
  `pincode` varchar(200) DEFAULT NULL,
  `district` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`vendor_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `vendor` */

insert  into `vendor`(`vendor_id`,`staff_id`,`first_name`,`last_name`,`email`,`phone`,`house`,`place`,`pincode`,`district`) values (1,1,'vendor','One','annregina@gmail.com','7012758728','sdfghj ghjk','chalakudy','688534','jjjj');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
