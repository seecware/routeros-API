from librouteros import connect
import os
from dotenv import load_dotenv

load_dotenv()

def get_api():
    print(os.getenv("MT_USER"))
    return connect(
            username=os.getenv("MT_USER"),
            password=os.getenv("MT_PASS"),
            host=os.getenv("MT_HOST"),
            port=8728,
            timeout=3
            )
