CREATE DATABASE IF NOT EXISTS examination;

USE examination;

SHOW TABLES;

CREATE TABLE member (
         email VARCHAR(100),
         login_pass varchar(100),
         num varchar(10),
         roll varchar(8)
     );
     
     CREATE TABLE student (
         email VARCHAR(100),
         login_pass varchar(100),
         num varchar(10),
         roll varchar(8)
     );
     
     CREATE TABLE teacher (
         email VARCHAR(100),
         login_pass varchar(100),
         num varchar(10),
         roll varchar(8)
     );
     
     CREATE TABLE file_path (
		  file_path VARCHAR(500)
    );
