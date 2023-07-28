from tire.tire import Tire


class CarriganTire(Tire):
    def __init__(self, tire_worn_arr):
        self.tire_worn_arr = tire_worn_arr

    def needs_service(self):
        for val in self.tire_worn_arr:
            if val >= 0.9:
                return True
        return False
