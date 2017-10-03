"""Object oriented programming lesson from HackerRank."""


class Car:
    """Initialize car class with instance variables."""

    max_speed = 100
    min_speed = 0
    is_driving = False
    # condition is a char
    condition = "A"

    def __init__(self, make, model):
        """Initialize make and model."""
        self.make = make
        self.model = model

    def print_variables(self):
        """Print to terminal the values of the instance variables."""
        print(Car.max_speed)
        print(Car.min_speed)
        print(Car.is_driving)
        print(Car.condition)

    def get_make_and_model(self):
        """Print the make of the car to the terminal."""
        make_model = self.make + " " + self.model
        print(make_model)
        return make_model

    def car_is_driving(self):
        """Return boolean value to set is_driving variable."""
        return True if is_driving else False


# Instantiate a car of the Car class
new_car = Car("Toyota", "Prius")
# Use the get make and model mathod on that car
new_car.get_make_and_model()
# Use the print method to see that the instance variables are set to
new_car.print_variables()
is_driving = car_is_driving(self, is_driving)
print("{} is currently driving: {}")
