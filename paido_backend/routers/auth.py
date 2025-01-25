from http import HTTPStatus

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy import select
from sqlalchemy.orm import Session

from paido_backend.database import get_session
from paido_backend.models import User
from paido_backend.schemas import Token
from paido_backend.security import create_access_token, verify_password

router = APIRouter(prefix='/v1/auth', tags=['auth'])


@router.post('/token', response_model=Token)
def login_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(),
    session: Session = Depends(get_session),
):
    db_user = session.scalar(select(User).where(User.email == form_data.username))

    if not db_user or not verify_password(form_data.password, db_user.password):
        raise HTTPException(
            status_code=HTTPStatus.UNAUTHORIZED,
            detail='Incorrect e-mail or password.',
        )

    access_token = create_access_token(data={'sub': db_user.email})

    return {'access_token': access_token, 'token_type': 'Bearer'}
