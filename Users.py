class Users():
    def __init__(self, firstname, lastname, email, password):
        self.__firstname = firstname
        self.__lastname = lastname
        self.__email = email
        self.__password = password

    def printInfo(self):
        print("Name: ", self.__firstname, self.__lastname)
        print("Email: ", self.__email)

    def login(self, email, password):
        if self.__email == email and self.__password == password:
            return True
        elif self.__email != email:
            return "Wrong email"
        elif self.__password != password:
            return "Wrong password"
        else:
            return "Both email and password are incorrect"