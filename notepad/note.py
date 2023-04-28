from sqlite3 import Cursor, Connection
from datetime import date
from mainTopics import MainTopics
from CONSTANTS import NOTELIMIT,BASEPATH


class Note():

    def __init__(self, topic: MainTopics = None,
                 header: str = None, content: str = None,date_i:date=None) -> None:
        self.__topic = topic if topic is not None else (
            MainTopics.car if input("1 for \"car\", other for driver") == "1"
            else MainTopics.driver)
        self.__header = header.upper() if header is not None\
            else input(
            f'''{"Input car goverment number" if self.__topic
            == MainTopics.car else "Input driver name surname"}'''
            .upper())
        self.__content = content[:NOTELIMIT] if content is not None\
            else input(f"Write down the note please. Less then {str(NOTELIMIT)} characters!")[:NOTELIMIT]
        self.__date = date(date.today().year,
                           date.today().month,
                           date.today().day) if date_i is None else date_i

    def __str__(self) -> str:
        return f"NOTE about {self.__topic.name} {self.__header}"\
            + f" from {self.__date:%d/%m/%Y}:\n\t'{self.__content}'"

    def sqlize(self) -> dict[str, str]:
        return {"topic": self.__topic,
                "date": self.__date,
                "header": self.__header,
                "content": self.__content}

def main():
    a = Note(MainTopics.car, "LCK 777", "26-ого напечатал расторжение")
    print(a)
    print(a.sqlize())


if __name__ == "__main__":
    main()
