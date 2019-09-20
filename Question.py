import DecisionTree
import numpy as np

class Question:
    def __init__(self, col, val, header):
        # index in row
        self.attribute = col
        # save the reference value we are comparing against
        self.value = val
        self.header = header
    
    def askQuestion(self, row):
        # get the value of at index
        attributeValue = row[self.attribute]
        # we are using numpy so type checking will be different
        if np.issubdtype(attributeValue, np.integer) or np.issubdtype(attributeValue, np.float):
            # check if the row value is greater or = to the reference value
            return attributeValue >= self.value
        else:
            # string case
            return attributeValue == self.value
        
    def __repr__(self):
        attributeValue = self.attribute
        if isinstance(attributeValue, int) or isinstance(attributeValue, float):
            # if number
            return "Is %s %s %s" % (self.header[self.attribute], ">=", self.value)
        else:
            # if string
            return "Is %s %s %s" % (self.header[self.attribute], "==", self.value)
