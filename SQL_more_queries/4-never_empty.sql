-- This script creates the table id_not_null with columns id and name if it does not exist.
CREATE TABLE IF NOT EXISTS id_not_null (
    id INT DEFAULT 1,
    name VARCHAR(256) NOT NULL
);