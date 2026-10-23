class SpiderMan:
    def __init__(self): 
        self.name = "Peter Parker"
    def speak(self): 
        print("I'm Spider Man")

class Venom(SpiderMan): 
    def __init__(self):
        self.name = "Eddie Brock"

    def speak(self): 
        print("We're Venom..")


spider_man = SpiderMan()
spider_man.speak()
venom = Venom()
venom.speak()