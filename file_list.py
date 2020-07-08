import os
from path import PathObject
from file import FileObject

filetype = {
    "txt": "Text",
    "doc": "Text",
    "rtf": "Text",
    "odt": "Text",
    "mp3": "Music",
    "flac": "Music",
    "wav": "Music",
    "mp4": "Video",
    "flv": "Video",
    "mkv": "Video",
    "avi": "Video",
    "webm": "Video",
    "mov": "Video",
    "jpg": "Image",
    "png": "Image",
    "gif": "Image",
    "exe": "Executable"

}

def determine_type(file_name):

    try:
        extension = str(file_name).rsplit('.', 1)[1]
        type = filetype.get(extension, "File")
        return type
    except:
        return "File"


def get_files_folders(path_obj):

    files = []
    folders = []
    path = str(path_obj) + "/"

    file_names = os.listdir(str(path))
    folder_names = []

    for f in file_names:
        if os.path.isdir(str(path) + f):
            folder_names.append(f)

    for dir in folder_names:
        file_names.remove(dir)
        dir_obj = FileObject(dir, 0, "Folder")
        folders.append(dir_obj)

    for f in file_names:
        size = os.stat(str(path) + f).st_size
        type = determine_type(f)
        file_obj = FileObject(f, size, type)
        files.append(file_obj)

    return files, folders
