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

CREATE TABLE direcciones(
    cedula VARCHAR(12) NOT NULL,
    direccion VARCHAR(50),
    de VARCHAR(20),
    CONSTRAINT fk_direccion FOREIGN KEY (cedula) REFERENCES representantes(cedula)
);


CREATE TABLE telefonos_representantes(
    cedula VARCHAR(12) NOT NULL,
    n_telefono VARCHAR(12),
    CONSTRAINT fk_telefono FOREIGN KEY (cedula) REFERENCES representantes(cedula)
);

CREATE TABLE representante_legal(
    cedula_representante VARCHAR(10),
    cedula_estudiante VARCHAR(12) NOT NULL,
    parentesco VARCHAR(50) NOT NULL,
    CONSTRAINT fk_representante_legal_estudiante FOREIGN KEY (cedula_estudiante) REFERENCES estudiantes(cedula_escolar),
    CONSTRAINT fk_representante_legal FOREIGN KEY (cedula_representante) REFERENCES representantes(cedula)
);