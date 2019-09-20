import csv
import numpy as np
import Question as qst
import Leaf as lf
import DecisionNode as dn

class DecisionTree:

    # read csv file and store dimensions
    def __init__(self, file):
        mat = np.genfromtxt(file,dtype=int, skip_header=1, delimiter=",", autostrip=True, case_sensitive=False)
        # get header
        self.header = np.genfromtxt(file,dtype=str,delimiter=",", autostrip=True, max_rows=1)
        # header remove
        self.header[0] = "age"
        self.X = mat
        dims = mat.shape
        self.rows = dims[0]
        self.columns = dims[1]
        # need to split for training and validation on self.X

    # gini impurity in a nutshell is the probaility of predicting the wrong class in subset vector y (random chance)
    def giniImpurity(self, X):
        # since we are predicting whether someone is male or female there are only 2 classes use a simple dictonary
        allClasses = {}
        # tally up counts of female and male (male = 1, female = 0)
        for row in X:
            # label vector y will be column 1 in heart.csv
            classVal = row[1]
            if classVal not in allClasses:
                allClasses[classVal] = 1
            else:
                allClasses[classVal] += 1
        # wikipedia gini impurity formula 
        impurity = 1
        for c in allClasses:
            probOfC = allClasses[c]/len(X)
            impurity -= probOfC**2
        return impurity
    
    def findBestSplit(self, rows):
        bestInfoGain = 0
        bestQuestion = None
        # parentCurrentGiniUncertainty - childrenWeightedAvgGiniUncertainty = infogain
        currentGiniUncertainty = self.giniImpurity(rows)
        # 0,1,2,3...13
        for colIndex in range(self.columns):
            # this is the label vector dont want to split on this or we get no uncertainty
            if colIndex == 1:
                continue
            # get all unique column values at current colIndex
            uniqueVals = set([row[colIndex] for row in rows])
            for uniqueVal in uniqueVals:
                quest = qst.Question(colIndex, uniqueVal, self.header)
                trueRows, falseRows = self.partition(rows, quest)
                # if this occurs then the column value we used to split on was probably shit or it has reached a leaf node
                if len(trueRows) == 0 or len(falseRows) == 0:
                    continue
                trueGini = self.giniImpurity(trueRows)
                falseGini = self.giniImpurity(falseRows)
                trueWeightedRatio = len(trueRows)/(len(trueRows) + len(falseRows))
                falseWeightedRation = 1 - trueWeightedRatio
                # currentGiniUncertainty - weightedAvgGiniUncertainty = infogain
                infoGain = currentGiniUncertainty - (trueWeightedRatio * trueGini + falseWeightedRation * falseGini)
                if infoGain > bestInfoGain:
                    bestInfoGain = infoGain
                    bestQuestion = quest
        return bestInfoGain, bestQuestion

    # split on dataset
    def partition(self, allRows, question):
        true, false = [], []
        for row in allRows:
            if question.askQuestion(row):
                true.append(row)
            else:
                false.append(row)
        return true, false

    def constructTree(self, rows):
        # for this set of example find the best split 
        bestInfoGain, bestQuestion = self.findBestSplit(rows)
        # this means that only one class remains or 
        if bestInfoGain == 0:
            return lf.Leaf(rows)
        trueSplit, falseSplit = self.partition(rows, bestQuestion)
        # append true and false childnodes
        trueChild = self.constructTree(trueSplit)
        falseChild = self.constructTree(falseSplit)
        return dn.DecisionNode(bestQuestion, trueChild, falseChild)

    def classify(self, row, node):
        print(isinstance(node, dn.DecisionNode))
        if isinstance(node, lf.Leaf):
            return node.prediction
        if node.question.askQuestion(row):
            return self.classify(row, node.trueBranch)
        else:
            return self.classify(row, node.falseBranch)

dTree = DecisionTree("heart.csv")
# should actually split this into training validation and test set
# for now just make sure it works properly
trainedTreeRoot = dTree.constructTree(dTree.X)
mat = dTree.X
label = dTree.classify(mat[0], trainedTreeRoot)
if (label == 1):
    print("male")
else:
    print("female")



        


        





