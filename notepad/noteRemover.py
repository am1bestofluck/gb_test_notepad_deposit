

from sqlite3 import Connection,Cursor
from CONSTANTS import BASEPATH

from interface import db_note_remover
from noteSelector import Note_selector

class NoteRemover(db_note_remover):
    def __init__(self,base:Connection):
        self.__base=base
    
    def remove(self):
        selector = Note_selector(self.__base)
        pick = selector.selectNote()
        crs = Cursor(self.__base)
        crs.execute(f"DELETE FROM {pick[0]} WHERE ID='{pick[2]}';")
        return self.__base


def main():
    a = Connection(BASEPATH)
    b = NoteRemover(a)
    b.remove()
    a.commit()
    a.close()
    


if __name__=="__main__":
    main()