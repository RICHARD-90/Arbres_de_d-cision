from ID3Tree import *

learnTree = ID3Tree("soybean-app.csv")
predTree = ID3Tree("soybean-pred.csv")


def bothNodeAreSame(node1, node2, learnTree, predTree):

    if isinstance(node1, Node) and isinstance(node2, Node):
        print("1")
        if node1.getLabel() == node2.getLabel() and len(node1.getChildren()) == len(node2.getChildren()):
            print("2")

            for x in range(len(list(node1.getChildren().items())[::-1])):
                child1 = list(node1.getChildren().items())[::-1][x]
                child2 = list(node2.getChildren().items())[::-1][x]

                print(child1)
                # print(child2)

                print(isElementOf(learnTree.getSet().getAttributes(), node1.getLabel(), child1[0]))
                print(isElementOf(predTree.getSet().getAttributes(), node2.getLabel(), child2[0]))
                if isElementOf(learnTree.getSet().getAttributes(), node1.getLabel(), child1[0]) and isElementOf(
                        predTree.getSet().getAttributes(), node2.getLabel(), child2[0]):
                    print("3")
                    if child1[0] == child2[0]:
                        bothNodeAreSame(child1[1], child2[1], learnTree, predTree)

                    else:
                        print("4")
                        child2[0] = child1[0]
                        print("old value: ", child2[0])
                        print("New value: ", child1[0])
                        print("\n")

    elif isinstance(node1, Leaf) and isinstance(node1, Leaf):
        if node1.getLabel() == node2.getLabel():
            pass
        else:
            node2[0] = node1[0]
            print("old value: ", node2[0])
            print("New value: ", node1[0])
            print("\n")


def prediction(learnTree, predTree):
    bothNodeAreSame(learnTree.getNode1()[0], predTree.getNode1()[0], learnTree, predTree)


if __name__ == '__main__':
    prediction(learnTree, predTree)
