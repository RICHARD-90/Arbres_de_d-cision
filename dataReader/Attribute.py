class Attribute:
    """
        an attribute is defined by its category and its name.
    """

    def __init__(self, category, name):
        self.category = category
        self.name = name

    def getCategory(self):
        return self.category

    def getName(self):
        return self.name

    def __str__(self):
        return "{category: " + self.getCategory() + " ,Name: " + self.getName() + "}"
