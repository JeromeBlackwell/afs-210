

class Song:
    def __init__(self,title,artist):
        self.title = title
        self.artist = artist
    def delete(self, data) -> None:
        # Delete a node from the list who's value matches the supplied value
        current = self.head
        prev = self.head
        while current:
            if current.data == data:
                if current == self.tail:
                    prev.next = None
                    self.tail = prev
                elif current == self.head:
                    current.next.prev = None
                    self.head = current.next
                else:
                    prev.next = current.next
                    current.next = prev
                self.count -= 1
                return
            prev = current
            current = current.next
    def getTitle(self):
        return self.title

    def getArtist(self):
        return self.artist
        
    def __str__(self):
        return self.title + " by " + self.artist 

    def __eq__(self, other):
        return ((self.title, self.artist) == (other.title, other.artist))
        
    def __ne__(self, other):
        return not (self == other)

    def __lt__(self, other):
        return ((self.title, self.artist) < (other.title, other.artist))
        
    def __gt__(self, other):
        return ((self.title, self.artist) < (other.title, other.artist))
        


def menu():
    print(20 * "-" , "MENU" , 20 * "-")
    print("1. Add Song to Playlist")
    print("2. Remove song from Playlist")
    print("3. Play")
    print("4. Skip")
    print("5. Go Back")
    print("6. Shuffle")
    print("7. Show Currently Playing Song")
    print("8. Show Current Playlist Order")
    print("0. Exit")
    print(47 * "-")


while True:
    menu()
    choice = int(input())

    if choice == 1:
        # Add code to prompt user for Song Title and Artist Name
        # Add song to playlist
        add()
        print("New Song Added to Playlist")
        pass
    elif choice == 2:
        # Prompt user for Song Title 
        # remove song from playlist
        delete()
        print("Song Removed to Playlist")
        pass
    elif choice == 3:
        # Play the playlist from the beginning
        # Display song name that is currently playing
        play_curr()
        print("Playing....")
        pass        
    elif choice == 4:
        # Skip to the next song on the playlist
        # Display song name that is now playing
        skip()
        print("Skipping....")
        pass                     
    elif choice == 5:
        # Go back to the previous song on the playlist
        # Display song name that is now playing
        prev_node()
        print("Replaying....")
        pass  
    elif choice == 6:
        # Randomly shuffle the playlist and play the first song
        # Display song name that is now playing
        # shuffle()
        # pass
    
        import random
        
        def shuffle(nSongs):
    
            # Loop over the range of indexes from 0 up to the length of the list:

                for i in range(len(nSongs) -1):

                # Randomly pick an index to swap with:

                    indexChange = random.randint(0, len(nSongs) -1)

                # Swap the nSongs between the two indexes:

                    nSongs[i], nSongs[indexChange] = nSongs[indexChange], nSongs[i]

                return nSongs #return Song list sorted

        
        s1 = Song("Purple Rain", "by Prince")
        s2 = Song("Beat It", "by Michael Jackson")
        s3 = Song("The Way You Love Me", "by Marc Avon Evans")
        s4 = Song("Love Calls", "by Kem")
        s5 = Song("When I See You", "by Fantasia")
        s6 = Song("Love and Happiness", "by Al Green")
        nSongs = [s1, s2, s3, s4, s5, s6]#  strings
        print(shuffle(nSongs))
        print("Shuffling....")          
    elif choice == 7:
        # Display the song name and artist of the currently playing song
        print("Currently playing: ", end=" ")    
    elif choice == 8:
        # Show the current song list order
        print(shuffle(nSongs))
        print("\nSong list:\n")
    elif choice == 0:
        print("Goodbye.")
        break

            
