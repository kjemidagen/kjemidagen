import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    dev = os.getenv("IS_DEV_ENV", "False").lower() in ["true", "1", "t"]
    db_user = os.getenv("DBUser")
    db_password = os.getenv("DBPassword")
    db_host = os.getenv("DBServer")
    db_port = os.getenv("DBPort")
    db_name = os.getenv("DBName")
    access_token_key: str = os.getenv("ACCESS_TOKEN_KEY")  # type: ignore
    refresh_token_key: str = os.getenv("REFRESH_TOKEN_KEY")  # type: ignore
    hash_algorithm = os.getenv("ALGORITHM") or "HS256"


assert Config.access_token_key is not None
assert Config.refresh_token_key is not None
