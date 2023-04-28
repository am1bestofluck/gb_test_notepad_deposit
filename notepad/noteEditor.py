from sqlite3 import Cursor,Connection

from interface import db_note_tweaker
from noteCreator import NoteCreator
from noteSelector import Note_selector
from CONSTANTS import NOTELIMIT,BASEPATH

class NoteEditor(db_note_tweaker, Note_selector):
    
    def __init__(self,base:Connection) -> None:
        self.__base = base
    
    def editNoteContent(self) -> Connection:
        # return (tableName,topic,number[0])# mainTopics.MainTopics.car, number.isdigit()
        print("We edit body of note!")
        selector=Note_selector(self.__base)
        pick=selector.selectNote()
        tableName=pick[0]
        obj=pick[1].name
        num=pick[2]
        crs = Cursor(self.__base)
        oldText=crs.execute(f"SELECT content FROM {tableName} where id='{num}'").fetchone()[0]
        newText=input(f"replace old text of {obj} note (\n{oldText}\n)... with new:\n>>> ")
        crs.execute(f"""UPDATE {tableName}
        SET content='{newText}'
        WHERE id='{num}';""")
        return self.__base
    
    def editNoteHeader(self) -> Connection:
        print("We edit header of note!")
        selector=Note_selector(self.__base)
        pick=selector.selectNote()
        tableName=pick[0]
        obj=pick[1].name
        num=pick[2]
        govpl=pick[3]
        crs = Cursor(self.__base)
        oldHeader = crs.execute(f"SELECT GOVPL FROM cars WHERE ID='{str(govpl)}'").fetchone()[0]
        oldText=crs.execute(f"SELECT content FROM {tableName} WHERE id='{num}'").fetchone()[0]
        # oldHeaderId=crs.execute(f"SELECT header FROM {tableName} where id='{num}'").fetchone()[0]
        
        correctNumber=False
        while not correctNumber:
            try:
                newText=input(f"replace old header({oldHeader}) of {obj} note (\n{oldText}\n)... with new:\n>>> ").upper()
                newId=crs.execute(f"SELECT ID FROM cars WHERE GOVPL='{newText}'").fetchone()[0]
                correctNumber=True
            except AttributeError:
                print("no such number")
    
        crs.execute(f"""UPDATE {tableName}
        SET header='{newId}'
        WHERE id='{num}';""")
        return self.__base

def main():
    q=Connection(BASEPATH)
    a=NoteEditor(q)
    q=a.editNoteContent()
    # q=a.editNoteHeader()
    q.commit()
    q.close()


if __name__ =="__main__":
    main()

