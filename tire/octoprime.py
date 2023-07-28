from tire.tire import Tire


class OctoprimeTire(Tire):
    def __init__(self, tire_worn_arr):
        self.tire_worn_arr = tire_worn_arr

    def needs_service(self):
        return sum(self.tire_worn_arr) >= 3
