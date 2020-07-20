# This class manages the browser's current path
class PathObject:

    def __init__(self, path):
        self.pathtext = path

    def __str__(self):
        return self.pathtext

    def push(self, dir): # adds a folder's name to the end of the path
        self.pathtext += '/'
        self.pathtext += str(dir)

    def pop(self): # removes the current folder from the end of the path
        if "/" not in self.pathtext:
            return
        self.pathtext = self.pathtext.rsplit('/', 1)[0]
