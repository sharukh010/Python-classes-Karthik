class Family: 
    def __init__(self,name): 
        self.name = name 
    def display(self,**members): 
        print(f"{self.name}'s Family:")
        for key in members.keys():
            print(f"{key.title()}: {members[key]}")

parker = Family("Parker")
parker.display(uncle="Ben Parker",aunt="May Parker",grandson="Peter Parker")

potter = Family("Potter")
potter.display(mother="Lily Potter",father="James Potter",son="Harry Potter",inlaw="Ginny Potter")
# the parameter will be converted to {"uncle":"Ben Parker","aunt":"May Parker","grandson":"Peter Parker"}