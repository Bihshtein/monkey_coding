import unittest


class Matrix:
    def __init__(self, rows, cols, field):
        self.rows = rows
        self.cols = cols
        self.field = field

    def validate(self, new_i, new_j, visited_spots):
        return new_j < self.rows and \
               new_i < self.cols and \
               new_j >= 0 and\
               new_i >= 0 and \
               self.field[new_i][new_j] and\
               not visited_spots[new_i][new_j]

    def mark_connected_spots(self, i, j, visited_spots):
        col_neighbour = [0, 0, 1, -1, -1, -1, 1, 1]
        row_neighbour = [1, -1, 1, -1, 0, 1, -1, 0]
        visited_spots[i][j] = True
        for t in range(8):
            if self.validate(i + col_neighbour[t], j + row_neighbour[t], visited_spots):
                self.mark_connected_spots(i + col_neighbour[t], j + row_neighbour[t], visited_spots)
        return

    def get_islands_number(self):
        islands = 0
        visited_spots = [[False for i in range(self.cols)] for j in range(self.rows)]
        for i in range(self.cols):
            for j in range(self.rows):
                if self.field[i][j] == 1 and not visited_spots[i][j]:
                    self.mark_connected_spots(i,j,visited_spots)
                    islands += 1

        return islands


class Tests(unittest.TestCase):
    def test1(self):
        rows = 5
        cols = 5
        field =   [[1, 1, 0, 0, 0],
                   [0, 1, 0, 0, 1],
                   [1, 0, 0, 1, 1],
                   [0, 0, 0, 0, 0],
                   [1, 0, 1, 0, 1]]
        matrix = Matrix(rows, cols, field)
        self.assertEqual(5, matrix.get_islands_number())
