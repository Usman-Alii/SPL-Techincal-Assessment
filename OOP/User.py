class User:
    __firstName=""
    __lastName=""
    __userName=""
    __password=""
    __isSignedIn=False

    def __init__(self, fname, lname,uName,pas):
        self.__firstName = fname
        self.__lastName = lname
        self.__userName = uName
        self.__password = pas


    #@abstractmethod
    def signIn(uname,pass):
        
        pass
    #@abstractmethod
    def signOut():
        pass

    def getProfile():
        pass

