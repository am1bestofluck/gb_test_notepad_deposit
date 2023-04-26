"""
Блокнотик v 0.0000001 alpha;
продолжает тему "кусочка управленческого учёта таксопарка", она же - диплом
"""
from abc import ABC, abstractmethod, property,abstractstaticmethod
from datetime import date
from sqlite3 import Connection

from note import Note
from mainTopics import MainTopics


class db_note_tweaker(ABC):
    
    @abstractstaticmethod
    def editNoteContent(cls, base:Connection, noteTopic:MainTopics, noteId:int):
        raise NotImplementedError("edit existing note, only content")
    
    @abstractstaticmethod
    def editNoteHeader(cls, base:Connection, noteTopic:MainTopics, noteId:int):
        raise NotImplementedError("edit existing note, only header")


class db_note_saver(ABC):
    
    @abstractstaticmethod
    def save(cls, note:Note, base: Connection):
        raise NotImplementedError("for creator")


class db_note_remover(ABC):
    
    @abstractstaticmethod
    def remove(self,base: Connection, noteTopic:MainTopics, noteId:int):
        raise NotImplementedError("removes note from table")


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
    
    def __addCarNote(self,note:Note):
        raise NotImplementedError("TODO")
    
    def __addDriverNote( self, note:Note):
        raise NotImplementedError("TODO")
    
    def removeNote(self,topic:MainTopics, noteID: int):
        raise NotImplementedError("fork, based on maintopic")
    
    def __removeCarNote(self, noteID:int):
        raise NotImplementedError("TODO")
    
    def __removeDriverNote( self, noteID:int):
        raise NotImplementedError("TODO")
    
    def editNote(self,topic:MainTopics, noteID: int):
        raise NotImplementedError("fork, based on maintopic")
    
    def __editCarNote(self, noteID:int):
        raise NotImplementedError("TODO")
    
    def __editDriverNote(self, noteID:int):
        raise NotImplementedError("TODO")