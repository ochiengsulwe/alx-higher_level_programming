-- create database

CREATE DATABASE IF NOT EXISTS  hbtn_0d_2;

-- specify the database to use

USE  hbtn_0d_2;

-- create user

CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- grant single privilage

GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
