import os


def create_dir(path: str) -> int:
    try:
        os.mkdir(path)
        return 201
    except OSError:
        print(f"Creation of the directory: {path} failed!")
        return 500

