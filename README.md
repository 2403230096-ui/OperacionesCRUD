# API de Juegos (Django + MySQL)

## Configuración
1. `pip install -r requirements.txt`
2. Crear la BD: `mysql -u root -p < sql/schema.sql` (o solo `CREATE DATABASE juegos_db;`)
3. Variables de entorno (opcionales): `DB_NAME`, `DB_USER`, `DB_PASSWORD`, `DB_HOST`, `DB_PORT`
4. `python manage.py migrate`
5. `python manage.py runserver`

## Pruebas
- Con MySQL: `python manage.py test` (Django crea y borra `test_juegos_db`; el usuario necesita permiso para crear BD)
- Sin MySQL: `USE_SQLITE=1 python manage.py test`  (PowerShell: `$env:USE_SQLITE=1; python manage.py test`)
