CREATE DATABASE proyecto;

USE proyecto;

DROP TABLE IF EXISTS users;
CREATE TABLE IF NOT EXISTS users(
    id INT NOT NULL AUTO_INCREMENT,
    primer_nombre VARCHAR(100) NOT NULL,
    segundo_nombre VARCHAR(100) NOT NULL,
    primer_apellido VARCHAR(100) NOT NULL,
    segundo_apellido VARCHAR(100) NOT NULL,
    password VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    fecha_nacimiento DATE NOT NULL,
    cedula VARCHAR(10) UNIQUE NOT NULL,
    edad TINYINT NOT NULL,
    n_telefono VARCHAR(12),
    sexo SET('M','F') NOT NULL,
    rol SET('admin','profesor') DEFAULT 'profesor',
    PRIMARY KEY (id)
);

DROP TABLE IF EXISTS estudiantes;
CREATE TABLE IF NOT EXISTS estudiantes(
    id INT NOT NULL AUTO_INCREMENT,
    nombres VARCHAR(100) NOT NULL,
    apellidos VARCHAR(100) NOT NULL,
    fecha_nacimiento DATE NOT NULL,
    edad TINYINT NOT NULL,
    id_representante INT NOT NULL,
    id_seccion CHAR NOT NULL,
    PRIMARY KEY(id),
    CONSTRAINT fk_representante FOREIGN KEY (id_representante) REFERENCES representantes(id),
    CONSTRAINT fk_seccion FOREIGN KEY (id_seccion) REFERENCES secciones(seccion)
);

DROP TABLE IF EXISTS representantes;
CREATE TABLE IF NOT EXISTS representantes(
    id INT NOT NULL AUTO_INCREMENT,
    primer_nombre VARCHAR(100) NOT NULL,
    segundo_nombre VARCHAR(100) NOT NULL,
    primer_apellido VARCHAR(100) NOT NULL,
    segundo_apellido VARCHAR(100) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    fecha_nacimiento DATE NOT NULL,
    cedula VARCHAR(10) UNIQUE NOT NULL,
    edad TINYINT NOT NULL,
    n_telefono VARCHAR(12),
    PRIMARY KEY(id)
);

DROP TABLE IF EXISTS secciones;
CREATE TABLE IF NOT EXISTS secciones(
    seccion CHAR NOT NULL UNIQUE,
    id_profesor INT NOT NULL,
    PRIMARY KEY(seccion),
    CONSTRAINT fk_profesor FOREIGN KEY (id_profesor) REFERENCES users(id)
);






-- INSERT INTO users (nombres,apellidos,password,email,fecha_nacimiento,cedula,edad,rol) VALUES ("Cristian Alejandro","Barajas Bolivar","300804","cristianbarajasimasc@gmail.com","2004-08-30","31357876",18,"admin");

