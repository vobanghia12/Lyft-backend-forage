#interface
from abc import ABC, abstractmethod

class Serviceable:
    @abstractmethod
    def needs_service():
        pass