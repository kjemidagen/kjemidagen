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
