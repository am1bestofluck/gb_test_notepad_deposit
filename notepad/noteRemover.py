

from sqlite3 import Connection
from CONSTANTS import BASEPATH

from interface import db_note_remover
from noteSelector import Note_selector

class NoteRemover(db_note_remover):
    def __init__(self,base:Connection):
        self.__base=base
    
    def remove(self):
        selector = Note_selector(self.__base)
        return self.base


def main():
    a = Connection(BASEPATH)
    b = NoteRemover(a)
    


if __name__=="__main__":
    main()