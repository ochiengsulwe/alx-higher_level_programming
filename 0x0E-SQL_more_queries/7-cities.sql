--crezate database

CREATE DATABASE IF NOT EXISTS `hbtn_0d_usa`;

-- specify database to use

USE `hbtn_0d_usa`;

-- creates states table

CREATE TABLE IF NOT EXISTS `states` (
	`id` INT AUTO_INCREMENT PRIMARY KEY,
	`name` VARCHAR(256)
	);

-- create cities  table

CREATE TABLE IF NOT EXISTS `cities` (
	`id` INT AUTO_INCREMENT PRIMARY KEY,
	`state_id` INT NOT NULL,
	FOREIGN KEY (`state_id`) REFERENCES `states` (`id`)
	);	
