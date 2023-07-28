from engine.capulet_engine import CapuletEngine
from engine.willoughby_engine import WilloughbyEngine
from engine.sternman_engine import SternmanEngine
from battery.splinder_battery import SplinderBattery
from battery.nubbin_battery import NubbinBattery
from car import Car


class CarFactory:

    def create_calliope(self, current_date, last_service_date, current_mileage, last_service_mileage):
        engine = CapuletEngine(last_service_mileage, current_mileage)
        battery = SplinderBattery(last_service_date, current_date)
        return Car(engine, battery)

    def create_glissade(self, current_date, last_service_date, current_mileage, last_service_mileage):
        engine = WilloughbyEngine(last_service_mileage, current_mileage)
        battery = SplinderBattery(last_service_date, current_date)
        return Car(engine, battery)

    def create_pallindrome(self, current_date, last_service_date, warning_light_on):
        engine = SternmanEngine(warning_light_on)
        battery = SplinderBattery(last_service_date, current_date)
        return Car(engine, battery)

    def create_rorschach(self, current_date, last_service_date, current_mileage, last_service_mileage):
        engine = WilloughbyEngine(last_service_mileage, current_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        return Car(engine, battery)

    def create_thovex(self, current_date, last_service_date, current_mileage, last_service_mileage):
        engine = CapuletEngine(last_service_mileage, current_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        return Car(engine, battery)