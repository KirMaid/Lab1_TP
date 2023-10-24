from src.Types import DataType
from src.DataReader import DataReader
import yaml

# Определить и вывести на экран студента, имеющего 90
# баллов по всем дисциплинам. Если таких студентов
# несколько, нужно вывести любого из них. Если таких
# студентов нет, необходимо вывести сообщение об их отсутствии.

class YamlDataReader(DataReader):
    def __init__(self) -> None:
        self.key: str = ""
        self.students: DataType = {}

    def read(self, path: str) -> DataType:
        with open(path, encoding='utf-8') as file:
            read_data = yaml.load(file, Loader=yaml.FullLoader)

            for i in range(0, len(read_data)):
                for key, value in read_data[i].items():
                    if value < 90:
                        continue

        return self.students
