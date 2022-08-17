from abc import ABC, abstractmethod

class Engine(ABC):
    def __init__(self, last_service_mileage, current_mileage) -> None:
        super().__init__()
        self.last_service_mileage = last_service_mileage
        self.current_mileage = current_mileage
    @abstractmethod
    def needs_service():
        pass

class CapuletEngine(Engine):
    def __init__(self, last_service_mileage, current_mileage) -> None:
        super().__init__(last_service_mileage, current_mileage)
    def needs_service(self) -> bool:
        return self.current_mileage - self.last_service_mileage > 30000

class WilloughbyEngine(Engine):
    def __init__(self, last_service_mileage, current_mileage) -> None:
        super().__init__(last_service_mileage, current_mileage)
    def needs_service(self) -> bool:
        return self.current_mileage - self.last_service_mileage > 60000

class SternmanEngine(Engine):
    def __init__(self, warning_light: bool) -> None:
        self.warning_light = warning_light

    def needs_service(self) -> bool:
        if self.warning_light:
            return True
        return False