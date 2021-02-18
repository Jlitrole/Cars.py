class Car:
    wheels = 4
    doors = 2
    engine = True

    def __init__(self, make, model, year):
        self.make = make
        self.model = Model
        self.year = year

    def stop(self):
        if self.is_moving:
            print('The car has stopped')
            self.is_moving = False
        else:
            print('The car has alredy stopped')

    def go(self, speed):
        if not self.is_moving:
            print('The car starts moving')
            

car_one = Car("Ford", "Model T", 1908)
car_two = Car("Rolls Royce", "Phantom", 2020)
print(car_one.make)
print
