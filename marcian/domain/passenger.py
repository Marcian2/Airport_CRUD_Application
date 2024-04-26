import domain.helper

class Passenger:
    '''
    Passenger class with first name, last name, passport number
    '''
    def __init__(self, firstName,lastName, passNumber):
        self.__firstName = firstName
        self.__lastName = lastName
        if domain.helper.isInt(passNumber):
            self.__passNumber = passNumber
        else:
            raise ValueError("Passport number must be int!")

    # Getters
    def getFirstName(self):
        '''
        Gets first name
        :return:
        '''
        return self.__firstName

    def getLastName(self):
        '''
        Gets last name
        :return:
        '''
        return self.__lastName

    def getPassNumber(self):
        '''
        Gets passport number
        :return:
        '''
        return self.__passNumber

    # Setters
    def setFirstName(self, newFirstName):
        '''
        Sets first name
        :param newFirstName: string
        :return:
        '''
        self.__firstName = newFirstName

    def setLastName(self, newLastName):
        '''
        Sets last name
        :param newLastName: string
        :return:
        '''
        self.__lastName = newLastName

    def setPassNumber(self, newPassNumber):
        '''
        Sets passport number
        :param newPassNumber: int
        :return:
        '''
        self.__passNumber = newPassNumber

    def __repr__(self):
        return "(" + self.__firstName + " " + self.__lastName + ", " + str(self.__passNumber) + ")"
