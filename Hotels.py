import csv

class Hotels():
    def __init__(self, name, address, description, avgRoomCost, hotelLink, reviews):
        self.name = name
        self.address = address
        self.description = description
        self.avgRoomCost = avgRoomCost
        self.hotelLink = hotelLink
        self.reviews = reviews

    def printHotelInfo(self):
        print("Name:", self.name)
        print("Address:", self.address)
        print("Description:", self.description)
        print("Average cost per room: $", self.avgRoomCost)
        print("Link to the hotels website:", self.hotelLink)
        print("This hotel has a review rating of:", self.reviews, "/5")

    def getName(self):
        return self.name

    def getAddress(self):
        return self.address

    def getDescription(self):
        return self.description

    def getAvgCost(self):
        return self.avgRoomCost

    def getHotelLink(self):
        return self.hotelLink

    def getReviews(self):
        return self.reviews

#hotel1 = Hotels("Hotel De Anza", "Cupertino", "Great hotel of De Anza", 120, "www.DeAnzaHotel.com", 4.1)
#hotel1.printHotelInfo()

hotelList = list()
with open('list_of_nearby_hotels.csv', mode='r') as file:
    csvFile = csv.reader(file)
    i = 0
    for lines in csvFile:
        if lines[5] == "name": # ignore csv file format / basically checking if name of hotel is name
            continue
        else:
            tempHotel = "hotel"+str(i)
            tempHotel = Hotels(lines[5], lines[15], "Great hotel", 408+i, "www."+lines[5]+".com", lines[10])
            hotelList.append(tempHotel)
            i += 1

#print(hotelList) prints all hotel objects

for hotel in hotelList:
    hotel.printHotelInfo()
    print() # spacer in between hotel prints