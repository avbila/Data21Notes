# Task:
# Create a car class. Give the vehicle a maximum speed, and keep track of the current speed of the vehicle.
# It doesn't make sense for the speed to be adjusted directly, so put an underscore in front of it and implement a
# speed getter as well as accelerate and brake setter methods that change the speed in a logical way.
# Do your methods make sense? Does braking past 0 cause the speed to increase?
# Can you accelerate past the car's top speed?

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


# Car 1:
bmw_z4 = Car(250, 1505)
bmw_z4.accelerate_car(5000, 6)
print(bmw_z4.show_car_speed())
bmw_z4.accelerate_car(5000, 20)
print(bmw_z4.show_car_speed())
bmw_z4.applying_car_breaks(6000, 120)
print(bmw_z4.show_car_speed())
