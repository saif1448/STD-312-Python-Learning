#class
#object
#instance variables
#constructor ---> __init__
#instance method ---> self is must for every method under the class

#OOP Principle
# Encapsulation
# Abstraction



class Car:
    def __init__(self, name, model):
        self.name = name
        self.model = model
    #
    # def show_car_details(self):
    #     print(f"Name: {self.name}\nModel: {self.model}")

    def show_yearly_depreciation(self):
        pass

    def __str__(self):
        return f'Name: {self.name}, Model: {self.model}'


toyota = Car("Toyota", "Toyota Model")  #objects are also called instances of class
mercedes = Car("Mercedes", "Mercedes Model")

# toyota.name = "Toyota"
# toyota.model = "Toyota model"
#
# mercedes.name = "Mercedes"
# mercedes.model = "Mercedes model"
#
# toyota.show_car_details()
# mercedes.show_car_details()

print(toyota)
print(mercedes)