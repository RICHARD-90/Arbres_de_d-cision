# imports
import unittest
import Reader as r
from Set import Set
from ID3Tree import ID3Tree


class TestModel(unittest.TestCase):
    def setUp(self):
        self.file1 = r.Reader("golf.csv")
        self.file2 = r.Reader("soybean-pred.csv")

    def testFileType(self):
        self.assertIsInstance(self.file1, r.Reader)
        self.assertIsInstance(self.file2, r.Reader)

    def testNbAttributesAndClasses(self):
        self.assertEqual(len(self.file1.getAttributes()), 5)
        self.assertEqual(len(self.file2.getAttributes()), 36)

    def testSet(self):
        self.assertIsInstance(self.file1.getSet(), Set)
        self.assertIsInstance(self.file2.getSet(), Set)

    def testEntropyOfTheSet(self):
        self.assertEqual(self.file1.getSet().entropy(), 0.6726994704822977)

    def buildTree(self):
        ID3Tree("golf.csv").buildTree()


if __name__ == '__main__':
    unittest.main()
