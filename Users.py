class Users():
    def __init__(self, firstname, lastname, email, password):
        self.__firstname = firstname
        self.__lastname = lastname
        self.__email = email
        self.__password = password

    def printInfo(self):
        print("Name: ", self.__firstname, self.__lastname)
        print("Email: ", self.__email)

user1 = Users("Bob", "Smith", "Bob@gmail.com", "password123")
user1.printInfo()