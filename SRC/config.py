import os

#DATABASE

DB_HOST = "localhost"
DB_PORT = 3306
DB_NAME = "examination"
DB_USER = "root"
DB_PASSWORD = "root123"


#Default path for file 

USERNAME = os.getlogin()

HOME_DIRECTORY = os.path.expanduser("~")

DEFAULT_SEARCH_PATHS = [
    os.path.join(HOME_DIRECTORY, "Desktop"),
    os.path.join(HOME_DIRECTORY, "Documents"),
    os.path.join(HOME_DIRECTORY, "Downloads"),
    HOME_DIRECTORY
]


