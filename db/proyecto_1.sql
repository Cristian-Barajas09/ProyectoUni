-- Active: 1687916797927@@127.0.0.1@3306@proyecto

DROP DATABASE IF EXISTS proyecto;
CREATE DATABASE IF NOT EXISTS proyecto;

USE proyecto;

DROP TABLE IF EXISTS users;
CREATE TABLE IF NOT EXISTS users(
    cedula VARCHAR(10) UNIQUE NOT NULL,
    nombres VARCHAR(50),
    apellidos VARCHAR(50),
    password VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    fecha_nacimiento DATE NOT NULL,
    edad TINYINT NOT NULL,
    n_telefono VARCHAR(12),
    sexo SET('M','F') NOT NULL,
    rol SET('admin','profesor','administracion') DEFAULT 'profesor',
    status SET ('activo','inactivo') DEFAULT 'activo',
    create_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (cedula)
);


INSERT INTO users
(cedula,nombres,apellidos,password,email,fecha_nacimiento,edad,n_telefono,sexo,rol)
VALUES ('1','admin','admin','$2a$12$m6qhNLM2B/cjyjlqVuaUXOsZjiuwmLvZz/IJvhb/p6.JyLfK/r7Ea','admin@admin','2000-01-01',18,'0424-7411450','M','admin');


DROP TABLE IF EXISTS estudiantes;
CREATE TABLE IF NOT EXISTS estudiantes (
    cedula_escolar VARCHAR(12) UNIQUE,
    nombres VARCHAR(100) NOT NULL,
    apellidos VARCHAR(100) NOT NULL,
    fecha_nacimiento DATE NOT NULL,
    edad TINYINT NOT NULL,
    sexo SET('M','F') NOT NULL,lugar_nacimiento VARCHAR(50),
    entidad_federal VARCHAR(50),
    nacionalidad VARCHAR(50),
    turno SET('M','T') NOT NULL,
    instituto_procedencia VARCHAR(20),
    parto VARCHAR(20) NOT NULL,
    proceso_nacimiento SET('N','C','F','T'),
    mano_dominante SET('D','I','A'),
    peso FLOAT NOT NULL,
    talla FLOAT NOT NULL,
    talla_comisa VARCHAR(2),
    talla_pantalon VARCHAR(2),
    zapatos VARCHAR(2),
    con_quien_vive VARCHAR(10) NOT NULL,
    cuando_hablo TINYINT ,
    cuando_camino TINYINT,
    duerme_con VARCHAR(10),
    tiene_hermanos BOOLEAN ,
    donde_estudian_hermanos VARCHAR(20),
    habla_correctamente BOOLEAN,
    con_quien_juega VARCHAR(20),
    seccion VARCHAR(1) NOT NULL,
    PRIMARY KEY(cedula_escolar),
    status SET ('activo','inactivo') DEFAULT 'activo',
    create_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_seccion FOREIGN KEY (seccion) REFERENCES annos(seccion)
);


SELECT * FROM representantes;

CREATE TABLE gustos(
    id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    cedula_estudiante VARCHAR(12) NOT NULL,
    gusto VARCHAR(20),
    CONSTRAINT fk_estudiante_gustos FOREIGN KEY (cedula_estudiante) REFERENCES estudiantes(cedula_escolar)
);



CREATE TABLE juegos(
    id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    cedula_estudiante VARCHAR(12) NOT NULL,
    juego VARCHAR(20),
    CONSTRAINT fk_estudiante_juegos FOREIGN KEY (cedula_estudiante) REFERENCES estudiantes(cedula_escolar)
);


CREATE TABLE actividades(
    id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    cedula_estudiante VARCHAR(12) NOT NULL,
    actividad VARCHAR(20),
    CONSTRAINT fk_estudiante_actividades FOREIGN KEY (cedula_estudiante) REFERENCES estudiantes(cedula_escolar)
);



CREATE TABLE vacunas(
    id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    cedula_estudiante VARCHAR(12) NOT NULL,
    vacuna VARCHAR(20),
    CONSTRAINT fk_estudiante_vacunas FOREIGN KEY (cedula_estudiante) REFERENCES estudiantes(cedula_escolar)
);



CREATE TABLE alergias(
    id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    cedula_estudiante VARCHAR(12) NOT NULL,
    alergias VARCHAR(20),
    CONSTRAINT fk_estudiante_alergias FOREIGN KEY (cedula_estudiante) REFERENCES estudiantes(cedula_escolar)
);


CREATE TABLE enfermedades(
    id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    cedula_estudiante VARCHAR(12) NOT NULL,
    enfermedad VARCHAR(20),
    CONSTRAINT fk_estudiante_enfermedades FOREIGN KEY (cedula_estudiante) REFERENCES estudiantes(cedula_escolar)
);

select * from enfermedades;

DROP TABLE IF EXISTS representantes;
CREATE TABLE IF NOT EXISTS representantes(
    cedula VARCHAR(10) UNIQUE NOT NULL PRIMARY KEY,
    nacionalidad VARCHAR(20),
    profesion VARCHAR(20),
    nombres VARCHAR(50),
    apellidos VARCHAR(50),
    vive_con_el BOOLEAN NOT NULL,
    parentesco VARCHAR(10),
    create_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    status SET ('activo','inactivo') DEFAULT 'activo'
);

select * from representantes;


CREATE TABLE direcciones(
    cedula VARCHAR(12) NOT NULL,
    direccion VARCHAR(50),
    de VARCHAR(20),
    CONSTRAINT fk_direccion FOREIGN KEY (cedula) REFERENCES representantes(cedula)
);


CREATE TABLE telefonos(
    cedula VARCHAR(12) NOT NULL,
    n_telefono VARCHAR(12),
    CONSTRAINT fk_telefono FOREIGN KEY (cedula) REFERENCES representantes(cedula)
);


DROP TABLE IF EXISTS annos;
CREATE TABLE IF NOT EXISTS annos(
    seccion VARCHAR(1),
    anno VARCHAR(9) NOT NULL UNIQUE,
    grupo ENUM('A','B','C'),
    id_profesor VARCHAR(10) NOT NULL UNIQUE,
    PRIMARY KEY(seccion),
    CONSTRAINT fk_profesor FOREIGN KEY (id_profesor) REFERENCES users(cedula)
);

INSERT INTO annos (anno,grupo,seccion,id_profesor) VALUES ('2023-2024','A','A',1);

INSERT INTO annos (anno,grupo,seccion,id_profesor) VALUES ('2023-2024','A','B',"31357876");

SELECT * FROM estudiantes;

CREATE TABLE representante_legal(
    cedula_representante VARCHAR(10),
    cedula_estudiante VARCHAR(12) NOT NULL,
    parentesco VARCHAR(50) NOT NULL,
    CONSTRAINT fk_representante_legal_estudiante FOREIGN KEY (cedula_estudiante) REFERENCES estudiantes(cedula_escolar),
    CONSTRAINT fk_representante_legal FOREIGN KEY (cedula_representante) REFERENCES representantes(cedula)
);

CREATE TABLE sessions(
    user_ced VARCHAR(12) NOT NULL,
    status BOOLEAN DEFAULT FALSE,
    create_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,CONSTRAINT fk_session FOREIGN KEY (user_ced) REFERENCES users(cedula)
);

SHOW TABLES;


 
