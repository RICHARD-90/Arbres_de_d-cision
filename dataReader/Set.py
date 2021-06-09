# imports
from math import log
from utility import *


class Set:
    """

    """

    def __init__(self, attributes, example):
        self.example = example
        self.attributes = attributes

    def getExample(self):
        return self.example

    def getAttributes(self):
        return self.attributes

    def enumerator(self, name_classe, compared=""):
        """
            allows to count the number of name_value
        """
        count = 0
        if compared == "":
            for value in self.getExample():
                for element in value:
                    if element == name_classe:
                        count += 1
        else:
            for value in self.getExample():
                if (name_classe in value) and (compared in value):
                    count += 1
        return count

    def proportion(self, name_value, bool=True, compared=""):
        """
            returns the proportion of examples of S having the  name_value
        """
        try:
            if bool:
                count = self.enumerator(name_value)
                return count / len(self.getExample())

            else:
                count = self.enumerator(name_value, compared)
                ref_count = self.enumerator(compared)
                return count / ref_count
        except ZeroDivisionError:
            return 0

    def entropy(self):
        """
            returns the Shannon entropy of the set
        """
        list_classe_element = list()
        for attribute in self.getAttributes()[-1][1]:
            list_classe_element.append(attribute)

        entropy = 0
        for value in list_classe_element:
            p = float(self.proportion(value.getName()))
            try:
                entropy = entropy - p * log(p)
            except ValueError:
                entropy = entropy + 0
        return entropy

    def attriEntropy(self, cat_attribute, attri):
        """

        """
        list_class_element = list()
        for attribute in self.getAttributes()[len(self.getAttributes()) - 1][1]:
            list_class_element.append(attribute)

        entropy = 0
        for value in list_class_element:
            p = self.proportion(value.getName(), False, attri)
            try:
                entropy = entropy - p * log(p)
            except ValueError:
                pass
        return entropy

    def attrIsInDataSet(self, attr):
        """
            returns if attr is in data
        """
        for data in self.getExample():
            if attr in data:
                return True
            else:
                return False

    def gain(self, cat_attribute):
        """

        """
        list_attributes = []
        for element in self.getAttributes():
            if element[0] == cat_attribute:
                list_attributes = element[1]

        gain = self.entropy()
        for attr in list_attributes:
            if self.attrIsInDataSet(attr):
                gain += -self.proportion(attr.getName()) * self.attriEntropy(cat_attribute, attr.getName())
        return gain

    def bestAttr(self):
        """
            returns the attribute which has the best gain
        """
        if len(self.getAttributes()) == 1:
            return self.getAttributes()[0][0]
        else:
            maxi = 0
            cat_attr = None
            for attr in ListOfAttributeExceptWord(self.getAttributes()):
                if self.gain(attr[0]) > maxi:
                    maxi = self.gain(attr[0])
                    cat_attr = attr[0]
            return cat_attr
