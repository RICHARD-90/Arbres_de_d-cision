from ID3Tree import ID3Tree

tree = ID3Tree("golf.csv")
# tree.buildTree(tree.getSet())

# print(tree.getNode1()[0].getChildren())
# print(tree)
tree.confusionMatrix(tree.getNode1()[0])