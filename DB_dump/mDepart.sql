-- phpMyAdmin SQL Dump
-- version 3.4.11.1deb2
-- http://www.phpmyadmin.net
--
-- Client: localhost
-- Généré le: Mer 21 Mai 2014 à 00:19
-- Version du serveur: 5.5.35
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
  `ping` int(11) DEFAULT NULL,
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
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

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
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=5 ;

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

--
-- Contraintes pour les tables exportées
--

--
-- Contraintes pour la table `locations`
--
ALTER TABLE `locations`
  ADD CONSTRAINT `locations_ibfk_2` FOREIGN KEY (`position_id`) REFERENCES `positions` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `locations_ibfk_1` FOREIGN KEY (`address_id`) REFERENCES `addresses` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Contraintes pour la table `transportation`
--
ALTER TABLE `transportation`
  ADD CONSTRAINT `transportation_ibfk_1` FOREIGN KEY (`location_id`) REFERENCES `locations` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
