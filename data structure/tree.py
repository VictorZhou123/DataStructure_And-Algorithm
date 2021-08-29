class Node:
    def __init__(self, name, type = "dir"):
        self.name = name
        self.type = type
        self.children = []
        self.parent = None
    
    def __repr__(self):
        return self.name

class FileSystemTree:
    def __init__(self):
        self.root = Node("/")