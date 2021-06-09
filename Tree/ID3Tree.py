# imports
import Reader as r
from Node import *
from leaf import *
from utility import *
from Set import Set


class ID3Tree:
    """

    """

    def __init__(self, path=""):
        self.file = r.Reader(path)
        self.list_node = list()
        self.buildTree(self.getSet())
        # self.showTree(self.getNode1()[0])

    def getNode1(self):
        return self.list_node

    def setNode(self, node):
        self.list_node.append(node)

    def getFile(self):
        return self.file

    def getSet(self):
        return self.getFile().getSet()

    def subsetData(self, attrValue, set):
        """
            returns the data of the subset
        """
        liste = list()
        for data in set.getExample():
            if attrValue in data:
                liste.append(data)
        return liste

    def subsetAttri(self, catAttr, set):
        """
            returns the list of attributes of the subset
        """
        liste = list()
        for attr in set.getAttributes():
            if attr[0] == catAttr:
                pass
            else:
                liste.append(attr)
        return liste

    def buildTree(self, set):
        """
            builds the tree
        """
        if len(set.getExample()) == 0:
            raise ValueError("Example cannot be empty")

        if set.entropy() == 0:
            classe_value = set.getExample()[0][-1]
            return Leaf(classe_value)

        if len(ListOfAttributeExceptWord(set.getAttributes())) == 0:
            return Leaf(set.getExample()[0][len(set.getExample()[0]) - 1])

        else:
            best_cat_attr = set.bestAttr()
            node = Node(best_cat_attr)
            self.setNode(node)
            for element in set.getAttributes():
                if element[0] == best_cat_attr:
                    for attr_value in element[1]:
                        if len(self.subsetData(attr_value.getName(), set)) == 0:
                            pass
                        else:
                            subset = Set(self.subsetAttri(best_cat_attr, set),
                                         self.subsetData(attr_value.getName(), set))
                            node.getChildren()[attr_value.getName()] = self.buildTree(subset)

            return node

    def __str__(self):
        self.showTree(self.getNode1()[0])

    def confusionMatrix(self, node, nb=0, liste=[]):
        """
            returns the Confusion matrix
        """

    def showTree(self, node, nb_tabs=0):
        if isinstance(node, Node):
            print('\t' * nb_tabs + node.getLabel() + '\n' + '\t' * nb_tabs + "|")
            copy_nb_tabs = nb_tabs
            for child in list(node.getChildren().items())[::-1]:
                if isElementOf(self.getSet().getAttributes(), node.getLabel(), child[0]):
                    print('\t' * nb_tabs + str(child[0]) + '\n' + '\t' * nb_tabs + "|")

                    self.showTree(child[1], nb_tabs + 1)

        elif isinstance(node, Leaf):
            print('\t' * nb_tabs + "--> " + node.getLabel() + "\n")
        else:
            raise TypeError("node must be a Node / Leaf and not a {}".format(type(node)))
