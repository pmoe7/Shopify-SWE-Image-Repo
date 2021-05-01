-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 01, 2021 at 02:12 AM
-- Server version: 10.4.11-MariaDB
-- PHP Version: 7.4.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `shopify`
--

-- --------------------------------------------------------

--
-- Table structure for table `images`
--

CREATE TABLE `images` (
  `id` int(11) NOT NULL,
  `title` varchar(100) NOT NULL,
  `descr` text NOT NULL,
  `tags` text NOT NULL,
  `category` varchar(20) NOT NULL,
  `objects` text NOT NULL,
  `img` varchar(1000) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `images`
--

INSERT INTO `images` (`id`, `title`, `descr`, `tags`, `category`, `objects`, `img`) VALUES
(1, 'animals', 'bunch o animals', 'animals', 'animals', 'elephant,zebra,giraffe', 'animals.jpg'),
(2, 'me', 'pic of me', 'me, pic, test', 'people', 'person', 'me.png'),
(3, 'Doggo', 'dog with glasses', 'dog, glasses', 'animals', 'dog', 'dog_glasses.jpg'),
(4, 'Tesla 3', 'pretty red tesla model 3 ', 'red, tesla, car, model, 3', 'cars', 'car', 'tesla.jpg'),
(5, 'Soccer and Salah', 'pic of my fav soccer player', 'soccer, sports, moh, salah, ball', 'sports', 'sports ball,person', 'salah.jpg'),
(6, 'league of legends', 'my fav champ kai sa from LOL', 'kai, sa, lol, league, of, legends, adc, champ', 'games', '', 'kai.jpg'),
(7, 'parrot', 'pretty parrot', 'parrot, animal, bird, birds', 'animals', 'bird,bird', 'parrot.jpg');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `images`
--
ALTER TABLE `images`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `images`
--
ALTER TABLE `images`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=54;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
