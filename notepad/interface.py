"""
Блокнотик v 0.0000001 alpha;
продолжает тему "кусочка управленческого учёта таксопарка", она же - диплом
"""
from abc import ABC, abstractmethod,abstractstaticmethod
from datetime import date
from sqlite3 import Connection

from note import Note
from mainTopics import MainTopics


class db_note_tweaker(ABC):
    
    @abstractstaticmethod
    def editNoteContent(cls, base:Connection):
        raise NotImplementedError("edit existing note, only content")
    
    @abstractstaticmethod
    def editNoteHeader(cls, base:Connection):
        raise NotImplementedError("edit existing note, only header")
    


class db_note_saver(ABC):
    
    @abstractstaticmethod
    def push(cls, note:Note, base: Connection):
        raise NotImplementedError("for creator")


class db_note_remover(ABC):
    
    @abstractstaticmethod
    def remove(self,base: Connection, noteTopic:MainTopics, noteId:int):
        raise NotImplementedError("removes note from table")

class db_note_reader(ABC):

    @abstractmethod
    def readall():
        raise NotImplementedError("todo")
    
    @abstractmethod
    def readSpecific():
        raise NotImplementedError("todo")

class dbMain(ABC):

    @abstractmethod
    def _purge_notepad():
        raise NotImplementedError("resests Notepad tables; Assumes that "
            + "database already exists.")

    @abstractmethod
    def __connection(self):
        raise NotImplementedError("sql handshake here")
    
    @abstractmethod
    def addNote(self,note:Note):
        raise NotImplementedError("fork, based on maintopic")
    
    @abstractmethod
    def __addCarNote(self,note:Note):
        raise NotImplementedError("TODO")
    
    @abstractmethod
    def __addDriverNote( self, note:Note):
        raise NotImplementedError("TODO")
    
    @abstractmethod
    def removeNote(self,topic:MainTopics, noteID: int):
        raise NotImplementedError("fork, based on maintopic")
    
    @abstractmethod
    def __removeCarNote(self, noteID:int):
        raise NotImplementedError("TODO")
    
    @abstractmethod
    def __removeDriverNote( self, noteID:int):
        raise NotImplementedError("TODO")
    
    @abstractmethod
    def editNote(self,topic:MainTopics, noteID: int):
        raise NotImplementedError("fork, based on maintopic")
    
    @abstractmethod
    def __editCarNote(self, noteID:int):
        raise NotImplementedError("TODO")
    
    @abstractmethod
    def __editDriverNote(self, noteID:int):
        raise NotImplementedError("TODO")
    
    @abstractmethod
    def readNote(self):
        raise NotImplementedError("TODO")
    
    @abstractmethod
    def readAllNotes(self):
        raise NotImplementedError("TODO")