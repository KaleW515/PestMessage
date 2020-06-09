-- MariaDB dump 10.17  Distrib 10.4.13-MariaDB, for Linux (x86_64)
--
-- Host: 127.0.0.1    Database: pestSituation
-- ------------------------------------------------------
-- Server version	10.4.13-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `PestApp_userinfo`
--

DROP TABLE IF EXISTS `PestApp_userinfo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `PestApp_userinfo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) COLLATE utf8mb4_unicode_ci NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) COLLATE utf8mb4_unicode_ci NOT NULL,
  `first_name` varchar(30) COLLATE utf8mb4_unicode_ci NOT NULL,
  `last_name` varchar(150) COLLATE utf8mb4_unicode_ci NOT NULL,
  `email` varchar(254) COLLATE utf8mb4_unicode_ci NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `signature` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `attachment_uuid` char(36) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  KEY `PestApp_userinfo_attachment_attachment_uuid_fk` (`attachment_uuid`),
  CONSTRAINT `PestApp_userinfo_attachment_attachment_uuid_fk` FOREIGN KEY (`attachment_uuid`) REFERENCES `attachment` (`attachment_uuid`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `PestApp_userinfo`
--

LOCK TABLES `PestApp_userinfo` WRITE;
/*!40000 ALTER TABLE `PestApp_userinfo` DISABLE KEYS */;
INSERT INTO `PestApp_userinfo` VALUES (1,'pbkdf2_sha256$180000$hrlAsQHhf9WL$nqATmg/Ru7P72lrLUr/yQO4GOpgz4EhATPkkbLYOnl8=',NULL,1,'kale','','','wk@kalew515.com',1,1,'2020-05-18 15:59:06.987115',NULL,NULL),(2,'pbkdf2_sha256$180000$u8AkKRmWdlKC$3o7J6Y0mvvc6X+l4Nv9RTtRcuOKso5aJHjnsRLutXus=','2020-06-09 17:55:21.523572',0,'kale_w','','','',0,1,'2020-05-18 16:05:36.530072','AAAA','b3d2bdc1-f226-4925-be6b-b9f3811d3420'),(3,'pbkdf2_sha256$180000$V93XqBLFe2BV$HB6fwzWuj9ga79OCordHdSw0ElheUN5PXy97NuztUGA=','2020-05-18 17:21:04.401924',0,'忧郁的小乌龟','','','',0,1,'2020-05-18 17:20:34.892168','这个人很懒,什么都没有留下',NULL);
/*!40000 ALTER TABLE `PestApp_userinfo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `PestApp_userinfo_groups`
--

DROP TABLE IF EXISTS `PestApp_userinfo_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `PestApp_userinfo_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `userinfo_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `PestApp_userinfo_groups_userinfo_id_group_id_5a8197f7_uniq` (`userinfo_id`,`group_id`),
  KEY `PestApp_userinfo_groups_group_id_002fc30f_fk_auth_group_id` (`group_id`),
  CONSTRAINT `PestApp_userinfo_gro_userinfo_id_63e2be5e_fk_PestApp_u` FOREIGN KEY (`userinfo_id`) REFERENCES `PestApp_userinfo` (`id`),
  CONSTRAINT `PestApp_userinfo_groups_group_id_002fc30f_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `PestApp_userinfo_groups`
--

LOCK TABLES `PestApp_userinfo_groups` WRITE;
/*!40000 ALTER TABLE `PestApp_userinfo_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `PestApp_userinfo_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `PestApp_userinfo_user_permissions`
--

DROP TABLE IF EXISTS `PestApp_userinfo_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `PestApp_userinfo_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `userinfo_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `PestApp_userinfo_user_pe_userinfo_id_permission_i_35f62a10_uniq` (`userinfo_id`,`permission_id`),
  KEY `PestApp_userinfo_use_permission_id_76b5ca56_fk_auth_perm` (`permission_id`),
  CONSTRAINT `PestApp_userinfo_use_permission_id_76b5ca56_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `PestApp_userinfo_use_userinfo_id_2a7f2201_fk_PestApp_u` FOREIGN KEY (`userinfo_id`) REFERENCES `PestApp_userinfo` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `PestApp_userinfo_user_permissions`
--

LOCK TABLES `PestApp_userinfo_user_permissions` WRITE;
/*!40000 ALTER TABLE `PestApp_userinfo_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `PestApp_userinfo_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `attachment`
--

DROP TABLE IF EXISTS `attachment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `attachment` (
  `attachment_name` text COLLATE utf8mb4_unicode_ci NOT NULL,
  `attachment_uuid` char(36) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`attachment_uuid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `attachment`
--

LOCK TABLES `attachment` WRITE;
/*!40000 ALTER TABLE `attachment` DISABLE KEYS */;
INSERT INTO `attachment` VALUES ('TIM图片20191212125559.jpg','b3d2bdc1-f226-4925-be6b-b9f3811d3420');
/*!40000 ALTER TABLE `attachment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=49 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add content type',4,'add_contenttype'),(14,'Can change content type',4,'change_contenttype'),(15,'Can delete content type',4,'delete_contenttype'),(16,'Can view content type',4,'view_contenttype'),(17,'Can add session',5,'add_session'),(18,'Can change session',5,'change_session'),(19,'Can delete session',5,'delete_session'),(20,'Can view session',5,'view_session'),(21,'Can add comments',6,'add_comments'),(22,'Can change comments',6,'change_comments'),(23,'Can delete comments',6,'delete_comments'),(24,'Can view comments',6,'view_comments'),(25,'Can add donation',7,'add_donation'),(26,'Can change donation',7,'change_donation'),(27,'Can delete donation',7,'delete_donation'),(28,'Can view donation',7,'view_donation'),(29,'Can add keywords',8,'add_keywords'),(30,'Can change keywords',8,'change_keywords'),(31,'Can delete keywords',8,'delete_keywords'),(32,'Can view keywords',8,'view_keywords'),(33,'Can add reply',9,'add_reply'),(34,'Can change reply',9,'change_reply'),(35,'Can delete reply',9,'delete_reply'),(36,'Can view reply',9,'view_reply'),(37,'Can add volunteer',10,'add_volunteer'),(38,'Can change volunteer',10,'change_volunteer'),(39,'Can delete volunteer',10,'delete_volunteer'),(40,'Can view volunteer',10,'view_volunteer'),(41,'Can add user',11,'add_userinfo'),(42,'Can change user',11,'change_userinfo'),(43,'Can delete user',11,'delete_userinfo'),(44,'Can view user',11,'view_userinfo'),(45,'Can add captcha store',12,'add_captchastore'),(46,'Can change captcha store',12,'change_captchastore'),(47,'Can delete captcha store',12,'delete_captchastore'),(48,'Can view captcha store',12,'view_captchastore');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `captcha_captchastore`
--

DROP TABLE IF EXISTS `captcha_captchastore`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `captcha_captchastore` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `challenge` varchar(32) COLLATE utf8mb4_unicode_ci NOT NULL,
  `response` varchar(32) COLLATE utf8mb4_unicode_ci NOT NULL,
  `hashkey` varchar(40) COLLATE utf8mb4_unicode_ci NOT NULL,
  `expiration` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `hashkey` (`hashkey`)
) ENGINE=InnoDB AUTO_INCREMENT=40 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `captcha_captchastore`
--

LOCK TABLES `captcha_captchastore` WRITE;
/*!40000 ALTER TABLE `captcha_captchastore` DISABLE KEYS */;
INSERT INTO `captcha_captchastore` VALUES (1,'FLIY','fliy','f619b19997890969f1e8cc139bbfbf24eedee7b0','2020-05-18 16:04:22.813063'),(2,'HVMZ','hvmz','78afd3d2c05710474073d0d19dfbe54d70488ed8','2020-05-18 16:04:23.063464'),(3,'GJQL','gjql','21b80c4bb89384041ac4906c497cc04f5b9a64a6','2020-05-18 16:10:36.851495'),(4,'MIIA','miia','4eb066c6ab7385d184033606a05c24cc020104dd','2020-05-18 16:27:04.359384'),(5,'ISZK','iszk','1e9342b392a999c38f9f955c6ae0d5985df695ac','2020-05-18 16:30:13.632540'),(6,'XRUV','xruv','7e704863c87e66755c9d6f49d2ba5481bebc82cb','2020-05-18 16:34:24.338378'),(7,'BRYK','bryk','b9cd61f09801991becddb96fe609131502826300','2020-05-18 16:47:31.522180'),(8,'OEQM','oeqm','33b1b03262d1f1fbf3fc5aafc87d9a37025edab0','2020-05-18 17:11:04.699579'),(9,'PBWV','pbwv','1763530e37497df059e37dd8dd9b218afdd7d41c','2020-05-18 17:24:47.881225'),(10,'BJHY','bjhy','f8b4e521f782af0f0178449d0b309cf773ee6e03','2020-05-18 17:25:35.333128'),(11,'DZHM','dzhm','9e1978d3901260d520f5e1a9b80b32248ae9e5b5','2020-05-18 17:31:20.638137'),(12,'GXXY','gxxy','0427881c68884f736fc71e7732397351529f8fd2','2020-05-18 17:50:41.549272'),(13,'RIRI','riri','3f5cfd71a84ef310564f3b392cb512841df5475d','2020-05-18 18:01:58.410131'),(14,'GVXW','gvxw','d3a4fb8d9a52afe3d36c5b1397e66b19a84a3ab5','2020-05-18 18:04:43.564011'),(15,'ZJAN','zjan','0bdf71b2efc8e5980b1bf01abf4fc25f78150f6f','2020-05-18 18:05:40.360420'),(16,'BDCD','bdcd','34409a96ba6052d6441369fe1c1979c8cd935cce','2020-05-18 18:11:30.907340'),(17,'SMHA','smha','c8f17b03cd1bc002286b8d6c6468bc20ebae8bb9','2020-05-18 18:12:33.216624'),(18,'PIMJ','pimj','ee56c51bb10f6c4d8d3c510ad0e358c6f6c78c4d','2020-05-18 18:12:33.899136'),(19,'NLJV','nljv','923ac1f4923467697f6da75ebe1cfd17955a1016','2020-05-18 18:12:35.043249'),(20,'AQJZ','aqjz','9c17743ca657db7733e4bd2c61c70d063ea95a29','2020-05-18 18:12:35.078186'),(21,'RZQE','rzqe','87a353b22f330863e1a06ba096041f6ab0606d29','2020-05-18 18:12:35.817365'),(22,'IICS','iics','2e0c8c0e7573d2247b8c2473e01d2fc00c43f5b5','2020-05-18 18:12:37.480430'),(23,'JPTQ','jptq','25554656f7d3fcded7263d50a3a8c242a2dd41ae','2020-05-19 01:40:26.439203'),(24,'EAQM','eaqm','69985c908d9e33db48767f414aeaa8599b9f8796','2020-05-19 01:46:50.439577'),(25,'JQYI','jqyi','5f4aeda674cbe26dcb1b6ad04ac21aac8e54233d','2020-05-28 06:11:46.315039'),(26,'RMIV','rmiv','d84ab136c18c160e779f68f2c036d9fbdaf96afb','2020-05-28 06:12:09.466436'),(27,'JZWK','jzwk','5db29c4f034c2dbe8ef1b480003c5607fa280ad7','2020-05-28 06:49:15.055516'),(28,'IQAK','iqak','bd7fc2aa315394f5b2d0116130b5811f7d1aad5e','2020-05-29 07:42:41.931130'),(29,'HHHD','hhhd','cfa3170608863311823ed8333df23e3060e43404','2020-05-29 07:43:02.708177'),(30,'UKFY','ukfy','ed0e85fbb1127a0b7095729d3ef84f52679c7651','2020-06-07 14:03:41.121324'),(31,'ELSW','elsw','0a6df54504095fc162d88f1de4a18375081c13d1','2020-06-07 14:08:31.026748'),(32,'DXHE','dxhe','b276873d89d5cc1928b1d80c64377b0c9f4525aa','2020-06-09 16:18:13.240638'),(33,'YRPP','yrpp','96678f15fc21c2bcbbc4a876d75a184b71e36fc2','2020-06-09 16:18:30.182870'),(34,'LJZP','ljzp','9d6ae2cc7253fe6c1cc84503880a817a57508556','2020-06-09 16:32:16.881677'),(35,'FUKC','fukc','d2d1d386ed011aac7f6ee025844fa11aa42a4fec','2020-06-09 16:32:20.133746'),(36,'ZYPT','zypt','9212c861b7bf1ad7a238f157dc18aeef17b2eb50','2020-06-09 16:32:41.808638'),(37,'ZYBF','zybf','f06b1faed938a3e67dbe67a6e8444bb0c88fbfdc','2020-06-09 16:39:10.043405'),(38,'QZFD','qzfd','b2941c63299f3ed9bbec084e2696f486a56cefa1','2020-06-09 16:59:07.440071'),(39,'XZNB','xznb','d117a3ed528273de92f2e565a109a1c3693fdf02','2020-06-09 17:59:57.136240');
/*!40000 ALTER TABLE `captcha_captchastore` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `comments`
--

DROP TABLE IF EXISTS `comments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `comments` (
  `comment_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `likeNum` int(11) DEFAULT 0,
  `disLikeNum` int(11) DEFAULT 0,
  `content` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `date` datetime NOT NULL,
  PRIMARY KEY (`comment_id`),
  KEY `comments_PestApp_userinfo_id_fk` (`user_id`),
  CONSTRAINT `comments_PestApp_userinfo_id_fk` FOREIGN KEY (`user_id`) REFERENCES `PestApp_userinfo` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=123 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `comments`
--

LOCK TABLES `comments` WRITE;
/*!40000 ALTER TABLE `comments` DISABLE KEYS */;
INSERT INTO `comments` VALUES (107,2,2,0,'重构','2020-05-19 00:00:00'),(108,2,1,0,'世间五彩','2020-05-19 00:00:00'),(109,2,1,0,'我执纯白','2020-05-19 00:00:00'),(110,2,0,0,'import crypto from \'crypto\';','2020-05-19 00:00:00'),(111,2,1,0,'四月变成了一座桥','2020-05-19 00:00:00'),(112,2,1,0,'急着让夏天来到','2020-05-19 00:00:00'),(113,2,1,0,'小区里搬进了知了 吵又闹','2020-05-19 00:00:00'),(114,2,1,0,'午后的我睡不着','2020-05-19 00:00:00'),(115,2,1,0,'你家的窗户台真高','2020-05-19 00:00:00'),(116,2,1,1,'垫着脚我够不着','2020-05-19 00:00:00'),(117,2,1,1,'碰到了楼下那只猫 没礼貌','2020-05-19 00:00:00'),(120,2,1,0,'随便写一条','2020-06-10 00:00:00'),(121,2,0,0,'安达市多','2020-06-10 01:48:41'),(122,2,0,0,'安师大撒','2020-06-10 01:49:53');
/*!40000 ALTER TABLE `comments` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `object_repr` varchar(200) COLLATE utf8mb4_unicode_ci NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_PestApp_userinfo_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_PestApp_userinfo_id` FOREIGN KEY (`user_id`) REFERENCES `PestApp_userinfo` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `model` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(12,'captcha','captchastore'),(4,'contenttypes','contenttype'),(6,'PestApp','comments'),(7,'PestApp','donation'),(8,'PestApp','keywords'),(9,'PestApp','reply'),(11,'PestApp','userinfo'),(10,'PestApp','volunteer'),(5,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `name` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2020-05-18 15:55:13.653078'),(2,'contenttypes','0002_remove_content_type_name','2020-05-18 15:55:14.428861'),(3,'auth','0001_initial','2020-05-18 15:55:15.618923'),(4,'auth','0002_alter_permission_name_max_length','2020-05-18 15:55:20.154003'),(5,'auth','0003_alter_user_email_max_length','2020-05-18 15:55:20.260958'),(6,'auth','0004_alter_user_username_opts','2020-05-18 15:55:20.317309'),(7,'auth','0005_alter_user_last_login_null','2020-05-18 15:55:20.437858'),(8,'auth','0006_require_contenttypes_0002','2020-05-18 15:55:20.501046'),(9,'auth','0007_alter_validators_add_error_messages','2020-05-18 15:55:20.543749'),(10,'auth','0008_alter_user_username_max_length','2020-05-18 15:55:20.585190'),(11,'auth','0009_alter_user_last_name_max_length','2020-05-18 15:55:20.618006'),(12,'auth','0010_alter_group_name_max_length','2020-05-18 15:55:20.732553'),(13,'auth','0011_update_proxy_permissions','2020-05-18 15:55:20.783357'),(14,'PestApp','0001_initial','2020-05-18 15:55:22.993423'),(15,'PestApp','0002_delete_captchacaptchastore','2020-05-18 15:55:29.307363'),(16,'admin','0001_initial','2020-05-18 15:55:29.561679'),(17,'admin','0002_logentry_remove_auto_add','2020-05-18 15:55:31.712853'),(18,'admin','0003_logentry_add_action_flag_choices','2020-05-18 15:55:31.770493'),(19,'captcha','0001_initial','2020-05-18 15:55:32.079935'),(20,'sessions','0001_initial','2020-05-18 15:55:32.330763');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) COLLATE utf8mb4_unicode_ci NOT NULL,
  `session_data` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('848bjjqbfbt2nu0y5d83roogul0l72bt','MjMwYWQ2NTEyNDFlMDZkY2JmNzJiNjMyODk2N2NmZDRhMGQ1ZTMyZTp7Il9hdXRoX3VzZXJfaWQiOiIyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIzN2VjMzUxNmJmOWQ0NDA0ZTRhOTBmYjE4MzBmMGQxMjgyNTNhZTU3In0=','2020-06-21 13:58:51.128866'),('bsky7hwgnsi8sqzqi97d4lh44ep4m383','MjMwYWQ2NTEyNDFlMDZkY2JmNzJiNjMyODk2N2NmZDRhMGQ1ZTMyZTp7Il9hdXRoX3VzZXJfaWQiOiIyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIzN2VjMzUxNmJmOWQ0NDA0ZTRhOTBmYjE4MzBmMGQxMjgyNTNhZTU3In0=','2020-06-11 06:07:17.123703'),('lpnx7dgsntq7bve57f0c8ylj48wgofpc','Yzk2ZjU5YzIxZGQzNWFjYjE4ODlmZWIyMDhmM2JkMmYwOTc0YWJmYjp7Il9hdXRoX3VzZXJfaWQiOiIyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIxMGVhMjk2MTAzYTQzOTg5MzNiOTgxYTFmNGJkYWRiMmY1ODI0YzIyIn0=','2020-06-23 17:55:21.556639'),('m1vyi5z1yz5kbnzljxrotnuqiemit0ij','MjMwYWQ2NTEyNDFlMDZkY2JmNzJiNjMyODk2N2NmZDRhMGQ1ZTMyZTp7Il9hdXRoX3VzZXJfaWQiOiIyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIzN2VjMzUxNmJmOWQ0NDA0ZTRhOTBmYjE4MzBmMGQxMjgyNTNhZTU3In0=','2020-06-11 06:07:17.090728'),('ol80d4oud1rl5kmo3mi34iuezc2z5zkc','MjMwYWQ2NTEyNDFlMDZkY2JmNzJiNjMyODk2N2NmZDRhMGQ1ZTMyZTp7Il9hdXRoX3VzZXJfaWQiOiIyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIzN2VjMzUxNmJmOWQ0NDA0ZTRhOTBmYjE4MzBmMGQxMjgyNTNhZTU3In0=','2020-06-12 07:38:09.767559'),('rfq6yfllweizyr7e5058dg3odbi19m3w','MjMwYWQ2NTEyNDFlMDZkY2JmNzJiNjMyODk2N2NmZDRhMGQ1ZTMyZTp7Il9hdXRoX3VzZXJfaWQiOiIyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIzN2VjMzUxNmJmOWQ0NDA0ZTRhOTBmYjE4MzBmMGQxMjgyNTNhZTU3In0=','2020-06-02 01:42:36.771303'),('v4vo04cgwtp20irtqvbiaqnhco9vi4kj','MjMwYWQ2NTEyNDFlMDZkY2JmNzJiNjMyODk2N2NmZDRhMGQ1ZTMyZTp7Il9hdXRoX3VzZXJfaWQiOiIyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIzN2VjMzUxNmJmOWQ0NDA0ZTRhOTBmYjE4MzBmMGQxMjgyNTNhZTU3In0=','2020-06-12 07:38:09.800938');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `donation`
--

DROP TABLE IF EXISTS `donation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `donation` (
  `donation_id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(30) COLLATE utf8mb4_unicode_ci NOT NULL,
  `user_id` int(11) NOT NULL,
  `mask` int(11) DEFAULT NULL,
  `suit` int(11) DEFAULT NULL,
  `alcohol` int(11) DEFAULT NULL,
  `convenient` int(11) DEFAULT NULL,
  `water` int(11) DEFAULT NULL,
  `phone` char(11) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`donation_id`),
  KEY `donation_PestApp_userinfo_id_fk` (`user_id`),
  CONSTRAINT `donation_PestApp_userinfo_id_fk` FOREIGN KEY (`user_id`) REFERENCES `PestApp_userinfo` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `donation`
--

LOCK TABLES `donation` WRITE;
/*!40000 ALTER TABLE `donation` DISABLE KEYS */;
INSERT INTO `donation` VALUES (10,'kale_w',2,10,10,2,2,2,''),(12,'kale_w',2,10,10,2,2,2,'12312312312');
/*!40000 ALTER TABLE `donation` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `keyWords`
--

DROP TABLE IF EXISTS `keyWords`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `keyWords` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `keyWord` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `keyWords_keyWord_uindex` (`keyWord`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `keyWords`
--

LOCK TABLES `keyWords` WRITE;
/*!40000 ALTER TABLE `keyWords` DISABLE KEYS */;
INSERT INTO `keyWords` VALUES (1,'你好');
/*!40000 ALTER TABLE `keyWords` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `reply`
--

DROP TABLE IF EXISTS `reply`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `reply` (
  `reply_id` int(11) NOT NULL AUTO_INCREMENT,
  `from_user_id` int(11) NOT NULL,
  `to_comment_id` int(11) NOT NULL,
  `date` datetime NOT NULL,
  `content` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`reply_id`),
  KEY `reply_PestApp_userinfo_id_fk` (`from_user_id`),
  CONSTRAINT `reply_PestApp_userinfo_id_fk` FOREIGN KEY (`from_user_id`) REFERENCES `PestApp_userinfo` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=142 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reply`
--

LOCK TABLES `reply` WRITE;
/*!40000 ALTER TABLE `reply` DISABLE KEYS */;
INSERT INTO `reply` VALUES (138,3,107,'2020-05-19 00:00:00','测试'),(139,2,107,'2020-05-19 00:00:00','测试'),(140,2,120,'2020-06-10 00:00:00','回复'),(141,2,122,'2020-06-09 17:58:46','测试');
/*!40000 ALTER TABLE `reply` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Temporary table structure for view `userInfoView`
--

DROP TABLE IF EXISTS `userInfoView`;
/*!50001 DROP VIEW IF EXISTS `userInfoView`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE TABLE `userInfoView` (
  `id` tinyint NOT NULL,
  `username` tinyint NOT NULL,
  `signature` tinyint NOT NULL
) ENGINE=MyISAM */;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `volunteer`
--

DROP TABLE IF EXISTS `volunteer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `volunteer` (
  `volunteer_id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(30) COLLATE utf8mb4_unicode_ci NOT NULL,
  `user_id` int(11) NOT NULL,
  `qqNum` varchar(10) COLLATE utf8mb4_unicode_ci NOT NULL,
  `date1` char(8) COLLATE utf8mb4_unicode_ci NOT NULL,
  `date2` char(8) COLLATE utf8mb4_unicode_ci NOT NULL,
  `isDoctor` int(11) NOT NULL,
  `advantage` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
  `words` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `phone` char(11) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`volunteer_id`),
  UNIQUE KEY `volunteer_phoneNumber_uindex` (`user_id`),
  CONSTRAINT `volunteer_PestApp_userinfo_id_fk` FOREIGN KEY (`user_id`) REFERENCES `PestApp_userinfo` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `volunteer`
--

LOCK TABLES `volunteer` WRITE;
/*!40000 ALTER TABLE `volunteer` DISABLE KEYS */;
INSERT INTO `volunteer` VALUES (10,'kale_w',2,'2593872410','00:11:01','00:11:02',1,'会应急救护,有志愿经历','test','');
/*!40000 ALTER TABLE `volunteer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Final view structure for view `userInfoView`
--

/*!50001 DROP TABLE IF EXISTS `userInfoView`*/;
/*!50001 DROP VIEW IF EXISTS `userInfoView`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `userInfoView` AS select `PestApp_userinfo`.`id` AS `id`,`PestApp_userinfo`.`username` AS `username`,`PestApp_userinfo`.`signature` AS `signature` from `PestApp_userinfo` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-06-10  1:59:26
