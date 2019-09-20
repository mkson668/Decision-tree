class DecisionNode:
    def __init__(self, question, tBranch, fBranch):
        self.question = question
        self.trueBranch = tBranch
        self.falseBranch = fBranch