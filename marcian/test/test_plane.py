from unittest import TestCase
from domain.plane import Plane
from domain.passenger import Passenger

class TestPlane(TestCase):
    def setUp(self):
        self.__p = Plane(1, "Ryanair", 3, "Dubai", [Passenger("Dwane", "Jhonson", 12345),
                                                    Passenger("Kevin", "Hart", 23456)])

    def testInit(self):
        self.assertEqual(str(self.__p), "(1, Ryanair, 3, Dubai, [(Dwane Jhonson, 12345), (Kevin Hart, 23456)])")

    def testGetters(self):
        self.assertEqual(self.__p.getNumber(), 1)
        self.assertEqual(self.__p.getAirline(), "Ryanair")
        self.assertEqual(self.__p.getNumberOfSeats(), 3)
        self.assertEqual(str(self.__p.getListOfPassengers()), "[(Dwane Jhonson, 12345), (Kevin Hart, 23456)]")

    def testSetters(self):
        self.assertRaises(ValueError, self.__p.setNumber, 'a')
        self.__p.setAirline("Wizzair")
        self.assertEqual(self.__p.getAirline(), "Wizzair")
        self.assertRaises(ValueError, self.__p.setNumberOfSeats, 'a')

    def testAddPassenger(self):
        self.__p.addPassenger(Passenger("Blake", "Lively", 34567))
        self.assertEqual(str(self.__p.getListOfPassengers()), "[(Dwane Jhonson, 12345), (Kevin Hart, 23456), (Blake Lively, 34567)]")

    def testUpdatePatientAtIndex(self):
        self.assertRaises(ValueError, self.__p.updatePassengerAtIndex, 5, "Salma", "Hayek", 45678)
        self.__p.updatePassengerAtIndex(1, "Salma", "Hayek", 45678)
        self.assertEqual(str(self.__p.getListOfPassengers()), "[(Dwane Jhonson, 12345), (Salma Hayek, 45678)]")
        self.assertRaises(ValueError, self.__p.updatePassengerAtIndex, 1, "Salma", "Hayek", 'a')

    def testDeleteAtIndex(self):
        self.assertRaises(ValueError, self.__p.deleteAtIndex, 6)
        self.__p.deleteAtIndex(1)
        self.assertEqual(str(self.__p.getListOfPassengers()), "[(Dwane Jhonson, 12345)]")
