CREATE DATABASE proyecto_v2;

USE proyecto_v2;

DROP TABLE IF EXISTS users;
CREATE TABLE IF NOT EXISTS Usuarios(
    cedula VARCHAR(10) UNIQUE NOT NULL,
    nombres VARCHAR(50),
    apellidos VARCHAR(50),
    password VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    fecha_nacimiento DATE NOT NULL,
    edad TINYINT NOT NULL,
    n_telefono VARCHAR(12),
    sexo SET('M','F') NOT NULL,
    rol SET('superadmin','profesor','administracion') DEFAULT 'profesor',
    status SET ('activo','inactivo') DEFAULT 'activo',
    create_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (cedula)
);

CREATE TABLE Telefonos(
    id INT NOT NULL AUTO_INCREMENT,
    cedula VARCHAR(10) NOT NULL,
    n_telefono VARCHAR(12) NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (cedula) REFERENCES Usuarios(cedula)
);


CREATE TABLE sessions(
    user_ced VARCHAR(12) NOT NULL,
    status BOOLEAN DEFAULT FALSE,
    create_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_session FOREIGN KEY (user_ced) REFERENCES usuarios(cedula)
);
