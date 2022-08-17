from abc import ABC, abstractmethod
from sys import _enablelegacywindowsfsencoding
from serviceable import Serviceable
from battery.battery import Battery
from engine.engine import Engine 

class Car(Serviceable):
    def __init__(self, engine: Engine, battery: Battery):
        self.engine = engine
        self.battery = battery

    @abstractmethod
    def battery_needs_service(self):
        if self.battery.needs_service():
            return True
        return False

    def engine_needs_service(self):
        if self.engine.needs_service():
            return True
        return False