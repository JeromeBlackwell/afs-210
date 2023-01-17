import random

class Song:
    # A doubly-linked node.
    def __init__(self,title,artist):
        self.title = title
        self.artist = artist
        self.next = None
        self.prev = None

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
        
class mediaplayer:
    def __init__(self):
        # Create an empty list.
        self.head = None             
        self.tail = None       
        self.count = 0
    def iter(self):
        # Iterate through the list.
        current = self.head
        while current:
            val = current
            current = current.next
            yield val
    def size(self) -> int:
        # Returns the number of elements in the list
        return self.count
    def addSong(self, title, artist) -> None:
        # Add a node at the end of the list
        
        new_node = Song(title,artist)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.count += 1
    
    def delete(self, title, artist) -> None:
        # Delete a node from the list who's value matches the supplied value
        current = self.head
        prev = self.head
        while current:
            if current == Song:
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
    def __str__(self):
        myStr = ""
        for node in self.iter():
            myStr += str(node)+ " "
        return myStr

    def shuffle(nSongs):
    
        # Loop over the range of indexes from 0 up to the length of the list:

        for i in range(len(nSongs) -1):

            # Randomly pick an index to swap with:

            indexChange = random.randint(0, len(nSongs) -1)

             # Swap the nSongs between the two indexes:

            nSongs[i], nSongs[indexChange] = nSongs[indexChange], nSongs[i]

        return nSongs(nSongs) #return Song list sorted
    
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


# while True:
#     menu()
#     choice = int(input())

#     if choice == 1:
#         # Add code to prompt user for Song Title and Artist Name
#         # Add song to playlist
#         # def addTitleArtist(self,val):
#         #     self.head = Node(val)
#         #     while current.next != None:
#         #         current = current.next
#         #     newTitleArtist = Node(val)
#         #     current.next = newTitleArtist
#         #     newTitleArtist.prev = current
#         #     self.tail = newTitleArtist
#         print("New Song Added to Playlist")
#         pass
#     elif choice == 2:
#         # Prompt user for Song Title 
#         # remove song from playlist
#         delete()
#         print("Song Removed to Playlist")
#         pass
#     elif choice == 3:
#         # Play the playlist from the beginning
#         # Display song name that is currently playing
#         play_curr()
#         print("Playing....")
#         pass        
#     elif choice == 4:
#         # Skip to the next song on the playlist
#         # Display song name that is now playing
#         skip()
#         print("Skipping....")
#         pass                     
#     elif choice == 5:
#         # Go back to the previous song on the playlist
#         # Display song name that is now playing
#         prev_node()
#         print("Replaying....")
#         pass  
#     elif choice == 6:
#         # Randomly shuffle the playlist and play the first song
#         # Display song name that is now playing
#         # shuffle()
#         # pass
    
        
        
#         
        
           
#     elif choice == 7:
#         # Display the song name and artist of the currently playing song
#         print("Currently playing: ", end=" ")    
#     elif choice == 8:
#         # Show the current song list order
#         print(shuffle(nSongs))
#         print("\nSong list:\n")
#     elif choice == 0:
#         print("Goodbye.")
#         break

mediaplayer = mediaplayer()
mediaplayer.addSong("Purple Rain", "Prince")
mediaplayer.addSong("Beat It", "Michael Jackson")
mediaplayer.addSong("The Way You Love Me", "Marc Avon Evans")
mediaplayer.addSong("Love Calls", "Kem")
mediaplayer.addSong("Love And Happiness", "Al Green")
mediaplayer.addSong("When I See You", "Fantasia")
print(mediaplayer)
# s1 = Song("Purple Rain", "Prince")
# s2 = Song("Beat It", "Michael Jackson")
# s3 = Song("The Way You Love Me", "Marc Avon Evans")
# s4 = Song("Love Calls", "Kem")
# s5 = Song("When I See You", "Fantasia")
# s6 = Song("Love and Happiness", "Al Green")
# nSongs = [s1, s2, s3, s4, s5, s6]#  strings
# # print(shuffle(nSongs))
# print("Shuffling....")

         
    