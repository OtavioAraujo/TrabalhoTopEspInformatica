CREATE TABLE tb_usuario (
    id_usuario          SERIAL,
    email               VARCHAR(50) UNIQUE NOT NULL,
    nome                VARCHAR(50) NOT NULL,
    senha               VARCHAR(50) NOT NULL,
    
    CONSTRAINT pk_tb_usuario_id_usuario
    PRIMARY KEY(id_usuario)
);

CREATE TABLE tb_fabricante (
    id_fabricante       SERIAL,
    nome                VARCHAR(50) UNIQUE NOT NULL,

    CONSTRAINT pk_tb_marca_id_fabricante 
    PRIMARY KEY(id_fabricante)
);

CREATE TABLE tb_nave (
    id_nave             SERIAL,
    id_fabricante       INTEGER,
    nome                VARCHAR(50) UNIQUE NOT NULL,
    modelo              VARCHAR(50) NOT NULL,
    tripulacao          INTEGER,
    passageiros         INTEGER,
    capacidade_carga    NUMERIC(23,2),
    preco               NUMERIC(23,2),

    CONSTRAINT pk_tb_nave_id_nave 
    PRIMARY KEY(id_nave),

    CONSTRAINT fk_tb_nave_id_fabricante F
    OREIGN KEY(id_fabricante)
    REFERENCES tb_fabricante(id_fabricante)
);