-- Equivalente en SQL de lo que hace la API
-- CREATE
INSERT INTO juegos_juego (titulo, plataforma, genero, anio_lanzamiento, completado, calificacion)
VALUES ('Mega Man ZX', 'Nintendo DS', 'Acción', 2006, 0, NULL);

-- READ (lista y detalle)
SELECT * FROM juegos_juego ORDER BY creado_en DESC, id DESC;
SELECT * FROM juegos_juego WHERE id = 1;

-- UPDATE
UPDATE juegos_juego SET completado = 1, calificacion = 9.5 WHERE id = 1;

-- DELETE
DELETE FROM juegos_juego WHERE id = 1;
