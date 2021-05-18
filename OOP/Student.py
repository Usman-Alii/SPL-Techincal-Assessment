import User
import Assignments
class Student(User):
    __rollNo=None
    __status=None
    __assignments=[]

    def __init__(self, rolno, stats,fName,lName,uName,pas):
        self.__rollNo = rolno
        self.__status = stats
        User.__init__(fName,lName,uName,pas)

    def signIn(uName,pas):
        
        User.__isSignedIn=True    #after authenticating from database


    def signOut():
        #defination
        User.__isSignedIn=False

    def viewMarks():
        #defination
        pass

    def viewResources():
        #defination
        pass

    def viewRoaster():
        #defination
        pass

    def viewAssignments():
        #defination
        pass

    def getProfile(self):
        print(self.__status)