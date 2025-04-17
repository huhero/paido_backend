# paido_backend


# Poetry commands

create new project.

`poetry new [name project]`


init project.

`poetry install`

install dependences

`poetry add [name]`

init virtual enviroment

`eval $(poetry env activate)`


# FastAPI commands

Init dev server

`fastapi dev src/paido_core/app.py`


# Tasks

lint: revisar buenas practicas de codigo

`task lint`

pre_format: correciones de buenas practicas

`task pre_format`

format: ejecuta formato en el codigo segun las convenciones en el toml

`task format`

run: ejecuta servidor de desarrollo FastAPI

`task run`

pre_test: ejecuta linter antes de los test

`task pre_test`

test: ejecuta los tests

`task test`

post_test: genera reporte de coverage

`task post_test`