import os
from path import PathObject
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
            if com.isnumeric() and int(com) <= dircount:
                i = int(com) - 1
                dir = folders[i]
                path.push(dir)
                files, folders, fcount, dircount = \
                refresh_list(path, files, folders, fcount, dircount)
            elif int(com) <= dircount + fcount:
                i = int(com) - dircount - 1
                file = files[i]
                execute(str(path) + '/' + file.name)


if __name__ == '__main__':
    main()