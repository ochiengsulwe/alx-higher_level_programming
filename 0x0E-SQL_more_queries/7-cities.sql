--create database

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- specify database to use
USE hbtn_0d_usa;

-- create cities  table
CREATE TABLE IF NOT EXISTS cities (
	id INT AUTO_INCREMENT PRIMARY KEY,
	state_id INT NOT NULL,
	name VARCHAR(256) NOT NULL,
	FOREIGN KEY (state_id) REFERENCES states (id)
	);	
