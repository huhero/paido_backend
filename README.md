# Paido

## Inicializar aplicacion

- poetry install
- poerty shell
- task run

## Migraciones

generar versiones

`alembic revision --autogenerate -m "create users table"`

Aplicar una Migracion

`alembic upgrade head`



## Herramientas para desarrollo

- Ruff: Un linter y formateador
- Pytest: Para escribir las pruebas
- Taskipy: Para automatizar ciertos comando de nuestra app

# Requirements 

- Poetry (version 1.8.5)
## Crear ambiente virtual:

- `poetry install`

## Agregar librerias

- `poerty add fastapi` 


# Extras
## Comandos Sqlite

Abrir db `sqlite database.d`
mostrar schemas `.schema`
select `SELECT * from [table]`
salir `.quit`