"""
A shop sells laptops. Create a Laptop class with a parameterized constructor that takes the
brand, RAM in GB, storage in GB and price in rupees. Add a display method that prints the
four lines shown in the sample output.
Create two laptops with the values below. Display the first, print a line of 20 dashes, and display
the second.
Sample Input:
laptop1 = Laptop("Dell", 16, 512, 55000)
laptop2 = Laptop("HP", 8, 256, 38500)
Sample Output:
Brand: Dell
RAM: 16 GB
Storage: 512 GB
Price: 55000 rupees
--------------------
Brand: HP
RAM: 8 GB
Storage: 256 GB
Price: 38500 rupees
"""
class Laptop: 
    def __init__(self,brand,ram,storage,price): 
        self.brand = brand 
        self.ram = ram 
        self.storage = storage 
        self.price = price 
    def display(self): 
        print(f"Brand: {self.brand}")
        print(f"RAM: {self.ram} GB")
        print(f"Storage: {self.storage} GB")
        print(f"Price: {self.price} rupees")

laptop1 = Laptop("Dell",16,512,55000)
laptop2 = Laptop("HP",8,256,38500)

laptop1.display()
print("-"*20)
laptop2.display()