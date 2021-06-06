-- MySQL dump 10.13  Distrib 5.7.33, for Linux (x86_64)
--
-- Host: localhost    Database: animal_disease
-- ------------------------------------------------------
-- Server version	5.7.33-0ubuntu0.18.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `animals`
--

DROP TABLE IF EXISTS `animals`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `animals` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `species_id` int(11) DEFAULT NULL,
  `production_type_id` int(11) DEFAULT NULL,
  `sub_unit_id` int(11) DEFAULT NULL,
  `establishment_id` int(11) DEFAULT NULL,
  `birth_establishment_id` int(11) DEFAULT NULL,
  `birth_sub_unit_id` int(11) DEFAULT NULL,
  `birth_country_id` int(11) DEFAULT NULL,
  `sex` int(11) DEFAULT NULL,
  `birth_date` datetime DEFAULT NULL,
  `mother_animal_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_new_table_1_idx` (`birth_country_id`),
  KEY `fk_animals_2_idx` (`establishment_id`),
  KEY `fk_animals_3_idx` (`birth_establishment_id`),
  KEY `fk_animals_5_idx` (`birth_sub_unit_id`),
  KEY `fk_animals_6_idx` (`sub_unit_id`),
  KEY `fk_animals_4_idx` (`production_type_id`),
  KEY `fk_animals_7_idx` (`species_id`),
  CONSTRAINT `fk_animals_1` FOREIGN KEY (`birth_country_id`) REFERENCES `countries` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_animals_2` FOREIGN KEY (`establishment_id`) REFERENCES `establishments` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_animals_3` FOREIGN KEY (`birth_establishment_id`) REFERENCES `establishments` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_animals_4` FOREIGN KEY (`production_type_id`) REFERENCES `production_types` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_animals_5` FOREIGN KEY (`birth_sub_unit_id`) REFERENCES `sub_units` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_animals_6` FOREIGN KEY (`sub_unit_id`) REFERENCES `sub_units` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_animals_7` FOREIGN KEY (`species_id`) REFERENCES `species` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `countries`
--

DROP TABLE IF EXISTS `countries`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `countries` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(45) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`),
  UNIQUE KEY `name_UNIQUE` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `disease_detections`
--

DROP TABLE IF EXISTS `disease_detections`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `disease_detections` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `geo_location_id` int(11) DEFAULT NULL,
  `disease_id` int(11) DEFAULT NULL,
  `species_id` int(11) DEFAULT NULL,
  `production_type_id` int(11) DEFAULT NULL,
  `outbreak_type` varchar(45) DEFAULT NULL,
  `num_susceptible` int(11) DEFAULT NULL,
  `num_affected` int(11) DEFAULT NULL,
  `num_killed` int(11) DEFAULT NULL,
  `num_destroyed` int(11) DEFAULT NULL,
  `kg_destroyed` varchar(45) DEFAULT NULL,
  `suspicion_date` datetime DEFAULT NULL,
  `confirmation_date` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_disease_detections_1_idx` (`disease_id`),
  KEY `fk_disease_detections_2_idx` (`geo_location_id`),
  KEY `fk_disease_detections_3_idx` (`species_id`),
  KEY `fk_disease_detections_4_idx` (`production_type_id`),
  CONSTRAINT `fk_disease_detections_1` FOREIGN KEY (`disease_id`) REFERENCES `diseases` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_disease_detections_2` FOREIGN KEY (`geo_location_id`) REFERENCES `geo_locations` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_disease_detections_3` FOREIGN KEY (`species_id`) REFERENCES `species` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_disease_detections_4` FOREIGN KEY (`production_type_id`) REFERENCES `production_types` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `diseases`
--

DROP TABLE IF EXISTS `diseases`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `diseases` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(45) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name_UNIQUE` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `establishments`
--

DROP TABLE IF EXISTS `establishments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `establishments` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `geo_location_id` int(11) DEFAULT NULL,
  `production_type_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_establishments_1_idx` (`geo_location_id`),
  KEY `fk_establishments_2_idx` (`production_type_id`),
  CONSTRAINT `fk_establishments_1` FOREIGN KEY (`geo_location_id`) REFERENCES `geo_locations` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_establishments_2` FOREIGN KEY (`production_type_id`) REFERENCES `production_types` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `geo_locations`
--

DROP TABLE IF EXISTS `geo_locations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `geo_locations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `coord_precision` decimal(10,0) DEFAULT NULL,
  `x_coord` decimal(10,0) DEFAULT NULL,
  `y_coord` decimal(10,0) DEFAULT NULL,
  `address` varchar(45) DEFAULT NULL,
  `zip_code` varchar(45) DEFAULT NULL,
  `country_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_geo_locations_1_idx` (`country_id`),
  CONSTRAINT `fk_geo_locations_1` FOREIGN KEY (`country_id`) REFERENCES `countries` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `monitoring_datas`
--

DROP TABLE IF EXISTS `monitoring_datas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `monitoring_datas` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `animal_id` int(11) DEFAULT NULL,
  `sub_unit_id` int(11) DEFAULT NULL,
  `establishment_id` int(11) DEFAULT NULL,
  `disease_detection_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_monitoring_datas_1_idx` (`animal_id`),
  KEY `fk_monitoring_datas_2_idx` (`sub_unit_id`),
  KEY `fk_monitoring_datas_3_idx` (`establishment_id`),
  KEY `fk_monitoring_datas_4_idx` (`disease_detection_id`),
  CONSTRAINT `fk_monitoring_datas_1` FOREIGN KEY (`animal_id`) REFERENCES `animals` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_monitoring_datas_2` FOREIGN KEY (`sub_unit_id`) REFERENCES `sub_units` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_monitoring_datas_3` FOREIGN KEY (`establishment_id`) REFERENCES `establishments` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_monitoring_datas_4` FOREIGN KEY (`disease_detection_id`) REFERENCES `disease_detections` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `production_types`
--

DROP TABLE IF EXISTS `production_types`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `production_types` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(45) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name_UNIQUE` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `species`
--

DROP TABLE IF EXISTS `species`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `species` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(45) NOT NULL,
  PRIMARY KEY (`id`,`name`),
  UNIQUE KEY `species_UNIQUE` (`id`),
  UNIQUE KEY `name_UNIQUE` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `sub_units`
--

DROP TABLE IF EXISTS `sub_units`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `sub_units` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `establishment_id` int(11) NOT NULL,
  `geo_location_id` int(11) NOT NULL,
  `production_type_id` int(11) NOT NULL,
  `species_id` int(11) NOT NULL,
  `actual_number` int(11) DEFAULT NULL,
  `capacity` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`),
  KEY `fk_sub_units_1_idx` (`species_id`),
  KEY `fk_sub_units_2_idx` (`establishment_id`),
  KEY `fk_sub_units_3_idx` (`geo_location_id`),
  KEY `fk_sub_units_4_idx` (`production_type_id`),
  CONSTRAINT `fk_sub_units_1` FOREIGN KEY (`species_id`) REFERENCES `species` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_sub_units_2` FOREIGN KEY (`establishment_id`) REFERENCES `establishments` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_sub_units_3` FOREIGN KEY (`geo_location_id`) REFERENCES `geo_locations` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_sub_units_4` FOREIGN KEY (`production_type_id`) REFERENCES `production_types` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-03-22 20:54:35
