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
