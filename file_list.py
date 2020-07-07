import os
from path import Path_Object


def get_files_folders(path_obj):

    path = str(path_obj) + "/"

    files = os.listdir(str(path))
    folders = []

    for f in files:
        if os.path.isdir(str(path) + f):
            folders.append(f)

    for f in folders:
        files.remove(f)

    return files, folders


def show(path_obj):

    files, folders = get_files_folders(path_obj)
    i = 0

    print(str(path_obj), '\n')

    for dir in folders:
        i += 1
        print(f"{i}. >{dir}")

    for f in files:
        i += 1
        print(f"{i}. {f}")
