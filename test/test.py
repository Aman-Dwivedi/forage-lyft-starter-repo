import unittest
from datetime import datetime
from engine import capulet_engine, willoughby_engine, sternman_engine
from battery import splinder_battery, nubbin_battery
from tire import carrigan, octoprime


class TestCapulet(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        current_mileage = 30001
        last_service_mileage = 0
        engine = capulet_engine.CapuletEngine(last_service_mileage, current_mileage)
        self.assertTrue(engine.needs_service())

    def test_engine_should_not_be_serviced(self):
        current_mileage = 29999
        last_service_mileage = 0
        engine = capulet_engine.CapuletEngine(last_service_mileage, current_mileage)
        self.assertFalse(engine.needs_service())

class TestWilloughby(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        current_mileage = 60001
        last_service_mileage = 0
        engine = willoughby_engine.WilloughbyEngine(last_service_mileage, current_mileage)
        self.assertTrue(engine.needs_service())

    def test_engine_should_not_be_serviced(self):
        current_mileage = 59999
        last_service_mileage = 0
        engine = willoughby_engine.WilloughbyEngine(last_service_mileage, current_mileage)
        self.assertFalse(engine.needs_service())

class TestSternman(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        engine = sternman_engine.SternmanEngine(True)
        self.assertTrue(engine.needs_service())

    def test_engine_should_not_be_serviced(self):
        engine = sternman_engine.SternmanEngine(False)
        self.assertFalse(engine.needs_service())

class TestSpindler(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        battery = splinder_battery.SplinderBattery(last_service_date, today)
        self.assertTrue(battery.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 2)
        battery = splinder_battery.SplinderBattery(last_service_date, today)
        self.assertFalse(battery.needs_service())

class TestNubbin(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 4)
        battery = nubbin_battery.NubbinBattery(last_service_date, today)
        self.assertTrue(battery.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        battery = nubbin_battery.NubbinBattery(last_service_date, today)
        self.assertFalse(battery.needs_service())

class TestCarrigan(unittest.TestCase):
    def test_tire_should_be_serviced(self):
        tire_worn_arr = [0.1, 0.2, 0.3, 0.9]
        tire = carrigan.CarriganTire(tire_worn_arr)
        self.assertTrue(tire.needs_service())

    def test_battery_should_not_be_serviced(self):
        tire_worn_arr = [0.1, 0.2, 0.3, 0.8]
        tire = carrigan.CarriganTire(tire_worn_arr)
        self.assertFalse(tire.needs_service())

class TestOctoprime(unittest.TestCase):
    def test_tire_should_be_serviced(self):
        tire_worn_arr = [1, 0.9, 0.2, 0.9]
        tire = octoprime.OctoprimeTire(tire_worn_arr)
        self.assertTrue(tire.needs_service())

    def test_battery_should_not_be_serviced(self):
        tire_worn_arr = [1, 0.1, 0.9, 0.9]
        tire = octoprime.OctoprimeTire(tire_worn_arr)
        self.assertFalse(tire.needs_service())