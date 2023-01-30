import unittest

from lesson12.unittests_example.table import Table

class TableTestCase(unittest.TestCase):

    def setUp(self) -> None:
        print("setup")
        self.table = Table(11, 4)

    def test_reserve_table(self):
        self.table.reserve(2)
        self.assertFalse(self.table.is_available())
        self.assertEqual(self.table.occupied_seats, 2)

    def test_release_table(self):
        self.table.reserve(2)
        self.table.release()
        self.assertTrue(self.table.is_available())
        self.assertEqual(self.table.occupied_seats, 0)

    def tearDown(self) -> None:
        pass


if __name__ == '__main__':
    unittest.main()
