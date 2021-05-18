class Assignments:
    __AssignmentId=None
    __AssignmentDescription=None
    __assignedTo=None
    __assignedBy=None

    def __init__(self, id, des,assignTo,assignBy):
        self.__AssignmentId = id
        self.__AssignmentDescription = des
        self.__assignedTo = assignTo
        self.__assignedBy =assignBy
