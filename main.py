class Car():

    def __init__(self, brand, color, count_of_door):
        self.brand = brand
        self.color = color
        self.count_of_door = count_of_door

    def beep(self):
        print('Beep beep')

car1 = Car('Jeep', 'Black', 4)

print(car1.color)

car1.beep()
