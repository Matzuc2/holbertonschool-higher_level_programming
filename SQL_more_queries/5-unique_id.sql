-- This script creates the table unique_id with columns id and name if it does not exist.
CREATE TABLE IF NOT EXISTS unique_id (
    id INT DEFAULT 1 UNIQUE,
    name VARCHAR(256) NOT NULL
);