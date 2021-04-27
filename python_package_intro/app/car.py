class Car:
    _vehicle_speed = 0.0

    def __init__(self, top_speed, weight):
        self._top_speed = top_speed
        self._car_weight = weight

    def accelerate_car(self, force, time):
        if force > 0:
            for t in range(time):
                self._vehicle_speed = self._vehicle_speed + 3.6*(force/self._car_weight)
                if self._vehicle_speed > self._top_speed:
                    self._vehicle_speed = self._top_speed
                    break

    def applying_car_breaks(self, force, time):
        if force > 0:
            for t in range(time):
                self._vehicle_speed = self._vehicle_speed - 3.6*(force/self._car_weight)
                if self._vehicle_speed < 0:
                    self._vehicle_speed = 0
                    break

    def show_car_speed(self):
        speed = str(round(self._vehicle_speed, 2)) + " Km/h"
        return speed