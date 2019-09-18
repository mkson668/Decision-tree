import csv
import numpy as np
import Question

class DecisionTree:

    # read csv file and store dimensions
    def __init__(self, file):
        mat = np.genfromtxt(file,dtype=None, skip_header=1, delimiter=",", autostrip=True, case_sensitive=False)
        # get header
        self.header = np.genfromtxt(file,dtype=str,delimiter=",", autostrip=True, max_rows=1)
        # header remove
        self.header[0] = "age"
        self.header[2] = "chest pain type"
        self.header[3] = "resting blood pressure"
        
        np.delete(mat, 0, axis=0) 
       
        self.X = mat
        dims = mat.shape
        self.rows = dims[0]
        self.columns = dims[1]

    # gini impurity in a nutshell is the probaility of predicting the wrong class in subset vector y (random chance)
    def giniImpurity(self, X):
        # since we are predicting whether someone has recieved treatment (yes/no) there are only 2 classes
        allClasses = {}
        # tally up counts of yes and no
        for row in X:
            # vector y will be column 7 in survey.csv
            classVal = row[7]
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
    
    # split on dataset
    def partition(self, question):
        true, false = [], []
        for row in self.X:
            if question.askQuestion:
                true.append(row)
            else:
                false.append(row)
        return true, false
    
dT = DecisionTree("heart.csv")
gini = dT.giniImpurity(dT.X)
print("value is " + str(gini))


