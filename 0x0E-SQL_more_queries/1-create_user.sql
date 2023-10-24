-- creating a new user

CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

-- granting all previlegages to the user

GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
