class linear_sys:
    
    def __init__(self, matrix):
        self.matrix = matrix
    
    def __str__(self):
        ret = ""
        count = 0
        for i in self.matrix:
            ret = ret + str(count) + ': ' + str(i) + '\n'
            count = count + 1
        return ret
    
    def row_interchange(self, row_index_a, row_index_b):
        """x = Ra; Ra = Rb; Rb = x"""
        z = row_index_a < len(matrix)
        y = row_index_b < len(matrix)
        x = row_index_a >= 0
        w = row_index_b >= 0
        if not (z and y and x and w):
            raise Exception("Index out of bounds in row_interchange call.")
        a = self.matrix[row_index_a]
        b = self.matrix[row_index_b]
        self.matrix[row_index_a] = b
        self.matrix[row_index_b] = a
    
    def row_mult(self, row_index, scalar):
        """Ra = s * Ra"""
        if scalar == 0:
            raise Exception("Multiply by zero in row_mult call.")
        for i in range(len(self.matrix[row_index])):
            x = self.matrix[row_index][i]
            x = x * scalar
            self.matrix[row_index][i] = x
    
    def row_add_mult(self, row_index_a, row_index_b, scalar=1):
        """Ra = (s * Rb) + Ra"""
        for i in range(len(self.matrix[row_index_b])):
            x = self.matrix[row_index_a][i]
            x = (scalar * self.matrix[row_index_b][i]) + x
            self.matrix[row_index_a][i] = x
    
    def row_echelon(self, row_index):
        first_nonzero = 0
        for i in self.matrix[row_index]:
            if i != 0
                first_nonzero = i
                break
        if first_nonzero != 0:
            scalar = 1 / first_nonzero
            self.row_mult(row_index, scalar)
    
