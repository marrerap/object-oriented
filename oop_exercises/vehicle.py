class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year


    def car_info(self):
         print( f"My car is a {self.year} {self.make}, {self.model}!\n")