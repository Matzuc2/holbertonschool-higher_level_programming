-- This script creates the table force_name with columns id and name if it does not exist.
CREATE TABLE IF NOT EXISTS force_name (
    id INT, -- The id column is of type INT.
    name VARCHAR(256) NOT NULL -- The name column is of type VARCHAR with a maximum length of 256 characters and cannot be NULL.
);