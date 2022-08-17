import unittest
from datetime import datetime
from CarFactory.carfactory import CarFactory
from Car.car import Car

from battery.battery import Battery, NubbinBattery, SpindlerBattery
from engine.engine import CapuletEngine, Engine, SternmanEngine, WilloughbyEngine


class TestCalliope(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0
        car_factory = CarFactory()
        car = car_factory.create_calliope(Battery(last_service_date, today), Engine(last_service_mileage, current_mileage))
        self.assertTrue(car.battery_needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        current_mileage = 0
        last_service_mileage = 0
        car_factory = CarFactory()
        car = car_factory.create_calliope(Battery(last_service_date, today), Engine(last_service_mileage, current_mileage))
        self.assertFalse(car.battery_needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 30001
        last_service_mileage = 0
        car_factory = CarFactory()
        car = car_factory.create_calliope(Battery(last_service_date, datetime.today().date()), Engine(last_service_mileage, current_mileage))
        self.assertTrue(car.engine_needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 30000
        last_service_mileage = 0
        car_factory = CarFactory()
        car = car_factory.create_calliope(Battery(last_service_date, datetime.today().date()), Engine(last_service_mileage, current_mileage))
        self.assertFalse(car.engine_needs_service())


class TestGlissade(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0

        car_factory = CarFactory()
        car = car_factory.create_glissade(Battery(last_service_date, today), Engine(last_service_mileage, current_mileage))
        self.assertTrue(car.battery_needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        current_mileage = 0
        last_service_mileage = 0

        car_factory = CarFactory()
        car = car_factory.create_glissade(Battery(last_service_date, today), Engine(last_service_mileage, current_mileage))
        self.assertFalse(car.battery_needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 60001
        last_service_mileage = 0
        car_factory = CarFactory()
        car = car_factory.create_glissade(Battery(last_service_date, datetime.today().date()), Engine(last_service_mileage, current_mileage))
        self.assertTrue(car.engine_needs_service())

        

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 60000
        last_service_mileage = 0

        car_factory = CarFactory()
        car = car_factory.create_glissade(Battery(last_service_date, datetime.today().date()), Engine(last_service_mileage, current_mileage))
        self.assertFalse(car.engine_needs_service())


class TestPalindrome(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        warning_light_is_on = False

        car_factory = CarFactory()
        car = car_factory.create_palindrome(Battery(last_service_date, today), Engine(warning_light_is_on))
        self.assertTrue(car.battery_needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        warning_light_is_on = False

        car_factory = CarFactory()
        car = car_factory.create_palindrome(Battery(last_service_date, today), Engine(warning_light_is_on))
        self.assertFalse(car.battery_needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        warning_light_is_on = True

        car_factory = CarFactory()
        car = car_factory.create_palindrome(Battery(last_service_date, datetime.today().date()), Engine(warning_light_is_on))
        self.assertTrue(car.engine_needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        warning_light_is_on = False

        car_factory = CarFactory()
        car = car_factory.create_palindrome(Battery(last_service_date, datetime.today().date()), Engine(warning_light_is_on))
        self.assertFalse(car.engine_needs_service())


class TestRorschach(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        current_mileage = 0
        last_service_mileage = 0

        car_factory = CarFactory()
        car = car_factory.create_rorschach(Battery(last_service_date, today), Engine(last_service_mileage, current_mileage))
        self.assertTrue(car.battery_needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0

        car_factory = CarFactory()
        car = car_factory.create_rorschach(Battery(last_service_date, today), Engine(last_service_mileage, current_mileage))
        self.assertFalse(car.battery_needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 60001
        last_service_mileage = 0

        car_factory = CarFactory()
        car = car_factory.create_rorschach(Battery(last_service_date, datetime.today().date()), Engine(last_service_mileage, current_mileage))
        self.assertTrue(car.engine_needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 60000
        last_service_mileage = 0

        car_factory = CarFactory()
        car = car_factory.create_rorschach(Battery(last_service_date, datetime.today().date()), Engine(last_service_mileage, current_mileage))
        self.assertFalse(car.engine_needs_service())


class TestThovex(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        current_mileage = 0
        last_service_mileage = 0

        car_factory = CarFactory()
        car = car_factory.create_thovex(Battery(last_service_date, today), Engine(last_service_mileage, current_mileage))
        self.assertTrue(car.battery_needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0

        car_factory = CarFactory()
        car = car_factory.create_thovex(Battery(last_service_date, today), Engine(last_service_mileage, current_mileage))
        self.assertFalse(car.battery_needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 30001
        last_service_mileage = 0

        car_factory = CarFactory()
        car = car_factory.create_thovex(Battery(last_service_date, datetime.today().date()), Engine(last_service_mileage, current_mileage))
        self.assertTrue(car.engine_needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 30000
        last_service_mileage = 0

        car_factory = CarFactory()
        car = car_factory.create_thovex(Battery(last_service_date, datetime.today().date()), Engine(last_service_mileage, current_mileage))
        self.assertFalse(car.engine_needs_service())


if __name__ == '__main__':
    unittest.main()
