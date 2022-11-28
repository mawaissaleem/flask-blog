-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Nov 28, 2022 at 07:00 AM
-- Server version: 10.4.25-MariaDB
-- PHP Version: 8.1.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `shadow_coding`
--

-- --------------------------------------------------------

--
-- Table structure for table `contact`
--

CREATE TABLE `contact` (
  `sno` int(11) NOT NULL,
  `name` text NOT NULL,
  `phone_num` varchar(50) NOT NULL,
  `date` datetime DEFAULT current_timestamp(),
  `email` varchar(50) NOT NULL,
  `msg` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `contact`
--

INSERT INTO `contact` (`sno`, `name`, `phone_num`, `date`, `email`, `msg`) VALUES
(1, 'first', '123', '2022-11-18 00:48:30', 'first@gmail.com', 'abcdfd fjdsf'),
(2, 'sh', '34354', NULL, 'sh@gmail.com', 'sdjfndjsg g'),
(3, 'gjasd', '473284', NULL, 'fjsd@sdfd.com', 'checking flask mail'),
(4, 'fdsfj', '3423', NULL, 'dfk@kgd.com', 'checking flask mail'),
(5, 'fdsfj', '3423', NULL, 'dfk@kgd.com', 'checking flask mail'),
(6, 'fdsfj', '3423', NULL, 'dfk@kgd.com', 'checking flask mail'),
(7, 'fdsfj', '3423', NULL, 'dfk@kgd.com', 'checking flask mail'),
(8, 'fdsfj', '3423', NULL, 'dfk@kgd.com', 'checking flask mail');

-- --------------------------------------------------------

--
-- Table structure for table `post`
--

CREATE TABLE `post` (
  `sno` int(11) NOT NULL,
  `title` text NOT NULL,
  `slug` varchar(20) NOT NULL,
  `content` text NOT NULL,
  `date` datetime NOT NULL,
  `img_file` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `post`
--

INSERT INTO `post` (`sno`, `title`, `slug`, `content`, `date`, `img_file`) VALUES
(1, '2 Advandasdtages to Taking Online Classes', 'first-post', 'Both recent high school graduates and nontraditional learners can take advantage of online classes. Online courses offer flexibility, affordable tuition, and a variety of academic opportunities. Distance learners who want to experience learning on campus can enrol in hybrid courses, which blend classroom instruction with online learning.', '2022-11-20 20:53:21', 'about-bg.jpg'),
(2, 'Innovation Management', '21chsadfInnovation-m', 'The first one on the list of top innovation blogs is InnovationManagement.se, which evolved from an online magazine with an audience based mostly in Western Europe to an online resource and learning center with an impressive growing global audience. Besides that, IM has collaborated with educational institutions and industry leaders on numerous side-projects such as research, reports, training and forums. Their mission is to provide relevant, inspiring and actionable knowledge to businesses and individuals looking to increase their innovation capabilities.In this blog you may find best practices, tools and related resources among innovation practitioners and professionals. It is a really great blog if you are interested in latest cutting-edge approaches to innovation challenges.', '2022-11-20 22:27:47', 'about-bg.jgp'),
(3, 'Cryptocurrency Explained', 'Cryptocurrency-Expla', 'A cryptocurrency is a digital or virtual currency that is secured by cryptography, which makes it nearly impossible to counterfeit or double-spend. Many cryptocurrencies are decentralized networks based on blockchain technology—a distributed ledger enforced by a disparate network of computers.\r\n\r\nA defining feature of cryptocurrencies is that they are generally not issued by any central authority, rendering them theoretically immune to government interference or manipulation.', '2022-11-20 22:29:10', 'about-bg.jgp'),
(4, 'How Does the Future of NFT Look Like?', 'Future-of-NFT', 'NFT has enhanced media exposure and special perks for aspiring artists on social media. Recently, Jack Dorsey, the CEO and co-founder of Twitter, with his very first and famous tweet, \"just setting up my twttr,\" and Vignesh Sundaresan, famously known as \"Metakovan,\" bought 69.3 million dollars worth of NFT art on Beeple. ', '2022-11-20 22:30:45', 'about-bg.jgp'),
(5, 'metaverse', 'metaverse', 'Imagine a virtual world where billions of people live, work, shop, learn and interact with each other -- all from the comfort of their couches in the physical world.\r\n\r\nIn this world, the computer screens we use today to connect to a worldwide web of information have become portals to a 3D virtual realm that\'s palpable -- like real life, only bigger and better. Digital facsimiles of ourselves, or avatars, move freely from one experience to another, taking our identities and our money with us.', '2022-11-20 22:32:13', 'about-bg.jgp'),
(6, 'THE ROLE OF AR AND VR IN THE DEVELOPMENT OF THE METAVERSE', 'THE-ROLE-OF-AR-AND-V', 'Technology such as artificial intelligence (AI), augmented reality (AR), and virtual reality (VR) are all strongly tied to the concept of the metaverse (VR). With the use of augmented reality technology, you may incorporate virtual objects into the actual environment. To fully immerse yourself in a 3D virtual environment, VR uses 3D computer modelling, one of the most fascinating sorts of visual designs. Although wearing a VR headset or other attachments isn’t strictly necessary in the metaverse, experts are sure that virtual reality technology will become a crucial part of the new environment.', '2022-11-20 22:33:23', 'about-bg.jgp');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `contact`
--
ALTER TABLE `contact`
  ADD PRIMARY KEY (`sno`);

--
-- Indexes for table `post`
--
ALTER TABLE `post`
  ADD PRIMARY KEY (`sno`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `contact`
--
ALTER TABLE `contact`
  MODIFY `sno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `post`
--
ALTER TABLE `post`
  MODIFY `sno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
