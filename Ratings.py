class Ratings():
    def __init__(self, title, published_date, rating, text):
        self.title = title
        self.published_date = published_date
        self.rating = rating
        self.text = text

    def printRatingInfo(self):
        print("Title:", self.title)
        print("Date:", self.published_date)
        print("Rating:", self.rating, "/5")
        print("Text", self.text)

    def getTitle(self):
        return self.title

    def getPublishDate(self):
        return self.published_date

    def getRating(self):
        return self.rating

    def getText(self):
        return self.text