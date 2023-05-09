CREATE DATABASE proyecto;

USE proyecto;

DROP TABLE IF EXISTS users;
CREATE TABLE IF NOT EXISTS users(
    id INT NOT NULL AUTO_INCREMENT,
    nombres VARCHAR(100) NOT NULL,
    apellidos VARCHAR(100) NOT NULL,
    password VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    fecha_nacimiento DATE NOT NULL,
    cedula VARCHAR(10) UNIQUE NOT NULL,
    edad TINYINT NOT NULL,
    rol SET('admin','profesor') DEFAULT 'profesor',
    PRIMARY KEY (id)
);


-- INSERT INTO users (nombres,apellidos,password,email,fecha_nacimiento,cedula,edad,rol) VALUES ("Cristian Alejandro","Barajas Bolivar","300804","cristianbarajasimasc@gmail.com","2004-08-30","31357876",18,"admin");

