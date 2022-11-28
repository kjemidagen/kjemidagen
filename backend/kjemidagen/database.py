from sqlmodel import Session, create_engine

from kjemidagen.config import Config


user = Config.db_user
password = Config.db_password
host = Config.db_host
port = Config.db_port
name = Config.db_name

DATABASE_URL = f"mysql+mysqldb://{user}:{password}@{host}/{name}"

engine = create_engine(DATABASE_URL)


def get_session():
    with Session(engine) as session:
        yield session
