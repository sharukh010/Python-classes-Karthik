"""
In a class you will have three types of methods those are 
1) setter -> which will set the value of a property
- they will not return any data they making changes in properties 
ex: 
set_name(new_name) it will set the property(name) value to the new name
set_owner(new_owner) it will set the property(owner) value to the new owner 
2) getters -> which will get the values of a property 
- they will not make any changes to the properties 
- they will return the data 
ex: 
get_name() -> it will get you the value of the name 
get_owner() -> it will get you the value of the owner 
3) action -> which will perform some operation 
ex: 
display() -> this will print the details 
area() -> this will calculate the area   
"""
class Playlist: 
    def __init__(self,playlist): 
        if playlist == None: 
            self.name = "Untitled Playlist"
            self.owner = "unknown"
            self.songs = 0 
            self.minutes = 0 
        else: 
            self.name = playlist.name 
            self.owner = playlist.owner 
            self.songs = playlist.songs 
            self.minutes = playlist.minutes 
    def display(self): 
        print(f"Name: {self.get_name()}")
        print(f"Owner: {self.get_owner()}")
        print(f"Songs: {self.get_songs()}")
        print(f"Minutes: {self.get_minutes()}")
    def set_name(self,new_name): 
        self.name = new_name 
    def set_owner(self,new_owner): 
        self.owner = new_owner
    def set_songs(self,new_songs): 
        self.songs = new_songs
    def set_minutes(self,new_minutes):
        self.minutes = new_minutes

    def get_name(self): 
        return self.name 
    def get_owner(self): 
        return self.owner 
    def get_songs(self): 
        return self.songs 
    def get_minutes(self): 
        return self.minutes

original_playlist = Playlist(None)
original_playlist.set_name("Coding Mix")
original_playlist.set_owner("Karthik")
original_playlist.set_songs(30)
original_playlist.set_minutes(120)
original_playlist.display()