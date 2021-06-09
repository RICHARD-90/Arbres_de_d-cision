import pdb
from c4 import C45

c1 = C45("golf.csv", "")
c1.fetchData()
c1.preprocessData()
c1.generateTree()
c1.printTree()