
from sqlite3 import Cursor,Connection
from datetime import datetime

from interface import db_note_reader
from noteSelector import Note_selector
from CONSTANTS import BASEPATH,CARNOTES,DRIVERNOTES,REFS


class NoteReader(db_note_reader):
    def __init__(self,base:Connection):
        self.__base= base

    def readall(self) -> None:
        crs=Cursor(self.__base)
        print("print all car notes")
        crs.execute(f"SELECT * FROM {CARNOTES}")
        notes=crs.fetchall()
        for i in notes:
            car=crs.execute(f"SELECT GOVPL FROM cars where ID='{i[1]}'").fetchone()[0]
            print(f"note about {car} from {datetime.strptime(i[2],'%Y-%m-%d').date().strftime('%d/%m/%Y')}:\n\t{i[3]}")
        print("out for driver notes")
        crs.execute(f"SELECT * FROM {DRIVERNOTES}")
        notes=crs.fetchall()
        for i in notes:
            personID = crs.execute(f"SELECT PERSONID FROM drivers where ID='{i[1]}'").fetchone()[0]
            fullname= crs.execute(f"SELECT FULLNAME FROM persons where ID='{personID}'").fetchone()[0]
            print(f"note about {fullname} from {datetime.strptime(i[2],'%Y-%m-%d').date().strftime('%d/%m/%Y')}:\n\t{i[3]}")

    def readSpecific(self) -> None:
        selector=Note_selector(self.__base)
        pick=selector.selectNote()
        tableName=pick[0]
        idNote=pick[2]
        idCar=pick[3]
        crs=Cursor(self.__base)
        carNumber =crs.execute(f"SELECT GOVPL FROM {REFS[tableName]} WHERE ID='{idCar}'").fetchone()[0]
        noteToRead=crs.execute(f"SELECT * FROM {tableName} WHERE ID='{idNote}'").fetchone()
        print(f"Note #{noteToRead[0]} about car {carNumber} from"
              + f" {datetime.strptime(noteToRead[2],'%Y-%m-%d').date().strftime('%d/%m/%Y')}:\n\t"
              + f"{noteToRead[3]}")
        pass



def main():
    a=Connection(BASEPATH)
    b=NoteReader(a)
    b.readSpecific()

if __name__ == "__main__":
    main()
