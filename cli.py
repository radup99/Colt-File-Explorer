import os
from path import Path_Object
from file_list import get_files_folders


def display(path, files, folders):
    print(str(path))
    i = 0

    for dir in folders:
        i += 1
        print(f"{i}.{dir}")

    for f in files:
        i += 1
        print(f)


def main():
    path = Path_Object("D:")
    files, folders = get_files_folders(path)

    while 1:
        os.system('cls')
        fcount = len(files)
        dircount = len(folders)
        display(path, files, folders)

        com = input("Command: ")
        if (com == "back"):
            path.pop()
            files, folders = get_files_folders(path)
        else:
            if com.isnumeric() and int(com) <= dircount:
                i = int(com) - 1
                dir = folders[i]
                path.push(dir)
                files, folders = get_files_folders(path)


if __name__ == '__main__':
    main()