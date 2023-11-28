import os

from src.TextDataReader import TextDataReader
from src.YamlDataReader import YamlDataReader


class DataController:
    @staticmethod
    def getDataReader(path: str):
        filename, file_extension = os.path.splitext(path)
        if file_extension == '.yaml':
            return YamlDataReader()
        else:
            return TextDataReader()
