from sqlalchemy import select

from paido_backend.models import User


def test_created_user(session):
    # engine = create_engine('sqlite:///:memory:')

    # table_registry.metadata.create_all(engine)

    # with Session(engine) as session:
    user = User(username='hugo', email='hola@hola.com', password='segura')

    session.add(user)
    session.commit()
    session.refresh(user)

    result = session.scalar(select(User).where(User.email == 'hola@hola.com'))

    assert result.username == 'hugo'
