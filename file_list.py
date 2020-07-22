import os
from PathObject import PathObject
from FileObject import FileObject

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
    "jpeg": "Image",
    "png": "Image",
    "gif": "Image",
    "bmp": "Image",
    "tiff": "Image",
    "webp": "Image",
    "exe": "Executable"
}

# determines a file's type, based on its extension
def determine_type(file_name):
    try:
        extension = str(file_name).rsplit('.', 1)[1]
        type = filetype.get(extension, "File")
        return type
    except:
        return "File"


# creates two FileObject lists, containing all the files and
# folders found in the path given as argument
def get_files_folders(path):
    # lists for storing files and folders as FileObjects
    files = []
    folders = []

    # inserts all file and folder names (strings) found in the path into file_names
    file_names = os.listdir(str(path) + "/")
    folder_names = []

    # find all folders from file_names and copy them to folder_names
    for f in file_names:
        if os.path.isdir(str(path) + "/" + f):
            folder_names.append(f)

    # removes folders from file_names and creates a FileObject for each folder
    for dir in folder_names:
        file_names.remove(dir)
        dir_obj = FileObject(dir, 0, "Folder")
        folders.append(dir_obj)

    # creates a FileObject for each file
    for f in file_names:
        size = os.stat(str(path) + "/" + f).st_size
        type = determine_type(f)
        file_obj = FileObject(f, size, type)
        files.append(file_obj)

    return files, folders
