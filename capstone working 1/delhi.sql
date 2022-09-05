-- phpMyAdmin SQL Dump
-- version 5.1.3
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Aug 15, 2022 at 08:52 AM
-- Server version: 10.4.24-MariaDB
-- PHP Version: 7.4.29

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `my_python`
--

-- --------------------------------------------------------

--
-- Table structure for table `delhi`
--

CREATE TABLE `delhi` (
  `title` varchar(10000) NOT NULL,
  `date` date NOT NULL,
  `url` varchar(500) NOT NULL,
  `description` mediumtext NOT NULL,
  `source` mediumtext NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `delhi`
--

INSERT INTO `delhi` (`title`, `date`, `url`, `description`, `source`) VALUES
('\n        <![CDATA[7 arrested for posing as police officers ]]>\n    ', '0000-00-00', 'https://www.thehindu.com/news/cities/Delhi/7-arrested-for-posing-as-police-officers/article65769886.ece        ', '\n        <![CDATA[]]>\n    ', 'thehindu'),
('\n        <![CDATA[HC seeks Centre’s stand on assistance to children suffering from rare disease ]]>\n    ', '0000-00-00', 'https://www.thehindu.com/news/cities/Delhi/hc-seeks-centres-stand-on-assistance-to-children-suffering-from-rare-disease/article65768731.ece        ', '\n        <![CDATA[54 children seek financial help in enrolling for clinical trials of new drug]]>\n    ', 'thehindu'),
('\n        <![CDATA[Man strangulated by manja ]]>\n    ', '0000-00-00', 'https://www.thehindu.com/news/cities/Delhi/man-strangulated-by-manja/article65769880.ece        ', '\n        <![CDATA[]]>\n    ', 'thehindu'),
('\n        <![CDATA[‘Memory park’ for pet lovers inaugurated in Delhi ]]>\n    ', '0000-00-00', 'https://www.thehindu.com/news/cities/Delhi/memory-park-for-pet-lovers-inaugurated-in-delhi/article65769893.ece        ', '\n        <![CDATA[]]>\n    ', 'thehindu'),
('\n        <![CDATA[Time to remember Ambedkar’s contribution: CM ]]>\n    ', '0000-00-00', 'https://www.thehindu.com/news/cities/Delhi/time-to-remember-ambedkars-contribution-cm/article65769233.ece        ', '\n        <![CDATA[L-G honours lone surviving member of INA]]>\n    ', 'thehindu'),
('\n        <![CDATA[Yamuna water level falls below danger mark ]]>\n    ', '0000-00-00', 'https://www.thehindu.com/news/cities/Delhi/yamuna-water-level-falls-below-danger-mark/article65768582.ece        ', '\n        <![CDATA[Relief camp set up for nearly 37,000 people]]>\n    ', 'thehindu'),
('\n        <![CDATA[Yamuna water level in Delhi recedes below danger mark ]]>\n    ', '0000-00-00', 'https://www.thehindu.com/news/cities/Delhi/yamuna-water-level-in-delhi-recedes-below-danger-mark/article65767812.ece        ', '\n        <![CDATA[Downward trend likely to continue in Yamuna water level]]>\n    ', 'thehindu');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `delhi`
--
ALTER TABLE `delhi`
  ADD PRIMARY KEY (`url`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
