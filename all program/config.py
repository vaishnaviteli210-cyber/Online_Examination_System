import os

import os

DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = int(os.getenv("DB_PORT", "3306"))
DB_NAME = os.getenv("DB_NAME", "examination")
DB_USER = os.getenv("DB_USER", "root")
DB_PASSWORD = os.getenv("DB_PASSWORD", "root123")

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

#Default path for file 

USERNAME = os.getlogin()

HOME_DIRECTORY = os.path.expanduser("~")

DEFAULT_SEARCH_PATHS = [
    os.path.join(HOME_DIRECTORY, "Desktop"),
    os.path.join(HOME_DIRECTORY, "Documents"),
    os.path.join(HOME_DIRECTORY, "Downloads"),
    HOME_DIRECTORY
]


