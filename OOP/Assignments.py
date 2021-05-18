class Assignments:
    AssignmentId=None
    AssignmentDescription=None
    assignedTo=None
    assignedBy=None

    def __init__(self, id, des,assignTo,assignBy):
        self.AssignmentId = id
        self.AssignmentDescription = des
        self.assignedTo = assignTo
        self.assignedBy =assignBy
