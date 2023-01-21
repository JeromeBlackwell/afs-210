import random

def shuffle(playList):
    
    # Loop over the range of indexes from 0 up to the length of the list:

    for i in range(len(playList) -1):

        # Randomly pick an index to swap with:

        indexChange = random.randint(0, len(playList) -1)

        # Swap the playList between the two indexes:

        playList[i], playList[indexChange] = playList[indexChange], playList[i]

    return playList  #return playList

play_List = DoublyLinkedList()
playList.add('Purple Rain by Prince') #0
playList.add('Beat It by Michael Jackson') #1
playList.add('The Way You Love Me by Marc Avon Evans') #2
playList.add('Love Calls by Kem') #3
playList.add('Love And Happiness by Al Green') #4
playList.add('When I See You by Fantasia') #5

print()
print(playList)


#Time complexity is: 0(n) - The Time Complexity of a loop is considered as O(n) since the iterations of the function grow with the size of the list.