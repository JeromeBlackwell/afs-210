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
        
class Mediaplayer:
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
    def getSize(self) -> int:
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
    

    def delete(self, title) -> None:
        # Delete a node from the list who's value matches the supplied value
        current = self.head
        prev = self.head
        while current:
            if current.title == title:
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
    
    # def append(value): 
    #     let  = (value)
    #     if let current = last 
    #         newNode.previous = M
    #         lastNode.next = newNode
    #     else: 
    #         head = newNode

    def shuffle(self):
        
        mediaplayer = []
        curr = self.head
        for count in range(0,self.getSize() + 1):
            mediaplayer.append(curr)
            curr = curr.next
            return

        # # Loop over the range of indexes from 0 up to the length of the list:

        for i in range(0, self.getSize() -1):
            print(self[i])
            # Randomly pick an index to swap with:

            indexChange = random.randint(0, len(mediaplayer))

             # Swap the mediaplayer between the two indexes:

            mediaplayer[i], mediaplayer[indexChange] = mediaplayer[indexChange], mediaplayer[i]


        
        # curr = Song(mediaplayer[0].title, mediaplayer[0].artist)
        # for count in range(0,len(mediaplayer)):
        #     curr.next = Song(mediaplayer[count].title, mediaplayer[count].artist)
        #     curr = curr.next
        # self.tail = curr
        # return self.head
        

    def __str__(self):
        myStr = ""
        for node in self.iter():
            myStr += str(node)+ "\n"
            
        return myStr

    # def __getitem__(self, index):
        
    #     return list(self)[index]
    
       
    
   
    
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

mediaplayer = Mediaplayer()
mediaplayer.addSong("Purple Rain", "Prince")
mediaplayer.addSong("Beat It", "Michael Jackson")
mediaplayer.addSong("The Way You Love Me", "Marc Avon Evans")
mediaplayer.addSong("Love Calls", "Kem")
mediaplayer.addSong("Love And Happiness", "Al Green")
mediaplayer.addSong("When I See You", "Fantasia")

while True:
    menu()
    choice = int(input())

    if choice == 1:
        # Add code to prompt user for Song Title and Artist Name
        # Add song to playlist
        songTitle = input("Song Name: ")
        songArtist = input("Artist Name: ")
        mediaplayer.addSong(songTitle, songArtist)
        print("New Song Added to Playlist")
        
    elif choice == 2:
        # Prompt user for Song Title 
        # remove song from playlist
        songTitle = input("Song Name: ")
        mediaplayer.delete(songTitle)
        print("Song Removed to Playlist")
        
    elif choice == 3:
        # Play the playlist from the beginning
        # Display song name that is currently playing
        mediaplayer.play(songTitle)        
        print("Playing....")
               
    elif choice == 4:
        # Skip to the next song on the playlist
        # Display song name that is now playing
        song = 0

        for song in range():
            if choice == 4:
                break
            
        print("Skipping....")
        pass

    elif choice == 5:
        # Go back to the previous song on the playlist
        # Display song name that is now playing
        mediaplayer.prev(songTitle)
        print("Replaying....")
        pass  
    elif choice == 6:
        # Randomly shuffle the playlist and play the first song
        # Display song name that is now playing
        mediaplayer.shuffle()
        print("Shuffling....")    
    elif choice == 7:
        # Display the song name and artist of the currently playing song
        print("Currently playing: ", end=" ")    
    elif choice == 8:
        # Show the current song list order
        # print(shuffle(mediaplayer))
        print("\nSong list:\n")
        print (mediaplayer)
    elif choice == 0:
        print("Goodbye.")
        break




         
    