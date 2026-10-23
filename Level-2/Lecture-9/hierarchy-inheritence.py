class Car: 
    def __init__(self,model_name,number_of_doors,engine_model): 
        self.model_name = model_name 
        self.number_of_doors = number_of_doors 
        self.engine_model = engine_model 

    def describe_car(self): 
        print(f"Model Name: {self.model_name}")
        print(f"Number of Doors: {self.number_of_doors}")
        print(f"Engine Model: {self.engine_model}")

class ElectircCar(Car): 
    def __init__(self,model_name,number_of_doors,engine_model,battery): 
        super().__init__(model_name,number_of_doors,engine_model)
        self.battery = battery
    def charge(self): 
        print("Charging...")
        self.battery = 100 
    def describe_electric_car(self):
        self.describe_car()
        print(f"Battery Percentage: {self.battery} %")

class FuelCar(Car): 
    def __init__(self,model_name,number_of_doors,engine_model,fuel,fuel_type):
        super().__init__(model_name,number_of_doors,engine_model)
        self.fuel = fuel 
        self.fuel_type = fuel_type
    def refill(self): 
        print("Refilling the Tank...")
        self.fuel = 100 
    def describe_fuel_car(self): 
        self.describe_car()
        print(f"Fuel Type : {self.fuel_type}")
        print(f"Fuel Percentage: {self.fuel} %") 

# electric_car = ElectircCar("Tesla",4,"Tesla electrical engine",50)
# electric_car.charge()
# electric_car.describe_electric_car()

petrol_car = FuelCar("BMW",4,"Petrol Engine",40,"Petrol")
petrol_car.refill()
petrol_car.describe_fuel_car()