
from sqlite3 import Connection, connect, Cursor
from datetime import date

from interface import db_note_saver
from note import Note
import mainTopics
from CONSTANTS import BASEPATH, REFS, CARNOTES, DRIVERNOTES, NOTELIMIT


class NoteCreator(db_note_saver):
    __notes: list[Note] = []

    def __init__(self, db: Connection) -> None:
        self.__db = db

    def addNote(self, note: Note = None):
        newnote = Note() if note is None else note
        self.__notes.append(newnote)

    def push(self):
        crs = Cursor(self.__db)
        personsTableName = "persons"
        for note in self.__notes:
            tmp = note.sqlize()
            tbl = CARNOTES if tmp['topic'].name == "car" else DRIVERNOTES

            if tbl == CARNOTES:
                extractedId = crs.execute(
                    f"SELECT ID FROM {REFS[tbl]} WHERE GOVPL='{tmp['header']}'")
            else:
                persid = crs.execute(
                    f"SELECT ID FROM {personsTableName} WHERE FULLNAME='{tmp['header']}'")
                persid = crs.fetchone()
                extractedId = crs.execute(
                    f"SELECT ID FROM {REFS[tbl]} WHERE ID={persid[0]}")

            extractedId = crs.fetchone()[0]
            buffer = (
                extractedId,
                date(date.today().year, date.today().month, date.today().day),
                note.sqlize()['content'])
            crs.execute(
                f"INSERT INTO {tbl}(header,today,content) VALUES(?,?,?) ", buffer)
        return self.__db


def main():
    root = connect(BASEPATH)
    noteCar = Note(topic=mainTopics.MainTopics.car,
                   header="LCK 777", content="WE ADD THE NOTE about CAR")
    noteDriver = Note(topic=mainTopics.MainTopics.driver,
                      header="PIT SNAKE", content="WE ADD THE NOTE about PERSON")
    magic = NoteCreator(root)
    magic.addNote(noteCar)
    magic.addNote(noteDriver)
    magic.push()
    root.commit()
    root.close()


if __name__ == "__main__":
    main()
