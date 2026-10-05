-- Base de datos y tabla para la entidad Juego (MySQL 8+)
CREATE DATABASE IF NOT EXISTS juegos_db
  CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE juegos_db;

CREATE TABLE IF NOT EXISTS juegos_juego (
  id               BIGINT AUTO_INCREMENT PRIMARY KEY,
  titulo           VARCHAR(150) NOT NULL,
  plataforma       VARCHAR(60)  NOT NULL,
  genero           VARCHAR(60)  NOT NULL DEFAULT '',
  anio_lanzamiento SMALLINT UNSIGNED NOT NULL,
  completado       TINYINT(1)   NOT NULL DEFAULT 0,
  calificacion     DECIMAL(3,1) NULL,
  creado_en        DATETIME(6)  NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
  CONSTRAINT chk_anio  CHECK (anio_lanzamiento BETWEEN 1950 AND 2100),
  CONSTRAINT chk_calif CHECK (calificacion IS NULL OR calificacion BETWEEN 0 AND 10)
) ENGINE=InnoDB;
