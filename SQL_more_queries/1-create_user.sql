-- This command creates a new user 'user_0d_1' with password 'user_0d_1_pwd' on localhost, 
-- but only if the user does not already exist.
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';