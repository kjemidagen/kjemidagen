import os
from dotenv import load_dotenv

load_dotenv()
dev = os.getenv("IS_DEV_ENV", "False").lower() in ["true", "1", "t"]
