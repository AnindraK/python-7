class Playlist:
    
    
    def __init__(self, name, genre):
        self.name = name
        self.genre= genre
        self.song = []
        print(f"Playlist '{self.name}' ({self.genre}) is ready!")


    def add_song(self, song):
        self.song.append(song)
        print(f"'{song} added to {self.name}.")

    
    
    
    
    
    
    def remove_song(self, song):
        if song in self.song:
            self.song.remove(song)
            print(f"'{song}' removed.")
        else:
            print(f"'{song} not found in playlist.")

    def display(self):
        print(f"\n--- {self.name} ({self.genre})---")
        if self.song:
            for i, song in enumerate(self.song, 1):
                print(f" {i}.{song}")
            else:
                print("No songs yet! add some.")
                
    def __del__(self):
        print(f"Playlist '{self.name}' has been deleted. goodbye!")

my_playlist = Playlist("road trip mix", "pop")

while True:
    print("\n1. add song  2. remove song  3. view playlist  4. delete and quit")
    choice = input("enter your choice:")

    if choice == "1":
        song = input("Enter your song name:")
        my_playlist.add_song(song)
    elif choice == "2":
        song = input("Enter a song to remove:")
        my_playlist.remove_song(song)
    elif choice == "3":
        my_playlist.display()
    elif choice == "4":
        del my_playlist
        break
    else:
        print("Invalid choice. Please enter choice 1,2,3 or 4.")



                                    