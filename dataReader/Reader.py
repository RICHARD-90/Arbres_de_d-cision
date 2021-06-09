# import
from Attribute import Attribute
from Classe import Classe
from Set import Set
import csv


class Reader:
    """
    Reading Sapp
        - name of the different attributes,
        - list of possible values for each attribute,
        - data.
    """

    def __init__(self, file=""):
        self.file = file
        # initialization in empty lists
        self.attributes = list()
        self.data = list()
        self.set = None
        # read the file
        self.fileReader()

    def setFile(self, newFile):
        self.file = newFile

    def getFile(self):
        return self.file

    def setAttributes(self):
        list_test = []
        for index in range(len(self.getData()[0])):
            list_test.append([self.getData()[0][index], []])
            self.getAttributes().append([self.getData()[0][index], []])

        line_count = 0
        for value in self.getData():
            if line_count == 0:
                pass
                line_count += 1
            else:

                for value_index in range(len(value)):
                    if value[value_index] not in list_test[value_index][1]:
                        list_test[value_index][1].append(value[value_index])

                        if value_index == len(value) - 1:
                            object_class = Classe(self.getAttributes()[value_index][0], value[value_index])
                            self.getAttributes()[value_index][1].append(object_class)
                        else:
                            object_attribute = Attribute(self.getAttributes()[value_index][0], value[value_index])
                            self.getAttributes()[value_index][1].append(object_attribute)

    def getSet(self):
        return self.set

    def getAttributes(self):
        return self.attributes

    def setData(self, list_data):
        self.data.append(list_data)

    def getData(self):
        return self.data

    def fileReader(self):
        file = self.getFile()

        if not isinstance(file, str):
            raise TypeError("path must be str and not {}".format(type(file)))

        else:
            with open(file, 'r') as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=",", quotechar='|')
                for row in csv_reader:
                    self.setData(row)
                self.setAttributes()

        self.set = Set(self.getAttributes(), self.getData())
