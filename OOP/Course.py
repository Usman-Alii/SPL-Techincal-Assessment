class Course:

    __courseName=None
    __courseCode=None
    __offerSchool=None
    __capacity=None
    def __init__(self,courseName,courseCode,offeringSchool,capacity):
        self.__courseName=courseName
        self.__courseCode=courseCode
        self.__offeringSchool=offeringSchool
        self.__capacity=capacity
    