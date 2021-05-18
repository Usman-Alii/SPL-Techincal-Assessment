import User
class Instructor(User):
    __designation=None
    __qulaification=None

    def __init__(self, des, qual):
        self.__designation = des
        self.__age = qual

    def signIn(uName,pas):
        #defination
        User.__isSignedIn=True    #after authenticating from database

    def signOut():
        #defination
        User.__isSignedIn=False

    def addMarksOfStudents():
        #defination
        pass

    def viewMarksOfStudents():
        #defination
        pass

    def addResources():
        #defination
        pass

    def viewResources():
        #defination
        pass

    def viewRoaster():
        #defination
        pass

    def addAssignments():
        #defination
        pass

    def viewAssignments():
        #defination
        pass


    def getProfile():
        pass

