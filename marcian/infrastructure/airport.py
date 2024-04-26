import domain.helper
import domain.criterias
from domain.plane import Plane
from domain.passenger import Passenger


class Airport:
    '''
    Airport class (repository with planes)
    '''
    def __init__(self):
        self.__data = []

    def getSize(self):
        '''
        Gets the size
        :return:
        '''
        return len(self.__data)

    def add(self,plane):
        '''
        Adds a plane to the airport
        :param plane:
        :return:
        '''
        self.__data.append(plane)

    def getAllPlanes(self):
        '''
        Gets all planes
        :return:
        '''
        return self.__data[:]

    def deletePlaneAtIndex(self,index):
        '''
        Deletes plane at index
        :param index:
        :return:
        '''
        if domain.helper.isInt(index):
            if index >= 0 and index < len(self.__data):
                del(self.__data[index])
            else:
                raise ValueError("Invalid index!")
        else:
            raise ValueError("Invalid index!")

    def __repr__(self):
        return str(self.__data)

    # done
    def sortPassengersByLastName(self, index):
        '''
        Sorts the patients in a given department by code
        :param index: int
        :return:
        '''
        if domain.helper.isInt(index):
            if index >= 0 and index < len(self.__data):
                domain.helper.bubbleSort(self.__data[index].getListOfPassengers(), domain.criterias.sortByLastName)
            else:
                raise ValueError("Invalid index!")
        else:
            raise ValueError("Invalid index!")

    # done
    def sortPlanesByNumberOfPassengers(self):
        '''
        Sorts the planes by number of passengers
        :return:
        '''
        if len(self.__data) == 0:
            raise ValueError("Can't sort an empty airport!")
        else:
            domain.helper.bubbleSort(self.__data, domain.criterias.sortByLen)

    # done
    def sortByNumberOfPassengersFirstName(self, startingSubstring):
        if len(self.__data) == 0:
            raise ValueError("Can't sort an empty airport!")
        else:
            domain.helper.bubbleSort(self.__data, domain.criterias.sortByStartingSubstring, startingSubstring)

    # done
    def sortPlanesAccordingToConcatenation(self):
        '''
        Sort planes according to the string obtained by concatenation of the number of passengers in the plane and the destination
        :return:
        '''
        if len(self.__data) == 0:
            raise ValueError("Can't sort an empty airport!")
        else:
            return domain.helper.bubbleSort(self.__data,domain.criterias.sortByConcatenation)

    # done
    def identifyByPassengerFirst3(self):
        '''
        Identify  planes  that  have  passengers  with  passport  numbers  starting  with  the  same 3 letters
        :return:
        '''
        if len(self.__data) == 0:
            raise ValueError("Can't search an empty airport!")
        else:
            return domain.helper.search(self.__data,domain.criterias.findByFirst3)

    # done
    def identifyByNameContainingString(self,index,containString):
        '''
        Identify passengers from a given plane for which the first name or last name contain a given string
        :param index: int
        :param containString: string
        :return:
        '''
        if len(self.__data) == 0:
            raise ValueError("Can't search an empty airport!")
        else:
            if domain.helper.isInt(index):
                if index >= 0 and index < len(self.__data):
                    return domain.helper.search(self.__data[index].getListOfPassengers(), domain.criterias.findByString,
                                                containString)
                else:
                    raise ValueError("Invalid index!")
            else:
                raise ValueError("Invalid index!")

    # done
    def identifyPlaneByPassengerName(self, name):
        '''
        Identify plane/planes where there are passengers with a given name
        :param name: string
        :return:
        '''
        if len(self.__data) == 0:
            raise ValueError("Can't search an empty airport!")
        else:
            return domain.helper.search(self.__data, domain.criterias.findByName, name)
