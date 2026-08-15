import os

from config import DEFAULT_SEARCH_PATHS
from document_reposotry import store_of_all

def normalize_name(name):
    '''
    Normalizes spoken file or folder names.
    '''
    return (
        name.lower()
            .strip()
            .replace(" dot ", ".")
            .replace(" underscore ", "_")
    )

def find_file(file_name):
    '''
    Searches for a file and returns its complete path.
    '''
    try:
        if not file_name:
            return None

        file_name = normalize_name(file_name)

        for search_path in DEFAULT_SEARCH_PATHS:

            if not os.path.exists(search_path):
                continue

            for root, directories, files in os.walk(search_path):

                for file in files:

                    # Exact Match
                    if file.lower() == file_name:
                        return os.path.join(root, file)

                    # Partial Match
                    if file_name in file.lower():
                        return os.path.join(root, file)

        return None

    except Exception as e:
        print(f"Search Error: {e}")
        return None


def open_file_workflow():

    file_name = input(("What is the file name?"))

    if not file_name:
        print("No file name received.")
        return

    print("Searching for the file...")

    file_path = find_file(file_name)

    if file_path:
        print("File found.")
        print(file_path)
        store_of_all(file_path)
        return file_path

    else:
        print("File not found.")

open_file_workflow()