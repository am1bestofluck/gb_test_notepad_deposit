from sqlite3 import Connection,Cursor,OperationalError

from interface import dbMain
from noteCreator import NoteCreator
from noteEditor import NoteEditor
from noteRemover import NoteRemover
from noteReader import NoteReader
from note import Note
from CONSTANTS import BASEPATH,CARNOTES,DRIVERNOTES,REFS,NOTELIMIT
import mainTopics

class DbBridge(dbMain):
    
    def __init__(self):
        self.__base = BASEPATH

    def _purge_notepad(self) -> None:
        # на случай сброса базы, пересоздаём ту часть которая отвечает за блокнот
        separator=", "
        base = Connection(self.__base)
        crs = Cursor(base)
        try:
            crs.execute(f"DROP TABLE {CARNOTES}")
        except OperationalError:
            print( "No car notes table found. First run?")
        try:
            crs.execute(f"DROP TABLE {DRIVERNOTES}")
        except OperationalError:
            print( "no driver notes table found. First run?")
        
        crs.execute(f"CREATE TABLE {CARNOTES} (" +separator.join([
                    "id integer primary key AUTOINCREMENT"
                    , "header integer"
                    , "today DATE"
                    , f"content varchar({str(NOTELIMIT)}) NOT NULL"
                    , f"FOREIGN KEY (header) REFERENCES {REFS[CARNOTES]}(ID)"])\
                    .strip(separator)+");")
        crs.execute(f"CREATE TABLE {DRIVERNOTES} (" +separator.join([
                    "id integer primary key AUTOINCREMENT"
                    , "header integer"
                    , "today DATE"
                    , f"content varchar({str(NOTELIMIT)}) NOT NULL"
                    , f"FOREIGN KEY (header) REFERENCES {REFS[DRIVERNOTES]}(ID)"])\
                    .strip(separator)+");")
            
        base.commit()
        base.close()
        return
    
    def _dbMain__addCarNote(self):
       print("obsolete")
       return # при проектировании думал что заметки будут разные для машин
    # и водителей, но сделал один конструктор
    
    def  _dbMain__addDriverNote(self):
        print("obsolete")
        return # при проектировании думал что заметки будут разные для машин
    # и водителей, но сделал один конструктор
    
    def _dbMain__connection(self):
        # отказался от этого
        raise NotImplementedError("todo")
    
    def _dbMain__editCarNote(self):
        print("obsolete")
        return # при проектировании думал что заметки будут разные для машин
    # и водителей, но сделал один конструктор
    
    def _dbMain__editDriverNote(self):
        print("obsolete")
        return # при проектировании думал что заметки будут разные для машин
    # и водителей, но сделал один конструктор
    
    def _dbMain__removeCarNote(self):
        print("obsolete")
        return # при проектировании думал что заметки будут разные для машин
    # и водителей, но сделал один конструктор
    
    def _dbMain__removeDriverNote(self):
        print("obsolete")
        return # при проектировании думал что заметки будут разные для машин
    # и водителей, но сделал один конструктор
    
    def addNote(self):
        root = Connection(self.__base)
        newNote=Note()
        magic = NoteCreator(root)
        magic.addNote(newNote)
        root=magic.push()
        root.commit()
        root.close()
    
    def editNote(self):
        q=Connection(BASEPATH)
        a=NoteEditor(q)
        q=a.editNoteContent()
        q.commit()
        q.close()
    
    def removeNote(self):
        a = Connection(BASEPATH)
        b = NoteRemover(a)
        b.remove()
        a.commit()
        a.close()

    def readAllNotes(self):
        a=Connection(BASEPATH)
        b=NoteReader(a)
        b.readall()
        a.close()
    def readNote(self):
        a=Connection(BASEPATH)
        b=NoteReader(a)
        b.readSpecific()
        a.close()
    
    
def main():
    a = DbBridge()
    # a._purge_notepad()
    # a.addNote()
    # a.editNote()
    # a.removeNote()
    a.readNote()
    a.readAllNotes()

if __name__ == "__main__":
    main()