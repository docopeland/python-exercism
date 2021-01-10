class Matrix:
    def __init__(self, matrix_string):
        self.matrix = matrix_string.split("\n")

    def row(self, index):
        return [int(num) for i in range(len(self.matrix)) if i+1 is index for num in self.matrix[i].split(" ")]

    def column(self, index):
        return [int(self.matrix[row].split(" ")[index-1]) for row in range(len(self.matrix))]