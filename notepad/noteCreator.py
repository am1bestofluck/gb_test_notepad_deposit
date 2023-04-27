
from sqlite3 import Connection,connect


from interface import db_note_saver
from note import Note
from CONSTANTS import BASEPATH

class NoteCreator(db_note_saver):
    def __init__(self, db: Connection, note: Note = None) -> None:
        self.__db = db
        self.__note = Note() if note is None else note

    def save(self):
        print()
        return self.__db


def main():
    root=connect(BASEPATH)
    crs = root.cursor()
    root.close()

if __name__ == "__main__":
    main()