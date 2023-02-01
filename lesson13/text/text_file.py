import csv
import json
import os.path
from abc import ABC, abstractmethod
from io import TextIOWrapper


class TextFileError(Exception):
    pass

class UnsupportedFileType(TextFileError):
    pass


class TextFile(ABC):

    def __init__(self, file_path: str):
        if not os.path.exists(file_path):
            raise FileNotFoundError()

        _, ext = os.path.splitext(file_path)
        # if ext not in ('txt', '.json', '.csv'):
        if ext != self.get_file_ext():
            raise UnsupportedFileType()

        self._file_path = file_path

    def get_file_size(self):
        return os.path.getsize(self._file_path)

    def get_content(self):
        with open(self._file_path, 'r') as f:
            ret_val = self._read_file_content(f)
        return ret_val

    @abstractmethod
    def _read_file_content(self, f: TextIOWrapper):
        raise NotImplementedError()

    @abstractmethod
    def get_file_ext(self):
        raise NotImplementedError()


class CsvFile(TextFile):

    def __init__(self, file_path: str, delimiter: str = ","):
        super().__init__(file_path)
        self._delimiter = delimiter

    def _read_file_content(self, f: TextIOWrapper):
        return list(csv.DictReader(f, delimiter=self._delimiter))

    def get_file_ext(self):
        return '.csv'


class JsonFile(TextFile):

    def _read_file_content(self, f: TextIOWrapper):
        return json.load(f)

    def get_file_ext(self):
        return '.json'


class TxtFile(TextFile):

    def _read_file_content(self, f: TextIOWrapper):
        return f.read()

    def get_file_ext(self):
        return '.txt'



if __name__ == '__main__':
    # my_file = TxtFile('/t/t/y.txt')
    # my_file.get_file_size()
    txt_file = TxtFile('/Users/valeria/src/evening-ninjas/lesson12/files/data/alice_in_wonderland.txt')
    csv_file = CsvFile('/Users/valeria/src/evening-ninjas/lesson12/files/data/AAPL.csv')
    json_file = JsonFile('/Users/valeria/src/evening-ninjas/lesson12/files/data/example_2.json')

    # txt_file + csv_file
    # txt_file + json_file
    # t1 = '/a/b/my.txt'
    # t2 = 'c/d/sun.txt'
    # new_f = t1 + t2 # /a/b/my_sun.txt
    # # csv_file + json_file
    # txt_file + txt_file #
    # csv_file + csv_file
    # a, b, c
    # b, a, c, d
    #

    # for i in (t, c, j):
    #     print(i.get_content())