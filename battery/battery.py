from abc import ABC, abstractmethod
from datetime import datetime
class Battery(ABC):
    def __init__(self, last_service_date, current_date : date) -> None:
        super().__init__()
        self.last_service_date = last_service_date
        self.current_date = current_date
    @abstractmethod
    def needs_service():
        pass

class SpindlerBattery(Battery):
    def __init__(self, last_service_date: datetime, current_date: datetime) -> None:
        super().__init__(last_service_date, current_date)

    def needs_service(self) -> bool:
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 2)
        return service_threshold_date < self.current_date

class NubbinBattery(Battery):
    def __init__(self, last_service_date, current_date) -> None:
        super().__init__(last_service_date, current_date)
    def needs_service(self) -> bool:
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 4)
        return service_threshold_date < self.current_date