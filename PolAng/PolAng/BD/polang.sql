-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Paź 19, 2023 at 02:56 PM
-- Wersja serwera: 10.4.28-MariaDB
-- Wersja PHP: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `polang`
--

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `fakewords`
--

CREATE TABLE `fakewords` (
  `id` int(11) NOT NULL,
  `translate` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `fakewords`
--

INSERT INTO `fakewords` (`id`, `translate`) VALUES
(1, 'transom'),
(2, 'chicken'),
(3, 'wearily'),
(4, 'belated'),
(5, 'beneath'),
(6, 'funny'),
(7, 'yowza'),
(8, 'often'),
(9, 'coast'),
(10, 'fooey'),
(11, 'night'),
(12, 'which'),
(13, 'jewel'),
(14, 'sleet'),
(15, 'fooey'),
(16, 'whose'),
(17, 'clean'),
(18, 'salty'),
(19, 'virus'),
(20, 'goose'),
(21, 'yahoo'),
(22, 'these'),
(23, 'haven'),
(24, 'given'),
(25, 'polyp'),
(26, 'truly'),
(27, 'dimly'),
(28, 'fooey'),
(29, 'bogus'),
(30, 'badly'),
(31, 'since'),
(32, 'burly'),
(33, 'scope'),
(34, 'after'),
(35, 'notch'),
(36, 'madly'),
(37, 'bossy'),
(38, 'fully'),
(39, 'where'),
(40, 'aside'),
(41, 'brook'),
(42, 'yowza'),
(43, 'pilaf'),
(44, 'place'),
(45, 'corny'),
(46, 'while'),
(47, 'zowie'),
(48, 'madly'),
(49, 'since'),
(50, 'crest'),
(51, 'yowza'),
(52, 'brook'),
(53, 'steep'),
(54, 'wetly'),
(55, 'print');

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `words`
--

CREATE TABLE `words` (
  `id` int(11) NOT NULL,
  `word` varchar(50) NOT NULL,
  `translate` varchar(50) NOT NULL,
  `image` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `words`
--

INSERT INTO `words` (`id`, `word`, `translate`, `image`) VALUES
(1, 'jabłko', 'apple', 'apple.png'),
(2, 'pomarańcza', 'orange', 'orange.png'),
(3, 'samochód', 'car', 'car.png'),
(4, 'samolot', 'plane', 'plane.png'),
(5, 'lotnisko', 'airport', 'airport.png'),
(6, 'klawiatura', 'keyboard', 'keyboard.png'),
(7, 'rysować', 'draw', 'draw.png'),
(8, 'długopis', 'pencil', 'pencil.png'),
(9, 'mikrofon', 'microphone', 'microphone.png'),
(10, 'latać', 'fly', 'fly.png'),
(11, 'klawisz spacji', 'space bar', 'spacebar.png'),
(12, 'czerwony', 'red', 'red.png'),
(13, 'zielony', 'green', 'green.png'),
(14, 'żółty', 'yellow', 'yellow.png'),
(15, 'sześcian', 'cube', 'cube.png'),
(16, 'koło', 'circle', 'circle.png'),
(17, 'sześciokąt', 'hexagon', 'hexagon.png'),
(18, 'dziesięć', 'ten', 'ten.png'),
(19, 'sześć', 'six', 'six.png'),
(20, 'sto', 'hundred', 'hundred.png'),
(21, 'dziecko', 'child', 'child.png'),
(22, 'matka', 'mother', 'mother.png'),
(23, 'córka', 'daughter', 'daughter.png'),
(24, 'osoba', 'person', 'person.png');

--
-- Indeksy dla zrzutów tabel
--

--
-- Indeksy dla tabeli `fakewords`
--
ALTER TABLE `fakewords`
  ADD PRIMARY KEY (`id`);

--
-- Indeksy dla tabeli `words`
--
ALTER TABLE `words`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `fakewords`
--
ALTER TABLE `fakewords`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=56;

--
-- AUTO_INCREMENT for table `words`
--
ALTER TABLE `words`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=25;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
