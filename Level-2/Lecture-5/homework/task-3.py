"""
A music app lets a user duplicate a playlist and then edit the duplicate. Create a Playlist class
with a copy constructor. If it receives None, the playlist starts with name "Untitled Playlist", owner
"unknown", songs 0 and minutes 0. Otherwise it copies all four values from the playlist it
receives. Add a display method that prints the four lines shown in the sample output.
Create a blank playlist, give it the values below, and make copy from it. Change the copy’s
name and number of songs. Display the original, print a line of 20 dashes, and display the copy.
Sample Input:
original: name = "Morning Run", owner = "Arjun", songs = 18, minutes = 62
copy: name = "Gym Mix", songs = 25
Sample Output:
Name: Morning Run
Owner: Arjun
Songs: 18
Minutes: 62
--------------------
Name: Gym Mix
Owner: Arjun
Songs: 25
Minutes: 62
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
        print(f"Name: {self.name}")
        print(f"Owner: {self.owner}")
        print(f"Songs: {self.songs}")
        print(f"Minutes: {self.minutes}")

original_playlist = Playlist(None)
original_playlist.name = "Morning Run"
original_playlist.owner = "Arjun"
original_playlist.songs = 18 
original_playlist.minutes = 64 
copy_playlist = Playlist(original_playlist)

copy_playlist.name = "Gym Mix"
copy_playlist.songs = 25 

original_playlist.display()
print("-"*20)
copy_playlist.display()