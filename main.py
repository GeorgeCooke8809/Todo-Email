import os
from dotenv import load_dotenv

load_dotenv("config.env")

DATABASE_URL = os.getenv("DATABASE_URL")
DEBUGGING_STATE = bool(os.getenv("DEBUGGING"))

import todo

# TODO Add logging and research how to use it across modules

def main():
    print("Hello from todo-email!")


if __name__ == "__main__":
    main()
