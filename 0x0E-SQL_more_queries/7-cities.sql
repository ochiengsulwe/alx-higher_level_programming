--crezate database

CREATE DATABASE IF NOT EXISTS `hbtn_0d_usa`;

-- specify database to use

USE `hbtn_0d_usa`;

-- create table

CREATE TABLE IF NOT EXISTS `cities` (
	`id` INT AUTO_INCREMENT PRIMARY KEY,
	`state_id` INT NOT NULL,
	FOREIGN KEY (`state_id`) REFERENCES `states` (`id`)
	);	
