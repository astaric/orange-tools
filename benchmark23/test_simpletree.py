from timetest import *

if ORANGE3:
    SimpleTreeLearner = Orange.classification.SimpleTreeLearner
else:
    SimpleTreeLearner = Orange.classification.tree.SimpleTreeLearner

class TestSimpleTree_iris(TimeTest):
    
    def setUp(self):
        self.data = Orange.data.Table("iris.tab")

    def test_simpleTreeUse(self):
        SimpleTreeLearner()(self.data)

class TestSimpleTree_adult(TimeTest):
    
    def setUp(self):
        self.data = Orange.data.Table("adult.tab")

    def test_simpleTreeUse(self):
        SimpleTreeLearner()(self.data)

if __name__ == '__main__':
    unittest.main()
