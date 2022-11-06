class Matrix:
    def __init__(self, matrix_str):
        self.matrix = list(map(lambda x: list(map(int, x.split(' '))), matrix_str.split('\n')))

    def row(self, index):
        return self.matrix[index-1]

    def column(self, index):
        transposed = list(zip(*self.matrix))
        return list(transposed[index-1])
