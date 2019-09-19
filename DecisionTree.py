import csv
import numpy as np
import Question

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
        # since we are predicting whether someone is male or female there are only 2 classes
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
            probOfC = allClasses[c]/self.rows
            impurity -= probOfC**2
        return impurity
    
    def findBestSplit(self, rows):
        bestInfoGain = 0
        bestQuestion = None
        # currentGiniUncertainty - weightedAvgGiniUncertainty = infogain
        currentGiniUncertainty = self.giniImpurity(rows)
        # 0,1,2,3...13
        for colIndex in range(self.columns):
            # get all unique column values at current colIndex
            uniqueVals = set([row[colIndex] for row in rows])
            for uniqueVal in uniqueVals:
                quest = Question.Question(colIndex, uniqueVal)
                trueRows, falseRows = self.partition(rows, quest)
                if len(trueRows) == 0 or len(falseRows) == 0:
                    continue
                trueGini = self.giniImpurity(trueRows)
                falseGini = self.giniImpurity(falseRows)
                infoGain = currentGiniUncertainty - (trueGini + falseGini)
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

dT = DecisionTree("heart.csv")
gini = dT.giniImpurity(dT.X)
print("value is " + str(gini))


