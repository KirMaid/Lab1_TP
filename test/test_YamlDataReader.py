import pytest
from src.Types import DataType
from src.YamlDataReader import YamlDataReader


class TestYamlTextDataReader:
    @pytest.fixture()
    def file_and_data_content(self) -> tuple[str, DataType]:
        text = "Иванов Константин Дмитриевич:\n" + \
               "  математика: 90\n" + "  химия: 90\n" + \
               "Петров Петр Семенович:\n" + \
               "  русский язык: 89\n" + "  литература: 90\n"
        data = {
            "Иванов Константин Дмитриевич": [
                ("математика", 90), ("химия", 90)
            ],
        }
        return text, data

    @pytest.fixture()
    def file_and_data_content_empty(self) -> tuple[str, DataType]:
        text = ""
        data = {}
        return text, data

    @pytest.fixture()
    def file_and_data_content_many(self) -> tuple[str, DataType]:
        text = "Петров Петр Семенович:\n" + \
               "  математика: 90\n" + "  химия: 90\n" + \
               "Иванов Константин Дмитриевич:\n" + \
               "  русский язык: 90\n" + "  литература: 90\n"
        data = {
            "Петров Петр Семенович": [
                ("математика", 90), ("химия", 90)
            ]
        }
        return text, data

    @pytest.fixture()
    def file_and_data_content_nobody(self) -> tuple[str, DataType]:
        text = "Иванов Константин Дмитриевич:\n" + \
               "  математика: 70\n" + "  химия: 60\n" + \
               "Петров Петр Семенович:\n" + \
               "  русский язык: 70\n" + "  литература: 50\n"
        data = {
        }
        return text, data

    @pytest.fixture()
    def filepath_and_data(self,
                          file_and_data_content: tuple[str, DataType],
                          tmpdir) -> tuple[str, DataType]:
        p = tmpdir.mkdir("datadir").join("my_data.yaml")
        p.write_text(file_and_data_content[0], encoding='utf-8')
        return str(p), file_and_data_content[1]

    @pytest.fixture()
    def filepath_and_data_nobody(self,
                                 file_and_data_content_nobody: tuple[
                                     str, DataType],
                                 tmpdir) -> tuple[str, DataType]:
        p = tmpdir.mkdir("datadir").join("my_data_nobody.yaml")
        p.write_text(file_and_data_content_nobody[0], encoding='utf-8')
        return str(p), file_and_data_content_nobody[1]

    @pytest.fixture()
    def filepath_and_data_many(self,
                               file_and_data_content_many: tuple[
                                   str, DataType],
                               tmpdir) -> tuple[str, DataType]:
        p = tmpdir.mkdir("datadir").join("my_data_many.yaml")
        p.write_text(file_and_data_content_many[0], encoding='utf-8')
        return str(p), file_and_data_content_many[1]

    def test_read(self, filepath_and_data: tuple[str, DataType]) -> None:
        file_content = YamlDataReader().read(filepath_and_data[0])
        assert file_content == filepath_and_data[1]

    def test_read_nobody(self, filepath_and_data_nobody: tuple[
            str, DataType]) -> None:
        file_content = YamlDataReader().read(filepath_and_data_nobody[0])
        assert file_content == filepath_and_data_nobody[1]

    def test_read_many(self, filepath_and_data_many: tuple[
            str, DataType]) -> None:
        file_content = YamlDataReader().read(filepath_and_data_many[0])
        assert file_content == filepath_and_data_many[1]
