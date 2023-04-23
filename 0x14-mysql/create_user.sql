CREATE USER 'holberton_user'@'localhost' IDENTIFIED BY 'projectcorrection280hbtn';
GRANT REPLICATION CLIENT ON *.* TO 'holberton_user'@'localhost';
CREATE DATABASE tyrell_corp;
use tyrell_corp;
CREATE TABLE nexus6 (
	id int NOT NULL AUTO_INCREMENT,
	name varchar(30) NOT NULL,
	PRIMARY KEY (id)
);
INSERT INTO nexus6 (name) VALUES ('Leon');
GRANT SELECT ON tyrell_corp.nexus6 TO 'holberton_user'@'localhost';
GRANT SELECT ON mysql.user TO 'holberton_user'@'localhost';
CREATE USER 'replica_user' IDENTIFIED BY 'replica123';
GRANT REPLICATION SLAVE ON *.* TO 'replica_user';
