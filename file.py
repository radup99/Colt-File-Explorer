# Object representation of files

class FileObject:

    def __init__(self, name, size, type):
        self.name = name
        self.size = size
        self.type = type

    def __str__(self):
        return self.name
