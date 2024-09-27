from itertools import permutations
from flagMap import MAP

class Card:
    def __init__(self, *args):
        self.card = [[-1 for i in range(3)] for j in range(3)]
        self.availableValues = [i for i in  range(1, 10)]
        self.availableSquares = [i for i in range(9)]

        for arg in args:
            self.reveal(arg[0], arg[1])
    
    def reveal(self, square, value):
        x, y = square // 3, square % 3
        if square not in self.availableSquares:
            raise ValueError("Square already revealed")
        if value not in self.availableValues:
            raise ValueError("Value already revealed or out of bounds")
        self.card[x][y] = value
        self.availableValues.remove(value)
        self.availableSquares.remove(square)

        totals = self.probabilitySearch()
        # Print the scratch card with known information
        for i in range(3):
            line = ""
            for j in range(3):
                if self.card[i][j] == -1:
                    line += " "
                else:
                    line += str(self.card[i][j])
                line += " | "
            print(line[:-2])
            if i != 2:
                print("-"*9)
        
        # Print the probabilities
        print(f"""Diagonal 1: {totals[0]}
Column 1: {totals[1]}
Column 2: {totals[2]}
Column 3: {totals[3]}
Diagonal 2: {totals[4]}
Row 1: {totals[5]}
Row 2: {totals[6]}
Row 3: {totals[7]}""")


    def probabilitySearch(self):
        lineTotals = [0, 0, 0, 0, 0, 0, 0, 0]
        counter = 0
        perms = permutations(self.availableValues, len(self.availableSquares))
        for perm in perms:
            for i, square in enumerate(self.availableSquares):
                x, y = square // 3, square % 3
                self.card[x][y] = perm[i]
            totals = self.getLineTotals()
            for i, total in enumerate(totals):
                lineTotals[i] = lineTotals[i] + total
            counter += 1
        
        for i in range(len(lineTotals)):
            lineTotals[i] = lineTotals[i] / counter

        # Reset the card for all non fixed values
        for square in self.availableSquares:
            x, y = square // 3, square % 3
            self.card[x][y] = -1 

        return lineTotals
    
    def new(self):
        self.card = [[-1 for i in range(3)] for j in range(3)]
        self.availableValues = [i for i in  range(1, 10)]
        self.availableSquares = [i for i in range(9)]
    
    def getLineTotals(self):
        totals = []
        totals.append(MAP[self.card[0][0] + self.card[1][1] + self.card[2][2]]) # Diagonal 1
        totals.append(MAP[self.card[0][0] + self.card[1][0] + self.card[2][0]]) # Column 1
        totals.append(MAP[self.card[0][1] + self.card[1][1] + self.card[2][1]]) # Column 2
        totals.append(MAP[self.card[0][2] + self.card[1][2] + self.card[2][2]]) # Column 3
        totals.append(MAP[self.card[0][2] + self.card[1][1] + self.card[2][0]]) # Diagonal 2
        totals.append(MAP[self.card[0][0] + self.card[0][1] + self.card[0][2]]) # Row 1
        totals.append(MAP[self.card[1][0] + self.card[1][1] + self.card[1][2]]) # Row 2
        totals.append(MAP[self.card[2][0] + self.card[2][1] + self.card[2][2]]) # Row 3
        return totals
    
    
