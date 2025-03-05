-- This script creates the table cities with columns id, state_id, and name if it does not exist.
CREATE DATABASE IF NOT EXISTS `hbtn_0d_usa`;
USE `hbtn_0d_usa`;

CREATE TABLE IF NOT EXISTS cities (
    id INT AUTO_INCREMENT UNIQUE NOT NULL PRIMARY KEY,
    state_id INT NOT NULL,
    FOREIGN KEY (state_id) REFERENCES states(id),
    name VARCHAR(256) NOT NULL
);