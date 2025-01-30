import unittest
from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_rows,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_cols,
        )

    def test_maze_create_cells_break_start_end(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_rows,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_cols,
        )

        self.assertFalse(m1._cells[0][0].has_top_wall)
        self.assertFalse(m1._cells[m1.num_rows-1][m1.num_cols-1].has_bottom_wall)


    def test_maze_create_cells_reset_visited(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_rows,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_cols,
        )

        self.assertFalse(m1._cells[0][0]._visited)
        self.assertFalse(m1._cells[m1.num_rows-1][m1.num_cols-1]._visited)

if __name__ == "__main__":
    unittest.main()