from unittest import TestCase
from domain.passenger import Passenger

class TestPassenger(TestCase):
    def setUp(self):
        self.__p = Passenger("Dwane", "Jhonson", 12345)

    def testInit(self):
        self.assertEqual(str(self.__p), "(Dwane Jhonson, 12345)")

    def testGetters(self):
        self.assertEqual(self.__p.getFirstName(), "Dwane")
        self.assertEqual(self.__p.getLastName(), "Jhonson")
        self.assertEqual(self.__p.getPassNumber(), 12345)

    def testSetters(self):
        self.__p.setFirstName("Kevin")
        self.assertEqual(self.__p.getFirstName(), "Kevin")
        self.__p.setLastName("Hart")
        self.assertEqual(self.__p.getLastName(), "Hart")
        self.__p.setPassNumber(23456)
        self.assertEqual(self.__p.getPassNumber(), 23456)