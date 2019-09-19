

class Question:
    def __init__(self, col, val):
        # index in row
        self.attribute = col
        # save the reference value we are comparing against
        self.value = val
    
    def askQuestion(self, row):
        # get the value of at index
        attributeValue = row[self.attribute]
        if isinstance(attributeValue, int) or isinstance(attributeValue, float):
            # check if the row value is greater or = to the reference value
            return self.attribute >= self.value
        else:
            # string case
            return self.attribute == self.value
        
    def __repr__(self):
        attributeValue = self.attribute
        if isinstance(attributeValue, int) or isinstance(attributeValue, float):
            # if number
            return "Is %s %s %s" % (self.attribute, ">=", self.value)
        else:
            # if string
            return "Is %s %s %s" % (self.attribute, "==", self.value)
