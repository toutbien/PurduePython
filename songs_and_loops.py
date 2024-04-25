#Attributes for dictionary
song = {
  "title1':"Uptown Funk"
  "artist1":"Bruno Mars"
  "genre1":"pop, funk"
  "album1":"Doo-Wops & Hooligans"
  "year1": "2008"
}


#Ask how many songs
#loop to prompt for the value of a song
#add a song to the dictionary

#print the loop for each song
myList=[]

#numNames = int(input("Enter Number of Names: "))
while True:
    mySong = {}
    name = input("Enter name or blank to exit: ")
    if name == "":
      break
    titlein = input("Enter song title: ")
    artistin = input("Enter artist: ")
    yearin = int(input("Enter the year: "))
    mySong["title"] = titlein 
    mySong["artist"] = artistin
    mySong["year"] = yearin
    myList.append(mySong)

for each Song in myList:
  print(entry)

for entry in myList:
for attribute in entry.values:
    print(attribute[0], ".",attribute[1])

print("Thanks for playing!!")
