-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Feb 07, 2024 at 05:47 PM
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
-- Struktura tabeli dla tabeli `easy_words`
--

CREATE TABLE `easy_words` (
  `id` int(11) NOT NULL,
  `word` varchar(50) NOT NULL,
  `translate` varchar(50) NOT NULL,
  `image` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `easy_words`
--

INSERT INTO `easy_words` (`id`, `word`, `translate`, `image`) VALUES
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
-- Struktura tabeli dla tabeli `hard_words`
--

CREATE TABLE `hard_words` (
  `id` int(11) NOT NULL,
  `word` varchar(50) NOT NULL,
  `translate` varchar(50) NOT NULL,
  `image` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `hard_words`
--

INSERT INTO `hard_words` (`id`, `word`, `translate`, `image`) VALUES
(26, 'Ocean', 'Morze', 'morze.png'),
(27, 'Sunflower', 'Słonecznik', 'slonecznik.png'),
(28, 'Coffee', 'Kawa', 'kawa.png'),
(29, 'Butterfly', 'Motyl', 'motyl.png'),
(30, 'Bedroom', 'Sypialnia', 'sypialnia.png'),
(31, 'Lamp', 'Lampa', 'lampa.png'),
(32, 'Mobile', 'Telefon komórkowy', 'telefon_komorkowy.png'),
(33, 'Forest', 'Las', 'las.png'),
(34, 'Seashell', 'Muszla morska', 'muszla_morska.png'),
(35, 'Bookshelf', 'Półka na książki', 'polka_na_ksiazki.png'),
(36, 'Plane', 'Samolot', 'samolot.png'),
(37, 'Snow', 'Śnieg', 'snieg.png'),
(38, 'Doorway', 'Wejście', 'wejscie.png'),
(39, 'Cap', 'Czapka', 'czapka.png'),
(40, 'Piano', 'Fortepian', 'fortepian.png'),
(41, 'Orange', 'Pomarańcza', 'pomarancza.png'),
(42, 'Beacon', 'Latarnia', 'latarnia.png'),
(43, 'Globe', 'Globus', 'globus.png'),
(44, 'Boots', 'Buty zimowe', 'buty_zimowe.png'),
(45, 'Kite', 'Latawiec', 'latawiec.png'),
(46, 'Sofa', 'Sofa', 'sofa.png'),
(47, 'Sky', 'Niebo', 'niebo.png'),
(48, 'River', 'Rzeka', 'rzeka.png'),
(49, 'Leopard', 'Leopard', 'leopard.png'),
(50, 'Android', 'Android', 'android.png');

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `medhar_words`
--

CREATE TABLE `medhar_words` (
  `id` int(11) NOT NULL,
  `word` varchar(50) NOT NULL,
  `translate` varchar(50) NOT NULL,
  `image` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `medhar_words`
--

INSERT INTO `medhar_words` (`id`, `word`, `translate`, `image`) VALUES
(1, 'Dog', 'Pies', 'pies.png'),
(2, 'Sky', 'Niebo', 'niebo.png'),
(3, 'Cup', 'Kubek', 'kubek.png'),
(4, 'Rainbow', 'Tęcza', 'tecza.png'),
(5, 'Bed', 'Łóżko', 'lozko.png'),
(6, 'Candle', 'Świeca', 'swieca.png'),
(7, 'Phone', 'Telefon', 'telefon.png'),
(8, 'Lake', 'Jezioro', 'jezioro.png'),
(9, 'Starfish', 'Rozgwiazda', 'rozgwiazda.png'),
(10, 'Camera', 'Aparat', 'aparat.png'),
(11, 'Train', 'Pociąg', 'pociag.png'),
(12, 'Rain', 'Deszcz', 'deszcz.png'),
(13, 'Window', 'Okno', 'okno.png'),
(14, 'Hat', 'Kapelusz', 'kapelusz.png'),
(15, 'Guitar', 'Gitara', 'gitara.png'),
(16, 'Apple', 'Jabłko', 'jablko.png'),
(17, 'Lighthouse', 'Latarnia morska', 'latarnia.png'),
(18, 'Map', 'Mapa', 'mapa.png'),
(19, 'Shoes', 'Buty', 'buty.png'),
(20, 'Balloon', 'Balon', 'balon.png'),
(21, 'Chair', 'Krzesło', 'krzeslo.png'),
(22, 'Cloud', 'Chmura', 'chmura.png'),
(23, 'Ocean', 'Ocean', 'ocean.png'),
(24, 'Tiger', 'Tygrys', 'tygrys.png'),
(25, 'Robot', 'Robot', 'robot.png');

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `medium_words`
--

CREATE TABLE `medium_words` (
  `id` int(11) NOT NULL,
  `word` varchar(10) NOT NULL,
  `translate` varchar(10) NOT NULL,
  `image` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `medium_words`
--

INSERT INTO `medium_words` (`id`, `word`, `translate`, `image`) VALUES
(1, 'Tree', 'Drzewo', 'drzewo.png'),
(2, 'Ocean', 'Ocean', 'ocean.png'),
(3, 'Book', 'Książka', 'ksiazka.pn'),
(4, 'Cloud', 'Chmura', 'chmura.png'),
(5, 'Chair', 'Krzesło', 'krzeslo.pn'),
(6, 'Window', 'Okno', 'okno.png'),
(7, 'Elephant', 'Słoń', 'slon.png'),
(8, 'River', 'Rzeka', 'rzeka.png'),
(9, 'Sun', 'Słońce', 'slonce.png'),
(10, 'Guitar', 'Gitara', 'gitara.png'),
(11, 'Mountain', 'Góra', 'gora.png'),
(12, 'Flower', 'Kwiat', 'kwiat.png'),
(13, 'Clock', 'Zegar', 'zegar.png'),
(14, 'Key', 'Klucz', 'klucz.png'),
(15, 'Door', 'Drzwi', 'drzwi.png'),
(16, 'Hat', 'Kapelusz', 'kapelusz.p'),
(17, 'Table', 'Stół', 'stol.png'),
(18, 'Moon', 'Księżyc', 'ksiezyc.pn'),
(19, 'Backpack', 'Plecak', 'plecak.png'),
(20, 'Star', 'Gwiazda', 'gwiazda.pn'),
(21, 'Cat', 'Kot', 'kot.png'),
(22, 'Car', 'Samochód', 'samochod.p'),
(23, 'Smile', 'Uśmiech', 'usmiech.pn'),
(24, 'Bridge', 'Most', 'most.png'),
(25, 'Dog', 'Pies', 'pies.png'),
(26, 'Sky', 'Niebo', 'niebo.png'),
(27, 'Cup', 'Kubek', 'kubek.png'),
(28, 'Rainbow', 'Tęcza', 'tecza.png'),
(29, 'Bed', 'Łóżko', 'lozko.png'),
(30, 'Candle', 'Świeca', 'swieca.png'),
(31, 'Phone', 'Telefon', 'telefon.pn'),
(32, 'Lake', 'Jezioro', 'jezioro.pn'),
(33, 'Starfish', 'Rozgwiazda', 'rozgwiazda'),
(34, 'Camera', 'Aparat', 'aparat.png'),
(35, 'Train', 'Pociąg', 'pociag.png'),
(36, 'Rain', 'Deszcz', 'deszcz.png'),
(37, 'Window', 'Okno', 'okno.png'),
(38, 'Hat', 'Kapelusz', 'kapelusz.p'),
(39, 'Guitar', 'Gitara', 'gitara.png'),
(40, 'Apple', 'Jabłko', 'jablko.png'),
(41, 'Lighthouse', 'Latarnia m', 'latarnia.p'),
(42, 'Map', 'Mapa', 'mapa.png'),
(43, 'Shoes', 'Buty', 'buty.png'),
(44, 'Balloon', 'Balon', 'balon.png'),
(45, 'Chair', 'Krzesło', 'krzeslo.pn'),
(46, 'Cloud', 'Chmura', 'chmura.png'),
(47, 'Ocean', 'Ocean', 'ocean.png'),
(48, 'Tiger', 'Tygrys', 'tygrys.png'),
(49, 'Robot', 'Robot', 'robot.png'),
(50, 'Dog', 'Pies', 'pies.png'),
(51, 'Sky', 'Niebo', 'niebo.png'),
(52, 'Cup', 'Kubek', 'kubek.png'),
(53, 'Rainbow', 'Tęcza', 'tecza.png'),
(54, 'Bed', 'Łóżko', 'lozko.png'),
(55, 'Candle', 'Świeca', 'swieca.png'),
(56, 'Phone', 'Telefon', 'telefon.pn'),
(57, 'Lake', 'Jezioro', 'jezioro.pn'),
(58, 'Starfish', 'Rozgwiazda', 'rozgwiazda'),
(59, 'Camera', 'Aparat', 'aparat.png'),
(60, 'Train', 'Pociąg', 'pociag.png'),
(61, 'Rain', 'Deszcz', 'deszcz.png'),
(62, 'Window', 'Okno', 'okno.png'),
(63, 'Hat', 'Kapelusz', 'kapelusz.p'),
(64, 'Guitar', 'Gitara', 'gitara.png'),
(65, 'Apple', 'Jabłko', 'jablko.png'),
(66, 'Lighthouse', 'Latarnia m', 'latarnia.p'),
(67, 'Map', 'Mapa', 'mapa.png'),
(68, 'Shoes', 'Buty', 'buty.png'),
(69, 'Balloon', 'Balon', 'balon.png'),
(70, 'Chair', 'Krzesło', 'krzeslo.pn'),
(71, 'Cloud', 'Chmura', 'chmura.png'),
(72, 'Ocean', 'Ocean', 'ocean.png'),
(73, 'Tiger', 'Tygrys', 'tygrys.png'),
(74, 'Robot', 'Robot', 'robot.png');

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `pol_fakewords`
--

CREATE TABLE `pol_fakewords` (
  `id` int(11) NOT NULL,
  `word` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `pol_fakewords`
--

INSERT INTO `pol_fakewords` (`id`, `word`) VALUES
(1, 'dom'),
(2, 'kot'),
(3, 'pies'),
(4, 'szczęście'),
(5, 'miłość'),
(6, 'przygoda'),
(7, 'szkoła'),
(8, 'komputer'),
(9, 'telefon'),
(10, 'kawa'),
(11, 'książka'),
(12, 'muzyka'),
(13, 'chleb'),
(14, 'jabłko'),
(15, 'samochód'),
(16, 'kwiat'),
(17, 'trawa'),
(18, 'słońce'),
(19, 'morze'),
(20, 'spacer'),
(21, 'kino'),
(22, 'kawałek'),
(23, 'serce'),
(24, 'dzień'),
(25, 'noc');

--
-- Indeksy dla zrzutów tabel
--

--
-- Indeksy dla tabeli `easy_words`
--
ALTER TABLE `easy_words`
  ADD PRIMARY KEY (`id`);

--
-- Indeksy dla tabeli `fakewords`
--
ALTER TABLE `fakewords`
  ADD PRIMARY KEY (`id`);

--
-- Indeksy dla tabeli `hard_words`
--
ALTER TABLE `hard_words`
  ADD PRIMARY KEY (`id`);

--
-- Indeksy dla tabeli `medhar_words`
--
ALTER TABLE `medhar_words`
  ADD PRIMARY KEY (`id`);

--
-- Indeksy dla tabeli `medium_words`
--
ALTER TABLE `medium_words`
  ADD PRIMARY KEY (`id`);

--
-- Indeksy dla tabeli `pol_fakewords`
--
ALTER TABLE `pol_fakewords`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `easy_words`
--
ALTER TABLE `easy_words`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=25;

--
-- AUTO_INCREMENT for table `fakewords`
--
ALTER TABLE `fakewords`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=56;

--
-- AUTO_INCREMENT for table `hard_words`
--
ALTER TABLE `hard_words`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=51;

--
-- AUTO_INCREMENT for table `medhar_words`
--
ALTER TABLE `medhar_words`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=26;

--
-- AUTO_INCREMENT for table `medium_words`
--
ALTER TABLE `medium_words`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=75;

--
-- AUTO_INCREMENT for table `pol_fakewords`
--
ALTER TABLE `pol_fakewords`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=26;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
