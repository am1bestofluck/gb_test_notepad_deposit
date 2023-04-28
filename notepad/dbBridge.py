from sqlite3 import Connection,Cursor,OperationalError

from interface import dbMain
from CONSTANTS import BASEPATH,CARNOTES,DRIVERNOTES,REFS,NOTELIMIT
import mainTopics

class DbBridge(dbMain):
    
    def __init__(self):
        self.__base = BASEPATH
    def _purge_notepad(self) -> None:
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
        raise NotImplementedError("todo")
    
    def  _dbMain__addDriverNote(self):
        raise NotImplementedError("todo")
    
    def _dbMain__connection(self):
        raise NotImplementedError("todo")
    
    def _dbMain__editCarNote(self):
        raise NotImplementedError("todo")
    
    def _dbMain__editDriverNote(self):
        raise NotImplementedError("todo")
    
    def _dbMain__removeCarNote(self):
        raise NotImplementedError("todo")
    
    def _dbMain__removeDriverNote(self):
        raise NotImplementedError("todo")
    
    def addNote(self):
        raise NotImplementedError("todo")
    
    def editNote(self):
        raise NotImplementedError("todo")
    
    def removeNote(self):
        raise NotImplementedError("todo")
    
    
def main():
    a = DbBridge()
    a._purge_notepad()

if __name__ == "__main__":
    main()