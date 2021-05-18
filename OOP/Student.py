import User
class Student(User):
    rollNo=None
    status=None

    def __init__(self, rolno, stats,fName,lName,uName,pas):
        self.rollNo = rolno
        self.status = stats
        User.__init__(fName,lName,uName,pas)
    def signIn():
        #defination
        pass

    def signOut():
        #defination
        pass

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
        print(self.status)