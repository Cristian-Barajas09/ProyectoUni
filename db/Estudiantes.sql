DROP TABLE IF EXISTS annos;
CREATE TABLE IF NOT EXISTS annos(
    seccion VARCHAR(1),
    anno VARCHAR(9) NOT NULL UNIQUE,
    grupo ENUM('A','B','C'),
    id_profesor VARCHAR(10) NOT NULL UNIQUE,
    PRIMARY KEY(seccion),
    CONSTRAINT fk_profesor FOREIGN KEY (id_profesor) REFERENCES usuarios(cedula)
);

CREATE TABLE IF NOT EXISTS Estudiantes (
    cedula_escolar VARCHAR(12) UNIQUE,
    nombres VARCHAR(100) NOT NULL,
    apellidos VARCHAR(100) NOT NULL,
    fecha_nacimiento DATE NOT NULL,
    edad TINYINT NOT NULL,
    sexo SET('M','F') NOT NULL,lugar_nacimiento VARCHAR(50),
    entidad_federal VARCHAR(50),
    nacionalidad VARCHAR(50),
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


CREATE TABLE Turnos (
    id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    cedula_escolar VARCHAR(12) NOT NULL,
    turno SET('M','T') NOT NULL,
    CONSTRAINT fk_estudiante_turno FOREIGN KEY (cedula_escolar) REFERENCES Estudiantes(cedula_escolar)
);


CREATE TABLE gustos(
    id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    cedula_estudiante VARCHAR(12) NOT NULL,
    gusto VARCHAR(20),
    CONSTRAINT fk_estudiante_gustos FOREIGN KEY (cedula_estudiante) REFERENCES Estudiantes(cedula_escolar)
);



CREATE TABLE juegos(
    id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    cedula_estudiante VARCHAR(12) NOT NULL,
    juego VARCHAR(20),
    CONSTRAINT fk_estudiante_juegos FOREIGN KEY (cedula_estudiante) REFERENCES Estudiantes(cedula_escolar)
);


CREATE TABLE actividades(
    id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    cedula_estudiante VARCHAR(12) NOT NULL,
    actividad VARCHAR(20),
    CONSTRAINT fk_estudiante_actividades FOREIGN KEY (cedula_estudiante) REFERENCES Estudiantes(cedula_escolar)
);



CREATE TABLE vacunas(
    id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    cedula_estudiante VARCHAR(12) NOT NULL,
    vacuna VARCHAR(20),
    CONSTRAINT fk_estudiante_vacunas FOREIGN KEY (cedula_estudiante) REFERENCES Estudiantes(cedula_escolar)
);



CREATE TABLE alergias(
    id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    cedula_estudiante VARCHAR(12) NOT NULL,
    alergias VARCHAR(20),
    CONSTRAINT fk_estudiante_alergias FOREIGN KEY (cedula_estudiante) REFERENCES Estudiantes(cedula_escolar)
);


CREATE TABLE enfermedades(
    id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    cedula_estudiante VARCHAR(12) NOT NULL,
    enfermedad VARCHAR(20),
    CONSTRAINT fk_estudiante_enfermedades FOREIGN KEY (cedula_estudiante) REFERENCES Estudiantes(cedula_escolar)
);

