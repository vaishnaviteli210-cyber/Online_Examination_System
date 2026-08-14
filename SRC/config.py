import os

import os

DB_HOST = "localhost"
DB_PORT = 3306
DB_NAME = "examination"
DB_USER = "root"
DB_PASSWORD = "root123"

<<<<<<< Updated upstream

#Default path for file 

=======
>>>>>>> Stashed changes
USERNAME = os.getlogin()

HOME_DIRECTORY = os.path.expanduser("~")

DEFAULT_SEARCH_PATHS = [
    os.path.join(HOME_DIRECTORY, "Desktop"),
    os.path.join(HOME_DIRECTORY, "Documents"),
    os.path.join(HOME_DIRECTORY, "Downloads"),
    HOME_DIRECTORY
<<<<<<< Updated upstream
]


=======
]
>>>>>>> Stashed changes
