from datetime import datetime
from battery.battery import Battery, NubbinBattery, SpindlerBattery
from engine.engine import CapuletEngine, Engine, SternmanEngine, WilloughbyEngine
from Car.car import Car
from ..tire.tire import CarriganTires, OctoprimeTires

class CarFactory:
    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage, tire_wear) -> Car:
        return Car(CapuletEngine(last_service_mileage, current_mileage), SpindlerBattery(last_service_date, current_date), CarriganTires(tire_wear))

    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage, tire_wear) -> Car:
        return Car(WilloughbyEngine(last_service_mileage, current_mileage), SpindlerBattery(last_service_date, current_date), OctoprimeTires(tire_wear))

    def create_palindrome(current_date, last_service_date, warning_light_on, tire_wear) -> Car:
        return Car(SternmanEngine(warning_light_on), SpindlerBattery(last_service_date, current_date), CarriganTires(tire_wear))


    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage, tire_wear) -> Car:
        return Car(WilloughbyEngine(last_service_mileage, current_mileage), NubbinBattery(last_service_date, current_date), OctoprimeTires(tire_wear))

    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage, tire_wear) -> Car:
        return Car(CapuletEngine(last_service_mileage, current_mileage), NubbinBattery(last_service_date, current_date), OctoprimeTires(tire_wear))
