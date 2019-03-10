-- phpMyAdmin SQL Dump
-- version 4.8.3
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Mar 10, 2019 at 12:36 PM
-- Server version: 10.1.37-MariaDB
-- PHP Version: 7.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `fas`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `id` int(255) NOT NULL,
  `username` varchar(256) NOT NULL,
  `password` varchar(256) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`id`, `username`, `password`) VALUES
(1, 'admin', '2c08e8f5884750a7b99f6f2f342fc638db25ff31');

-- --------------------------------------------------------

--
-- Table structure for table `attendance`
--

CREATE TABLE `attendance` (
  `id` int(255) NOT NULL,
  `student_id` varchar(256) NOT NULL,
  `class_code` varchar(256) NOT NULL,
  `date` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `attendance`
--

INSERT INTO `attendance` (`id`, `student_id`, `class_code`, `date`) VALUES
(1, '1001', 'MATH_101', '2018-09-09'),
(2, '1002', 'MATH_101', '2019-09-09'),
(3, '1002', 'PSY_101', '2019-09-09');

-- --------------------------------------------------------

--
-- Table structure for table `classes`
--

CREATE TABLE `classes` (
  `id` int(255) NOT NULL,
  `class_id` varchar(256) NOT NULL,
  `class_code` varchar(256) NOT NULL,
  `teacher_name` varchar(256) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `classes`
--

INSERT INTO `classes` (`id`, `class_id`, `class_code`, `teacher_name`) VALUES
(1, '1001', 'MATH_101', 'Saqib Shabir'),
(2, '1002', 'PSY_101', 'Rafeeq'),
(3, '1020', 'PHY_101', 'Saqib Shabir'),
(4, '10299', 'BIO_101', 'Shams'),
(5, '1223', 'PE_101', 'Shams'),
(6, '1990', 'PE_102', 'Saqib Sir'),
(8, '1009234', 'PSY_2001', 'Mr. Zaroo');

-- --------------------------------------------------------

--
-- Table structure for table `students`
--

CREATE TABLE `students` (
  `id` int(255) NOT NULL,
  `student_id` varchar(256) NOT NULL,
  `name` varchar(256) NOT NULL,
  `dob` date NOT NULL,
  `guardian` varchar(256) NOT NULL,
  `address` text NOT NULL,
  `image_path` text NOT NULL,
  `fingerprint_id` int(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `students`
--

INSERT INTO `students` (`id`, `student_id`, `name`, `dob`, `guardian`, `address`, `image_path`, `fingerprint_id`) VALUES
(4, '1001', 'Abdul Hanan Zaroo', '1991-07-25', 'Mohammad Inam Zaroo', 'Peerbagh', 'C:\\Users\\Hanan\\Desktop\\Fingerprint Attendance System/assets/project_img/1543931438.1.jpg', 0),
(5, '1002', 'Saqib Shabir', '1992-09-19', 'Shabir Ahmed', 'Srinagar', 'C:\\Users\\Hanan\\Desktop\\Fingerprint Attendance System/assets/project_img/1543931560.23.jpg', 0),
(7, '1012', 'Hanan', '1991-09-19', 'Mr Inam Zaroo', 'H2 Cooperative', 'C:\\Users\\Hanan\\Desktop\\Fingerprint Attendance System/assets/project_img/1543932907.73.jpg', 0),
(8, '1004', 'Saqib Shabir', '1992-09-19', 'Shabir Ahmad', 'Srinagar', 'C:\\Users\\Hanan\\Desktop\\Fingerprint Attendance System/assets/project_img/1543934502.01.jpg', 0),
(9, '300012', 'Abdul Zaroo', '2019-01-01', 'Mr. Zaroo', 'Some Adress', 'C:\\Users\\Hanan\\Desktop\\Fingerprint Attendance System/assets/project_img/1546343631.95.jpg', 0),
(10, '0192384', 'Kali Kal', '2000-01-01', 'Kali', 'Some address', 'C:\\Users\\Hanan\\Desktop\\Fingerprint Attendance System/assets/project_img/1550582467.99.jpg', 0);

-- --------------------------------------------------------

--
-- Table structure for table `student_classes`
--

CREATE TABLE `student_classes` (
  `id` int(255) NOT NULL,
  `student_id` varchar(256) NOT NULL,
  `class_code` varchar(256) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `student_classes`
--

INSERT INTO `student_classes` (`id`, `student_id`, `class_code`) VALUES
(5, '1001', 'MATH_101'),
(6, '1001', 'PSY_101'),
(7, '1002', 'PSY_101'),
(8, '1002', 'MATH_101'),
(11, '1012', 'BIO_101'),
(12, '1012', 'PHY_101'),
(13, '1004', 'MATH_101'),
(14, '1004', 'PE_101'),
(15, '300012', 'PSY_2001'),
(16, '0192384', 'PSY_101'),
(17, '0192384', 'PHY_101');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `attendance`
--
ALTER TABLE `attendance`
  ADD PRIMARY KEY (`id`),
  ADD KEY `student_id` (`student_id`),
  ADD KEY `class_code` (`class_code`);

--
-- Indexes for table `classes`
--
ALTER TABLE `classes`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `class_code` (`class_code`),
  ADD KEY `class_id` (`class_id`);

--
-- Indexes for table `students`
--
ALTER TABLE `students`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `student_id` (`student_id`);

--
-- Indexes for table `student_classes`
--
ALTER TABLE `student_classes`
  ADD PRIMARY KEY (`id`),
  ADD KEY `student_id` (`student_id`),
  ADD KEY `class_code` (`class_code`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `admin`
--
ALTER TABLE `admin`
  MODIFY `id` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `attendance`
--
ALTER TABLE `attendance`
  MODIFY `id` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `classes`
--
ALTER TABLE `classes`
  MODIFY `id` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `students`
--
ALTER TABLE `students`
  MODIFY `id` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `student_classes`
--
ALTER TABLE `student_classes`
  MODIFY `id` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `attendance`
--
ALTER TABLE `attendance`
  ADD CONSTRAINT `attendance_ibfk_1` FOREIGN KEY (`class_code`) REFERENCES `classes` (`class_code`),
  ADD CONSTRAINT `attendance_ibfk_2` FOREIGN KEY (`student_id`) REFERENCES `students` (`student_id`);

--
-- Constraints for table `student_classes`
--
ALTER TABLE `student_classes`
  ADD CONSTRAINT `student_classes_ibfk_1` FOREIGN KEY (`class_code`) REFERENCES `classes` (`class_code`),
  ADD CONSTRAINT `student_classes_ibfk_2` FOREIGN KEY (`student_id`) REFERENCES `students` (`student_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
