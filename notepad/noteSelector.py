
from sqlite3 import Connection, Cursor

import mainTopics
from CONSTANTS import CARNOTES,DRIVERNOTES,BASEPATH


class Note_selector():
    def __init__(self,base:Connection) -> None:
        self.__base = base
    
    def selectNote(self):
        print("Now We choose note to edit/remove!")
        topic = mainTopics.MainTopics.car \
            if input("Choose topic, \"1\" for car, else for driver") in \
                ["1","\"1\""] else mainTopics.MainTopics.driver
        
        correctIndex=False
        while not correctIndex:
            number= ""
            while not number.isdigit():
                number = input("input note number")
            tableName=CARNOTES if topic.name == "car" else DRIVERNOTES
            crs = Cursor(self.__base)
            number_= crs.execute(f"SELECT id FROM {tableName} where id='{number}'")
            number_o = number_.fetchone()
            car = crs.execute(f"SELECT header FROM {tableName} where id='{number}'")
            car_o=car.fetchone()
            
            correctIndex = False if number_ is None else True
            if not correctIndex:
                print(f"no such noteID in {tableName}")
        return (tableName,topic,number_o[0],car_o[0])# mainTopics.MainTopics.car, number.isdigit(),int
    

def main():
    a=Connection(BASEPATH)
    b=Note_selector(a)
    c=b.selectNote()
    a.close()
    print(c)

if __name__ == "__main__":
    main()