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
    peso
    talla,
    talla_comisa,
    talla_pantalon,
    zapatos,
    con_quien_vive,
    cuando_hablo,
    cuando_camino,
    duerme_con,
    tiene_hermanos,
    donde_estudia_hermanos
    habla_correctamente
    con_quien_juega,
    

    id_representante INT NOT NULL,
    id_anno INT NOT NULL,
    PRIMARY KEY(id),
    CONSTRAINT fk_representante FOREIGN KEY (id_representante) REFERENCES representantes(id),
    CONSTRAINT fk_annos FOREIGN KEY (id_anno) REFERENCES annos(anno)
);

CREATE TABLE gustos(

);

CREATE TABLE juegos(
    
);

CREATE TABLE actividades(
    id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    id_estudiante
    vacuna VARCHAR(20)
);


CREATE TABLE vacunas(
    id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    id_estudiante,

    vacuna VARCHAR(20)
);

CREATE TABLE alergias(
    id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    id_estudiante,
    alergias VARCHAR(20)
);

CREATE TABLE enfermedades(
    id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    id_estudiante,
    enfermedad VARCHAR(20)
);

DROP TABLE IF EXISTS representantes;
CREATE TABLE IF NOT EXISTS representantes(
    id INT NOT NULL AUTO_INCREMENT,
    nombres VARCHAR(50),
    apellidos VARCHAR(50),
    email VARCHAR(255) NOT NULL UNIQUE,
    fecha_nacimiento DATE NOT NULL,
    cedula VARCHAR(10) UNIQUE NOT NULL,
    edad TINYINT NOT NULL,
    n_telefono VARCHAR(12),
    PRIMARY KEY(id)
);

DROP TABLE IF EXISTS annos;
CREATE TABLE IF NOT EXISTS annos(
    anno INT NOT NULL UNIQUE,
    seccion VARCHAR(1),
    id_profesor INT NOT NULL,
    PRIMARY KEY(annos),
    CONSTRAINT fk_profesor FOREIGN KEY (id_profesor) REFERENCES users(id)
);


CREATE TABLE sessions(
    user_id INT NOT NULL,
    status BOOLEAN DEFAULT FALSE,
    create_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_session FOREIGN KEY (user_id) REFERENCES users(id)
);


DROP DATABASE proyecto;



-- INSERT INTO users (nombres,apellidos,password,email,fecha_nacimiento,cedula,edad,rol) VALUES ("Cristian Alejandro","Barajas Bolivar","300804","cristianbarajasimasc@gmail.com","2004-08-30","31357876",18,"admin");

