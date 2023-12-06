import argparse
import sys

from src.CalcRating import CalcRating
from src.DataController import DataController


def get_path_from_arguments(args) -> str:
    parser = argparse.ArgumentParser(description="Path to datafile")
    parser.add_argument("-p", dest="path", type=str, required=True,
                        help="Path to datafile")
    args = parser.parse_args(args)
    return args.path


def main():
    path = get_path_from_arguments(sys.argv[1:])
    reader = DataController.getDataReader(path)
    students = reader.read(path)
    if not students:
        print("Таких студентов нет")
    else:
        print("Students: ", students)
        rating = CalcRating(students).calc()
        print("Rating: ", rating)


if __name__ == "__main__":
    main()
