import json
def insert(arr):
    ## might have to make list3 = [fixed, arr] ; then list3 = arr, return arr
    for pos in range(1, len(arr)):
        val = arr[pos]

        while pos > 0 and arr[pos - 1] > val:
            arr[pos] = arr[pos - 1]
            pos = pos - 1
        arr[pos] = val
    return arr
def contains(arr, item):
    for element in arr:
        if element == item:
            return True
    
    return False
def binery(arr, item):
    low = 0
    hi = len(arr) - 1
    ## looooop
    
    while low <= hi:
        miInd = (low + hi) // 2
        if arr[miInd] == item:
            return item, miInd
        elif item > arr[miInd]:
            low = miInd + 1
        else:
            hi = miInd - 1
            
    return -1

def linear(arr, element):
    counter = 0
    for i in range(len(arr)):
        if arr[i] != element:
            counter += 1
        if arr[i] == element:
            return counter
        if counter == len(arr):
            return -1

file = open("musicdata.json", "r")
dataStr = file.read()
file.close()

library = []
## months
January = 1
February = 2
March = 3
April = 4
May = 5
June = 6
July = 7
August = 8
September = 9 
October = 10
November = 11
December = 12
tracklist = json.loads(dataStr)
loop = True
while loop:
    ### MENU
    print("1: Show Catalogue")
    print("2: Search song or artist by keyword")
    print("3: Browse all songs of a chosen genre")
    print("4: Sort songs by oldest to newest")
    print("5: Add or Revmove songs from the library")
    print("6: Display Library")
    print("7: Exit SoulCloud")

    runfun = input("What would you like to do?")
    if runfun == "1":
        for song in tracklist:
            print(song["name"], {song["artist"]})
    elif runfun == "2":
        print("---------Hello-----------")
        search = input('search by artist, song or keyword. press 1 to see all keywords')
        if search == "1":
            print("Rap , RnB/Soul , Jazz , Rock")
        else:
            for song in tracklist:
                if song["name"] == search:
                    print(song)
                elif song["artist"] == search:
                    print(song)
                elif song["genre"] == search:
                    print(song)            
    elif runfun == "3":
        print("1: Rock")
        print("2: Jazz")
        print("3: Rnb/Soul")
        print("4: Rap")
        ques = input("Which genre would you like to browse")
        if  ques == "1":
            for song in tracklist:
                if song["genre"] == "Rock":
                    print(song["name"], song["artist"], song["genre"])
        elif  ques == "2":
            for song in tracklist:
                if song["genre"] == "Jazz":
                    print(song["name"], song["artist"], song["genre"])
        elif  ques == "3":
            for song in tracklist:
                if song["genre"] == "RnB/Soul":
                    print(song["name"], song["artist"], song["genre"])
        elif  ques == "4":
            for song in tracklist:
                if song["genre"] == "Rap":
                    print(song["name"], song["artist"])
    elif runfun == "4":
        arr = []
        for song in tracklist:
            var = song["releasedate"]
            arr.append(var)
        insert(arr)
        for ele in arr:
            for song in tracklist:
                if ele == song["releasedate"]:
                    print(song["name"] + ",  " + song["artist"] + "-" + song["releasedate"])

            
    elif runfun == "5":
        ques = input("which song would you like to add to your library?(song name)")
        for song in tracklist:
            if ques == song["name"]:
                library.append(song)
        print(library)
    elif runfun == "6":
        print(library)
    elif runfun == "7":
        print("7")
        loop = False
    
            
