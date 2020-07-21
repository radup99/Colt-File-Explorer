import os
from PathObject import PathObject
from file_list import get_files_folders


def display(path, files, folders):
    print(str(path))
    i = 0
    for dir in folders:
        i += 1
        print(f"{i}. {dir}/")
    for f in files:
        i += 1
        print(f"{i}. {f.name} {f.type} {f.size}")


def execute(path):
    try:
        print("Opening file...")
        os.startfile(path)
    except:
        print("Cannot execute file.")


def is_accesible(path, dir):
    path.push(dir)
    if not os.access(str(path), os.R_OK):
        print("Cannot access folder.")
        path.pop()
        return False
    return True


def refresh_list(path, files, folders, fcount, dircount):
    files, folders = get_files_folders(path)
    fcount = len(files)
    dircount = len(folders)
    os.system('cls')
    display(path, files, folders)
    print("")
    return files, folders, fcount, dircount


def main():
    path = PathObject("D:")
    files, folders = get_files_folders(path)
    fcount = len(files)
    dircount = len(folders)
    os.system('cls')
    display(path, files, folders)
    print("")

    while 1:
        com = input("command: ")
        if (com == "back"):
            path.pop()
            files, folders, fcount, dircount = \
            refresh_list(path, files, folders, fcount, dircount)
        else:
            if com.isnumeric():
                i = int(com)
                if i <= dircount:
                    i -= 1
                    dir = folders[i]
                    if is_accesible(path, dir):
                        files, folders, fcount, dircount = \
                        refresh_list(path, files, folders, fcount, dircount)
                elif i <= dircount + fcount:
                    i = i - dircount - 1
                    file = files[i]
                    execute(str(path) + '/' + file.name)


if __name__ == '__main__':
    main()