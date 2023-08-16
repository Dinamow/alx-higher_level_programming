-- a script that creates the database hbtn_0d_usa and the table cities
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities(
	id INT PRIMARY KEY AUTO_INCREMENT,
	name VARCHAR(256) NOT NULL,
	state_id INT,
	FOREIGN KEY (state_id) REFERENCES states(id)
);
