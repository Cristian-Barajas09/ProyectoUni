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
    PRIMARY KEY (cedula)
);


INSERT INTO users 
(cedula,nombres,apellidos,password,email,fecha_nacimiento,edad,n_telefono,sexo,rol) 
VALUES ('1','admin','admin','$2a$12$m6qhNLM2B/cjyjlqVuaUXOsZjiuwmLvZz/IJvhb/p6.JyLfK/r7Ea','admin@admin','2000-01-01',18,'0424-7411450','M','admin');


DROP TABLE IF EXISTS estudiantes;
CREATE TABLE IF NOT EXISTS estudiantes (
    id INT NOT NULL AUTO_INCREMENT,
    nombres VARCHAR(100) NOT NULL,
    apellidos VARCHAR(100) NOT NULL,
    fecha_nacimiento DATE NOT NULL,
    edad TINYINT NOT NULL,
    sexo SET('M','F') NOT NULL,

    lugar_nacimiento VARCHAR(50),
    entidad_federal VARCHAR(50),
    nacionalidad VARCHAR(50),
    cedula_escolar VARCHAR(12),
    turno SET('M','T') NOT NULL,
    instituto_procedencia VARCHAR(20),
    parto VARCHAR(20) NOT NULL,
    proceso_nacimiento SET('N','C','F','T'),
    mano_dominante SET('D','I','A'),
    peso DECIMAL(2,2) NOT NULL,
    talla DECIMAL(2,2) NOT NULL,
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

    id_representante  VARCHAR(10) UNIQUE NOT NULL,
    id_anno INT NOT NULL,
    PRIMARY KEY(id),
    CONSTRAINT fk_representante FOREIGN KEY (id_representante) REFERENCES representantes(cedula),
    CONSTRAINT fk_annos FOREIGN KEY (id_anno) REFERENCES annos(anno)
);

CREATE TABLE gustos(

);

CREATE TABLE juegos(

    id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    id_estudiante INT NOT NULL,
    gusto VARCHAR(20),
    CONSTRAINT fk_estudiante_gustos FOREIGN KEY (id_estudiante) REFERENCES estudiantes(id)
);

CREATE TABLE juegos(
    id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    id_estudiante INT NOT NULL,
    juego VARCHAR(20),
    CONSTRAINT fk_estudiante_juegos FOREIGN KEY (id_estudiante) REFERENCES estudiantes(id)

);

CREATE TABLE actividades(
    id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    id_estudiante INT NOT NULL,
    actividad VARCHAR(20),
    CONSTRAINT fk_estudiante_actividades FOREIGN KEY (id_estudiante) REFERENCES estudiantes(id)

);


CREATE TABLE vacunas(
    id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    id_estudiante INT NOT NULL,
    vacuna VARCHAR(20),
    CONSTRAINT fk_estudiante_vacunas FOREIGN KEY (id_estudiante) REFERENCES estudiantes(id)

);

CREATE TABLE alergias(
    id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    id_estudiante INT NOT NULL,
    alergias VARCHAR(20),
    CONSTRAINT fk_estudiante_alergias FOREIGN KEY (id_estudiante) REFERENCES estudiantes(id)
);

CREATE TABLE enfermedades(
    id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    id_estudiante INT NOT NULL,
    enfermedad VARCHAR(20),
    CONSTRAINT fk_estudiante_enfermedades FOREIGN KEY (id_estudiante) REFERENCES estudiantes(id)

);

DROP TABLE IF EXISTS representantes;
CREATE TABLE IF NOT EXISTS representantes(
    cedula VARCHAR(10) UNIQUE NOT NULL PRIMARY KEY,
    nacionalidad VARCHAR(20),
    profesion VARCHAR(20),
    nombres VARCHAR(50),
    apellidos VARCHAR(50),

    vive_con_el BOOLEAN NOT NULL

);

CREATE TABLE direcciones(
    cedula VARCHAR(12) NOT NULL,
    direccion VARCHAR(50),
    de VARCHAR(20),
    CONSTRAINT fk_direccion FOREIGN KEY (cedula) REFERENCES representantes(cedula)
);

CREATE TABLE telefonos(

    cedula VARCHAR(10) UNIQUE NOT NULL,
    n_telefono VARCHAR(12),
    CONSTRAINT fk_telefono FOREIGN KEY (cedula) REFERENCES representantes(cedula)
);

DROP TABLE IF EXISTS annos;
CREATE TABLE IF NOT EXISTS annos(
    anno INT NOT NULL UNIQUE,
    seccion VARCHAR(1),
    id_profesor VARCHAR(10) NOT NULL UNIQUE,
    PRIMARY KEY(anno),
    CONSTRAINT fk_profesor FOREIGN KEY (id_profesor) REFERENCES users(cedula)
);


CREATE TABLE sessions(
    user_id INT NOT NULL,
    status BOOLEAN DEFAULT FALSE,
    create_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_session FOREIGN KEY (user_id) REFERENCES users(id)
);

SHOW TABLES;

DROP DATABASE proyecto;



-- INSERT INTO users (nombres,apellidos,password,email,fecha_nacimiento,cedula,edad,rol) VALUES ("Cristian Alejandro","Barajas Bolivar","300804","cristianbarajasimasc@gmail.com","2004-08-30","31357876",18,"admin");

