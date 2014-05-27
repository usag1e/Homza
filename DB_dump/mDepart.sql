-- phpMyAdmin SQL Dump
-- version 3.4.11.1deb2
-- http://www.phpmyadmin.net
--
-- Client: localhost
-- Généré le: Mar 27 Mai 2014 à 23:34
-- Version du serveur: 5.5.37
-- Version de PHP: 5.4.4-14+deb7u9

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Base de données: `mDepart`
--

-- --------------------------------------------------------

--
-- Structure de la table `addresses`
--

CREATE TABLE IF NOT EXISTS `addresses` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `number` int(11) DEFAULT NULL,
  `street` char(255) DEFAULT NULL,
  `postcode` char(255) DEFAULT NULL,
  `city` char(255) DEFAULT NULL,
  `state` char(255) DEFAULT NULL,
  `country` char(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Structure de la table `internet`
--

CREATE TABLE IF NOT EXISTS `internet` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `connected` tinyint(1) NOT NULL,
  `timestamp` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Structure de la table `iss`
--

CREATE TABLE IF NOT EXISTS `iss` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `timestamp` datetime NOT NULL,
  `date` datetime NOT NULL,
  `duration` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `date` (`date`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=47 ;

--
-- Contenu de la table `iss`
--

INSERT INTO `iss` (`id`, `timestamp`, `date`, `duration`) VALUES
(2, '2014-05-27 00:10:23', '2014-05-27 04:34:49', 481),
(3, '2014-05-27 00:11:26', '2014-05-27 04:34:52', 478),
(4, '2014-05-27 20:16:28', '2014-05-28 03:47:15', 352),
(5, '2014-05-27 20:58:45', '2014-05-28 03:47:21', 346),
(6, '2014-05-27 20:58:45', '2014-05-28 05:20:53', 615),
(7, '2014-05-27 20:58:45', '2014-05-28 06:57:28', 633),
(8, '2014-05-27 20:58:45', '2014-05-28 08:34:41', 625),
(9, '2014-05-27 20:58:45', '2014-05-28 10:11:46', 634),
(10, '2014-05-27 20:58:54', '2014-05-28 03:47:18', 349),
(12, '2014-05-27 20:59:04', '2014-05-28 03:47:25', 338),
(13, '2014-05-27 20:59:04', '2014-05-28 05:20:54', 614),
(15, '2014-05-27 21:00:51', '2014-05-28 03:47:33', 332),
(16, '2014-05-27 21:00:51', '2014-05-28 05:20:51', 627),
(17, '2014-05-27 21:00:51', '2014-05-28 06:57:27', 634),
(18, '2014-05-27 21:00:51', '2014-05-28 08:34:44', 622),
(20, '2014-05-27 21:00:56', '2014-05-28 03:47:23', 342),
(22, '2014-05-27 21:01:00', '2014-05-28 03:47:24', 342),
(25, '2014-05-27 21:01:09', '2014-05-28 03:47:22', 344),
(28, '2014-05-27 21:02:37', '2014-05-28 03:47:20', 346),
(30, '2014-05-27 21:08:01', '2014-05-28 03:47:16', 351),
(32, '2014-05-27 21:09:09', '2014-05-28 03:47:19', 347),
(34, '2014-05-27 23:16:02', '2014-05-28 03:47:27', 337),
(37, '2014-05-27 23:20:06', '2014-05-28 03:47:31', 333),
(38, '2014-05-27 23:20:06', '2014-05-28 05:20:50', 627);

-- --------------------------------------------------------

--
-- Structure de la table `locations`
--

CREATE TABLE IF NOT EXISTS `locations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` char(255) DEFAULT NULL,
  `address_id` int(11) DEFAULT NULL,
  `is_transportation_stop` tinyint(1) NOT NULL DEFAULT '0',
  `position_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `address_id` (`address_id`),
  KEY `position_id` (`position_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=3 ;

--
-- Contenu de la table `locations`
--

INSERT INTO `locations` (`id`, `name`, `address_id`, `is_transportation_stop`, `position_id`) VALUES
(1, 'test', NULL, 0, 2),
(2, 'home', NULL, 0, 1);

-- --------------------------------------------------------

--
-- Structure de la table `positions`
--

CREATE TABLE IF NOT EXISTS `positions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `latitude` char(50) DEFAULT NULL,
  `longitude` char(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=3 ;

--
-- Contenu de la table `positions`
--

INSERT INTO `positions` (`id`, `latitude`, `longitude`) VALUES
(1, '45.4963857', '-73.62036'),
(2, '32.235435', '112.123124');

-- --------------------------------------------------------

--
-- Structure de la table `transportation`
--

CREATE TABLE IF NOT EXISTS `transportation` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `timestamp` datetime NOT NULL,
  `line` varchar(35) DEFAULT NULL,
  `direction` varchar(35) DEFAULT NULL,
  `time_of_arrival` time DEFAULT NULL,
  `location_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `location_id` (`location_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Structure de la table `weather`
--

CREATE TABLE IF NOT EXISTS `weather` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `timestamp` datetime NOT NULL,
  `id_station` int(11) DEFAULT NULL,
  `name_station` varchar(55) DEFAULT NULL,
  `clouds` float DEFAULT NULL,
  `time` datetime DEFAULT NULL,
  `humidity` float DEFAULT NULL,
  `pressure` int(11) DEFAULT NULL,
  `temp` float DEFAULT NULL,
  `temp_max` float DEFAULT NULL,
  `temp_min` float DEFAULT NULL,
  `rain` float DEFAULT NULL,
  `sunrise` datetime DEFAULT NULL,
  `sunset` datetime DEFAULT NULL,
  `weather` varchar(55) DEFAULT NULL,
  `description` varchar(255) DEFAULT NULL,
  `icon` varchar(10) DEFAULT NULL,
  `wind_deg` float DEFAULT NULL,
  `wind_speed` float DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=5 ;

--
-- Contenu de la table `weather`
--

INSERT INTO `weather` (`id`, `timestamp`, `id_station`, `name_station`, `clouds`, `time`, `humidity`, `pressure`, `temp`, `temp_max`, `temp_min`, `rain`, `sunrise`, `sunset`, `weather`, `description`, `icon`, `wind_deg`, `wind_speed`) VALUES
(1, '2014-05-27 23:16:02', 6138980, 'Saint-Raymond', 64, '2014-05-27 23:07:40', 98, 1007, 11.74, 13.89, 10, 2.5, '2014-05-27 10:11:46', '2014-05-28 01:31:39', 'Rain', 'light rain', '10d', 35, 1.54),
(2, '2014-05-27 23:17:16', 6138980, 'Saint-Raymond', 64, '2014-05-27 23:07:40', 98, 1007, 11.74, 13.89, 10, 2.5, '2014-05-27 10:11:46', '2014-05-28 01:31:39', 'Rain', 'light rain', '10d', 35, 1.54),
(3, '2014-05-27 23:20:06', 6138980, 'Saint-Raymond', 64, '2014-05-27 23:07:40', 98, 1007, 11.74, 13.89, 10, 2.5, '2014-05-27 10:11:46', '2014-05-28 01:31:39', 'Rain', 'light rain', '10d', 35, 1.54),
(4, '2014-05-27 23:21:51', 6138980, 'Saint-Raymond', 64, '2014-05-27 23:07:40', 98, 1007, 11.74, 13.89, 10, 2.5, '2014-05-27 10:11:46', '2014-05-28 01:31:39', 'Rain', 'light rain', '10d', 35, 1.54);

--
-- Contraintes pour les tables exportées
--

--
-- Contraintes pour la table `locations`
--
ALTER TABLE `locations`
  ADD CONSTRAINT `locations_ibfk_1` FOREIGN KEY (`address_id`) REFERENCES `addresses` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `locations_ibfk_2` FOREIGN KEY (`position_id`) REFERENCES `positions` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Contraintes pour la table `transportation`
--
ALTER TABLE `transportation`
  ADD CONSTRAINT `transportation_ibfk_1` FOREIGN KEY (`location_id`) REFERENCES `locations` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
