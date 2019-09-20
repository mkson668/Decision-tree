class Leaf:
    def __init__(self, rows):
        self.rows = rows
        count = 0
        colIndex = None
        allClasses = {}
        # tally up counts of female and male (male = 1, female = 0)
        for row in rows:
            # label vector y will be column 1 in heart.csv
            classVal = row[1]
            if classVal not in allClasses:
                allClasses[classVal] = 1
            else:
                allClasses[classVal] += 1
        for c in allClasses:
            if allClasses[c] > count:
                count = allClasses[c]
                colIndex = c
        self.predition = colIndex

