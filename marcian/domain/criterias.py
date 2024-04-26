import domain.helper

def sortByLastName(a,b,help = None):
    '''
    Returns True is the last name of the object a is greater than the last name of the object b
    :param a: object
    :param b: object
    :param help: None
    :return:
    '''
    if a.getLastName() > b.getLastName():
        return True
    return False

def sortByLen(a,b,help = None):
    '''
    Returns true if the length of a is greater than the length of b
    :param a: list of objects
    :param b: list of objects
    :param help: None
    :return:
    '''
    if len(a.getListOfPassengers()) > len(b.getListOfPassengers()):
        return True
    return False

def sortByStartingSubstring(a,b,subString):
    '''
    Returns true if the number of passengers in a that have their first name starting with subString is
    greater than the number of passengers in b that have their first name starting with subString
    :param a: plane object
    :param b: plane object
    :param subString: string
    :return:
    '''
    result1 = 0
    for i in range(len(a.getListOfPassengers())):
        if a.getListOfPassengers()[i].getFirstName()[0:len(subString)] == subString:
            result1 += 1
    result2 = 0
    for i in range(len(b.getListOfPassengers())):
        if b.getListOfPassengers()[i].getFirstName()[0:len(subString)] == subString:
            result2 += 1
    if result1 > result2:
        return True
    return False

def sortByConcatenation(a,b, help = None):
    '''
    Returns true if the string obtained by concatenation of the number of passengers
    in the plane and the destination of a is greater than
    the string obtained by concatenation of the number of passengers in the
    plane and the destination of b
    :param a:
    :param b:
    :param help:
    :return:
    '''
    myString1 = str(len(a.getListOfPassengers())) + a.getDestination()
    myString2 = str(len(b.getListOfPassengers())) + b.getDestination()
    if myString1 > myString2:
        return True
    return False

def findByFirst3(a, help = None):
    '''
    Returns true if there are at least 2 passengers in the plane that have the first
    3 digits of their passport numbers the same
    :param a: plane object
    :param help:
    :return:
    '''
    for i in range(len(a.getListOfPassengers()) - 1):
        for j in range(i + 1, len(a.getListOfPassengers())):
            myList1 = domain.helper.makeIntList(a.getListOfPassengers()[i].getPassNumber())
            myList2 = domain.helper.makeIntList(a.getListOfPassengers()[j].getPassNumber())
            if myList2[0:3] == myList1[0:3]:
                return True
    return False

def findByString(a, subString):
    '''
    Returns true if a substring is in the first or last name of a
    :param a: passenger object
    :param subString: string
    :return:
    '''
    if subString in a.getFirstName() or subString in a.getLastName():
        return True
    return False

def findByName(a, name):
    '''
    Returns true if a person has the same name as a given name
    :param a: plane object
    :param name: string
    :return:
    '''
    name = name.split()
    for elem in a.getListOfPassengers():
        if elem.getFirstName() == name[0] and elem.getLastName() == name[1]:
            return True
    return False