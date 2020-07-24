# This class manages the browser's current path
class PathObject:

    def __init__(self, path):
        self.pathtext = path

    def __str__(self):
        return self.pathtext

    def set(self, text):
        self.pathtext = text

    def add(self, dir):  # adds a folder's name to the end of the path
        self.pathtext += '/'
        self.pathtext += str(dir)

    def back(self):  # removes the current folder from the end of the path
        if "/" not in self.pathtext:
            return
        dir = self.pathtext.rsplit('/', 1)[1]
        self.pathtext = self.pathtext.rsplit('/', 1)[0]
        return dir

    def is_root(self):
        if "/" not in self.pathtext:
            return True
        return False
