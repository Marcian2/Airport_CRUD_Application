from domain.passenger import Passenger
import domain.helper


class Plane:
    '''
    Plane class with number, airline, number of seats, list of passengers
    '''
    def __init__(self, number, airline, numberOfSeats,destination,listOfPassengers):
        if domain.helper.isInt(number):
            self.__number = number
        else:
            raise ValueError("Must be int!")
        self.__airline = airline
        if domain.helper.isInt(numberOfSeats):
            self.__numberOfSeats = numberOfSeats
        else:
            raise ValueError("Must be int!")
        self.__destination = destination
        if len(listOfPassengers) <= numberOfSeats:
            self.__listOfPassengers = listOfPassengers[:]
        else:
            raise ValueError("Not enough seats!")

    # Getters
    def getNumber(self):
        '''
        Gets number
        :return:
        '''
        return self.__number

    def getAirline(self):
        '''
        Gets airline
        :return:
        '''
        return self.__airline

    def getNumberOfSeats(self):
        '''
        Gets number of seats
        :return:
        '''
        return self.__numberOfSeats

    def getDestination(self):
        '''
        Gets the destination
        :return:
        '''
        return self.__destination

    def getListOfPassengers(self):
        '''
        Gets list of passengers
        :return:
        '''
        return self.__listOfPassengers

    # Setters
    def setNumber(self, newNumber):
        '''
        Sets number
        :param newNumber: int
        :return:
        '''
        if domain.helper.isInt(newNumber):
            self.__number = newNumber
        else:
            raise ValueError("Must be int!")

    def setAirline(self,newAirline):
        '''
        Sets airline
        :param newAirline: string
        :return:
        '''
        self.__airline = newAirline

    def setNumberOfSeats(self, newNumberOfSeats):
        '''
        Sets number of seats
        :param newNumberOfSeats: int
        :return:
        '''
        if domain.helper.isInt(newNumberOfSeats):
            self.__numberOfSeats = newNumberOfSeats
        else:
            raise ValueError("Must be int!")

    def setDestination(self, newDestination):
        '''
        Sets destination
        :param newDestination: string
        :return:
        '''
        self.__destination = newDestination

    def addPassenger(self, passenger):
        '''
        Adds a passenger
        :param passenger: Passenger object
        :return:
        '''
        if len(self.__listOfPassengers) < self.__numberOfSeats:
            self.__listOfPassengers.append(passenger)
        else:
            raise ValueError("Not enough beds!")

    def updatePassengerAtIndex(self,index,newFirstName,newLastName,newPassNumber):
        '''
        Updates passenger at index
        :param index: int
        :param newFirstName: string
        :param newLastName: string
        :param newPassNumber: int
        :return:
        '''
        if domain.helper.isInt(index):
            if index >= 0 and index < len(self.__listOfPassengers):
                self.__listOfPassengers[index].setFirstName(newFirstName)
                self.__listOfPassengers[index].setLastName(newLastName)
                if domain.helper.isInt(newPassNumber):
                    self.__listOfPassengers[index].setPassNumber(newPassNumber)
                else:
                    raise ValueError("Invalid passport number!")
            else:
                raise ValueError("Invalid index!")
        else:
            raise ValueError("Invalid index!")

    def deleteAtIndex(self,index):
        '''
        Deletes passenger at index
        :param index: int
        :return:
        '''
        if domain.helper.isInt(index):
            if index >= 0 and index < len(self.__listOfPassengers):
                del(self.__listOfPassengers[index])
            else:
                raise ValueError("Invalid index!")
        else:
            raise ValueError("Invalid index!")

    def __repr__(self):
        return "(" + str(self.__number) + ", " + self.__airline + ", " + str(self.__numberOfSeats) + ", " + self.__destination + ", " + str(self.__listOfPassengers) + ")"
