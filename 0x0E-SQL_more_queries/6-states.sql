-- create a database

CREATE DATABASE IF NOT EXISTS `hbtn_0d_usa`;

-- specify the database to use

USE hbtn_0d_usa;

-- create table

CREATE TABLE IF NOT EXISTS `states` (
	PRIMARY KEY(`id`),
	`id` INT AUTO INCREMENT,
	`name` VARCHAR(256) NOT NULL
	);
