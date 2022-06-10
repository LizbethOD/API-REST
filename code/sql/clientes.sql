DROP TABLE IF EXISTS clientes;

CREATE TABLE clientes (
    id_cliente INTEGER     PRIMARY KEY         AUTOINCREMENT,
    nombre                  varchar(50)         NOT NULL,
    email                   varchar(50)         NOT NULL
    );

INSERT INTO clientes (nombre,email) VALUES ("Yess", "Yess@email.com");
INSERT INTO clientes (nombre,email) VALUES ("Liz", "liz@email.com");
INSERT INTO clientes (nombre,email) VALUES ("Rey", "Rey@email.com");

.headers OFF 

SELECT * FROM clientes;