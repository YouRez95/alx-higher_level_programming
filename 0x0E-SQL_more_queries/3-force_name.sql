-- create table force_name
-- if the table already exist the script should not fail
CREATE TABLE IF NOT EXISTS force_name (
	id INT,
	name VARCHAR(256) NOT NULL
);
