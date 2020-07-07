class Path_Object:
    def __init__(self, path):
        self.pathtext = path

    def __str__(self):
        return self.pathtext

    def push(self, dir):
        self.pathtext += '/'
        self.pathtext += dir

    def pop(self):
        if "/" not in self.pathtext:
            return
        self.pathtext = self.pathtext.rsplit('/', 1)[0]
