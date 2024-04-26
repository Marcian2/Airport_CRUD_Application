from domain.passenger import Passenger
from domain.plane import Plane

class AirportUI:
    '''
    AirportUI class that has a controller
    '''
    def __init__(self, ctrl):
        self.__ctrl = ctrl

    def __repr__(self):
        return str(self.__ctrl)

    @staticmethod
    def printMenu():
        '''
        Prints the menu
        :return:
        '''
        msg = "********** \n"
        msg += "\t Airport Menu: \n"
        msg += "\t 1 - View plane list \n"
        msg += "\t 2 - Add plane \n"
        msg += "\t 3 - Sort the passengers in a plane by last name \n"
        msg += "\t 4 - Sort planes according to the number of passengers \n"
        msg += "\t 5 - Sort planes according to the number of passengers with the first name starting with a given substring \n"
        msg += "\t 6 - Sort planes according to the string obtained by concatenation of the number of passengers in the plane and the destination \n"
        msg += "\t 7 - Identify planes that have passengers with passport numbers starting with the same 3 letters \n"
        msg += "\t 8 - Identify passengers from a given plane for which the first name or last name contain a string \n"
        msg += "\t 9 - Identify plane/planes where there is a passenger with given name \n"
        msg += "\t ********** \n"
        msg += "\t 0 - Exit"
        print(msg)

    @staticmethod
    def readPassenger():
        '''
        Reads passenger from the user
        :return:
        '''
        firstName = input("Enter the passenger's first name: ")
        lastName = input("Enter the passenger's last name: ")
        passNumber = int(input("Enter the passenger's passport number: "))
        return Passenger(firstName, lastName, passNumber)

    def readPlane(self):
        '''
        Reads plane from the user
        :return:
        '''
        listOfPassengers = []
        number = int(input("Enter the plane's number: "))
        airline = input("Enter the plane's airline: ")
        numberOfSeats = int(input("Enter the plane's number of seats: "))
        destination = input("Please enter the plane's destination: ")
        passengers = int(input("Enter the plane's number of passengers: "))
        for i in range(passengers):
            listOfPassengers.append(AirportUI.readPassenger())
        try:
            p = Plane(number, airline, numberOfSeats,destination, listOfPassengers)
        except ValueError as ve:
            print(ve)
        return Plane(number, airline, numberOfSeats,destination, listOfPassengers)

    def printPlaneList(self):
        '''
        Prints the plane list
        :return:
        '''
        print("Plane list is: ")
        for elem in self.__ctrl.getAllPlanes():
            print(elem)

    def start(self):
        '''
        Starts the application
        :return:
        '''
        option = None
        while True:
            try:
                AirportUI.printMenu()
                option = int(input("Enter an option: "))
                if option == 1:
                    self.printPlaneList()
                elif option == 2:
                    plane = self.readPlane()
                    self.__ctrl.addPlane(plane)
                elif option == 3:
                    index = int(input("Please enter the index: "))
                    self.__ctrl.sortPassengersByLastName(index)
                elif option == 4:
                    self.__ctrl.sortPlanesByNumberOfPassengers()
                elif option == 5:
                    firstName = input("Please enter the first name: ")
                    self.__ctrl.sortByNumberOfPassengersFirstName(firstName)
                elif option == 6:
                    self.__ctrl.sortPlanesAccordingToConcatenation()
                elif option == 7:
                    print(self.__ctrl.identifyByPassengerFirst3())
                elif option == 8:
                    index = int(input("Enter the index: "))
                    containingString = input("Enter the containing string: ")
                    print(self.__ctrl.identifyByNameContainingString(index,containingString))
                elif option == 9:
                    name = input("Enter the full name: ")
                    print(self.__ctrl.identifyPlaneByPassengerName(name))
                elif option == 0:
                    print("Goodbye!")
                    break
                else:
                    print("Invalid option!")
            except ValueError:
                print("Invalid type!")