

class Question:
    def __init__(self, col, val):
        self.attribute = col
        self.value = val
    
    def askQuestion(self):
        attributeValue = self.attribute
        if isinstance(attributeValue, int) or isinstance(attributeValue, float):
            return self.attribute >= self.value
        else:
            # string case
            return self.attribute == self.value
        
    def __repr__(self):
        attributeValue = self.attribute
        if isinstance(attributeValue, int) or isinstance(attributeValue, float):
            return "Is %s %s %s" % (self.attribute, ">=", self.value)
        else:
            return "Is %s %s %s" % (self.attribute, "==", self.value)
