class Person:
    def __init__(self, fname, email):
        self.first_name = fname #Public variable
        self._email = email # Private variable (_string) for encapsulation : the private variable is used only internally

    def update_email(self, email):
        self._email = email

    def get_email(self):
        return self._email


tk = Person('tk', 'tk@email')
print(tk.first_name, tk.get_email)
tk.update_email('new@email')
print(tk.get_email())

# Example of encapsulation 2 :
class Person:
    def __init__(self, fname, age):
        self.first_name = fname 
        self._age = age 
    def show_age(self):
        return self._get_age() # here function is private and cannot be reached external

    def _get_age(self):
        return self._age

tk = Person('tk', 20)
print(tk.show_age())

# Example of inheritance 
class Car:
    def __init__(self, num_of_wheels, seating_capacity, max_velocity):
        self.num_of_wheels = num_of_wheels
        self.seating_capacity = seating_capacity
        self.max_velocity = max_velocity

    def make_noicse(self):
        print('Yeehaa!!')

class ElectricCar(Car):
    def __init__(self, num_of_wheels, seating_capacity, max_velocity, battery):
        super().__init__(num_of_wheels, seating_capacity, max_velocity)
        self.battery = battery
        self.state = ''

    def sold_in_state(self, sold_state):
        self.state = sold_state


electricCar = ElectricCar(4, 5, 250, "1000V")
electricCar.sold_in_state('CA')
electricCar.make_noicse()
