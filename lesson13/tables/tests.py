import unittest

from lesson13.tables.exceptions import TableAlreadyReserved
from lesson13.tables.table_system import Table


class TableTestCase(unittest.TestCase):
    def test_already_reserved_table(self):
        t = Table(111, 2)
        t.reserve(2)
        self.assertRaises(TableAlreadyReserved, Table.reserve, t, 2)



if __name__ == '__main__':
    unittest.main()
