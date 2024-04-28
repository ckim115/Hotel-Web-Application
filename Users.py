class Users():
    def __init__(self, email, password):
        self.email = email
        self.password = password

    def getEmail(self):
        return self.email

    def setEmail(self, newEmail):
        self.email = newEmail

    def setPassword(self, newPassword):
        self.password = password