from http import HTTPStatus

from fastapi import FastAPI

from paido_backend.routers import auth, users

app = FastAPI()

app.include_router(auth.router)
app.include_router(users.router)


@app.get('/ping', status_code=HTTPStatus.OK)
def read_root():
    return {'message': 'pong!'}
