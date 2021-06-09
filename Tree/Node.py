class Node:

    def __init__(self, label, children={}):
        self.label = label
        self.children = children

    def getLabel(self):
        return self.label

    def getChildren(self):
        return self.children
