import os.path
from abc import ABC, abstractmethod


class TextFileError(Exception):
    pass

class UnsupportedFileType(TextFileError):
    pass


class TextFile(ABC):

    def __init__(self, file_path: str):
        if not os.path.exists(file_path):
            raise FileNotFoundError()

        _, ext = os.path.splitext(file_path)
        if ext != self.get_file_ext():
            raise UnsupportedFileType()

        self.file_path = file_path

    def get_file_size(self):
        pass


    def get_content(self):
        pass

    @abstractmethod
    def get_file_ext(self):
        pass


class CsvFile(TextFile):

    def __init__(self, file_path: str, delimeter: str = ","):
        super().__init__(file_path)
        self.delimeter = delimeter

    def get_file_ext(self):
        return '.csv'



class JsonFile(TextFile):
    def get_file_ext(self):
        return '.json'


class TxtFile(TextFile):
    def get_file_ext(self):
        return '.txt'


if __name__ == '__main__':
    # my_file = TxtFile('/t/t/y.txt')
    # my_file.get_file_size()
    TextFile('/text_file.py')