from unittest import TestCase
from infrastructure.airport import Airport
from domain.plane import Plane
from domain.passenger import Passenger

class TestAirport(TestCase):
    def setUp(self):
        self.__a = Airport()

    def testInit(self):
        self.assertEqual(str(self.__a), "[]")

    def testAdd(self):
        self.__a.add(Plane(1, "Ryanair", 3, "Dubai", [Passenger("Dwane", "Jhonson", 12345),
                                             Passenger("Kevin", "Hart", 23456)]))
        self.assertEqual(str(self.__a), "[(1, Ryanair, 3, Dubai, [(Dwane Jhonson, 12345), (Kevin Hart, 23456)])]")
        self.__a.add(Plane(2, "Wizzair", 4, "London", [Passenger("Blake", "Lively", 34567),
                                          Passenger("Salma", "Hayek", 45678)]))
        self.assertEqual(str(self.__a), "[(1, Ryanair, 3, Dubai, [(Dwane Jhonson, 12345), (Kevin Hart, 23456)]), (2, Wizzair, 4, London, [(Blake Lively, 34567), (Salma Hayek, 45678)])]")

    def testSortPassengersByLastName(self):
        self.__a.add(Plane(1, "Ryanair", 3, "Dubai", [Passenger("Dwane", "Jhonson", 12345),
                                             Passenger("Kevin", "Hart", 23456)]))
        self.__a.sortPassengersByLastName(0)
        self.assertEqual(str(self.__a.getAllPlanes()), "[(1, Ryanair, 3, Dubai, [(Kevin Hart, 23456), (Dwane Jhonson, 12345)])]")
        self.__a.add(Plane(2, "Wizzair", 4, "London", [Passenger("Blake", "Lively", 34567),
                                          Passenger("Salma", "Hayek", 45678)]))
        self.__a.sortPassengersByLastName(0)
        self.assertEqual(str(self.__a.getAllPlanes()), "[(1, Ryanair, 3, Dubai, [(Kevin Hart, 23456), (Dwane Jhonson, 12345)]), (2, Wizzair, 4, London, [(Blake Lively, 34567), (Salma Hayek, 45678)])]")

    def testSortPlanesByNumberOfPassengers(self):
        self.assertRaises(ValueError, self.__a.sortPlanesByNumberOfPassengers)
        self.__a.add(Plane(1, "Ryanair", 3, "Dubai", [Passenger("Dwane", "Jhonson", 12345),
                                             Passenger("Kevin", "Hart", 23456), Passenger("Gal", "Gadot", 54321)]))
        self.__a.add(Plane(2, "Wizzair", 4, "London", [Passenger("Blake", "Lively", 34567),
                                          Passenger("Salma", "Hayek", 45678)]))
        self.__a.sortPlanesByNumberOfPassengers()
        self.assertEqual(str(self.__a.getAllPlanes()), "[(2, Wizzair, 4, London, [(Blake Lively, 34567), (Salma Hayek, 45678)]), (1, Ryanair, 3, Dubai, [(Dwane Jhonson, 12345), (Kevin Hart, 23456), (Gal Gadot, 54321)])]")

    def testSortByNumberOfPassengersFirstName(self):
        self.assertRaises(ValueError, self.__a.sortByNumberOfPassengersFirstName, "Dwa")
        self.__a.add(Plane(1, "Ryanair", 3, "Dubai", [Passenger("Dwane", "Jhonson", 12345),
                                             Passenger("Dwayne", "Hart", 23456)]))
        self.__a.add(Plane(2, "Wizzair", 4, "London", [Passenger("Blake", "Lively", 34567),
                                          Passenger("Salma", "Hayek", 45678)]))
        self.__a.sortByNumberOfPassengersFirstName("Dwa")
        self.assertEqual(str(self.__a.getAllPlanes()), "[(2, Wizzair, 4, London, [(Blake Lively, 34567), (Salma Hayek, 45678)]), (1, Ryanair, 3, Dubai, [(Dwane Jhonson, 12345), (Dwayne Hart, 23456)])]")

    def testSortPlanesAccordingToConcatenation(self):
        self.assertRaises(ValueError, self.__a.sortPlanesAccordingToConcatenation)
        self.__a.add(Plane(2, "Wizzair", 4, "London", [Passenger("Blake", "Lively", 34567),
                                          Passenger("Salma", "Hayek", 45678)]))
        self.__a.add(Plane(1, "Ryanair", 3, "Dubai", [Passenger("Dwane", "Jhonson", 12345),
                                             Passenger("Kevin", "Hart", 23456)]))
        self.__a.sortPlanesAccordingToConcatenation()
        self.assertEqual(str(self.__a.getAllPlanes()), "[(1, Ryanair, 3, Dubai, [(Dwane Jhonson, 12345), (Kevin Hart, 23456)]), (2, Wizzair, 4, London, [(Blake Lively, 34567), (Salma Hayek, 45678)])]")

    def testIdentifyByPassengerFirst3(self):
        self.assertRaises(ValueError, self.__a.identifyByPassengerFirst3)
        self.__a.add(Plane(1, "Ryanair", 3, "Dubai", [Passenger("Dwane", "Jhonson", 12345), Passenger("Kevin", "Hart", 12356)]))
        self.__a.add(Plane(2, "Wizzair", 4, "London", [Passenger("Blake", "Lively", 34567),
                                          Passenger("Salma", "Hayek", 45678)]))
        self.assertEqual(str(self.__a.identifyByPassengerFirst3()), "[(1, Ryanair, 3, Dubai, [(Dwane Jhonson, 12345), (Kevin Hart, 12356)])]")

    def testIdentifyByNameContainingString(self):
        self.assertRaises(ValueError, self.__a.identifyByNameContainingString, 0, "Dwa")
        self.__a.add(Plane(1, "Ryanair", 3, "Dubai", [Passenger("Dwane", "Jhonson", 12345), Passenger("Kevin", "Hart", 12356)]))
        self.__a.add(Plane(2, "Wizzair", 4, "London", [Passenger("Blake", "Lively", 34567),
                                          Passenger("Salma", "Hayek", 45678)]))
        self.assertRaises(ValueError, self.__a.identifyByNameContainingString, 6, "Dwa")
        self.assertEqual(str(self.__a.identifyByNameContainingString(0, "Dwa")), "[(Dwane Jhonson, 12345)]")

    def testIdentifyPlaneByPassengerName(self):
        self.assertRaises(ValueError, self.__a.identifyPlaneByPassengerName, "Dwane Jhonson")
        self.__a.add(Plane(1, "Ryanair", 3, "Dubai", [Passenger("Dwane", "Jhonson", 12345),
                                             Passenger("Kevin", "Hart", 23456)]))
        self.__a.add(Plane(2, "Wizzair", 4, "London", [Passenger("Blake", "Lively", 34567),
                                          Passenger("Salma", "Hayek", 45678)]))
        self.assertEqual(str(self.__a.identifyPlaneByPassengerName("Blake Lively")), "[(2, Wizzair, 4, London, [(Blake Lively, 34567), (Salma Hayek, 45678)])]")