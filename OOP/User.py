class User:
    firstName=""
    lastName=""
    userName=""
    password=""

    def __init__(self, fname, lname,uName,pas):
        self.firstName = fname
        self.lastName = lname
        self.userName = uName
        self.password = pas


    #@abstractmethod
    def signIn(uname,pass):
        pass
    #@abstractmethod
    def signOut():
        pass

    def getProfile():
        pass

