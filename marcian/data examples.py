from domain.plane import Plane
from domain.passenger import Passenger
from infrastructure.airport import Airport

def dataExamples():
    a = Airport()
    # 1st data example
    a.add(Plane(1,"Ryanair", 3, "Dubai", [Passenger("Dwane", "Jhonson", 1234), Passenger("Kevin", "Hart", 2345), Passenger("Gal", "Gadot", 1235)]))
    # [(1, Ryanair, 3, Dubai, [(Dwane Jhonson, 1234), (Kevin Hart, 2345), (Gal Gadot, 1235)])]
    print(a)
    print()

    # 2nd data example
    a.sortPassengersByLastName(0)
    # [(1, Ryanair, 3, Dubai, [(Gal Gadot, 1235), (Kevin Hart, 2345), (Dwane Jhonson, 1234)])]
    print(a.getAllPlanes())
    print()

    # 3rd data example
    a.add(Plane(2,"Wizzair", 3,"London", [Passenger("Blake", "Lively", 4567), Passenger("Salma", "Hayek", 5678)]))
    # [(2, Wizzair, 3, London, [(Blake Lively, 4567), (Salma Hayek, 5678)]), (1, Ryanair, 3, Dubai, [(Gal Gadot, 1235), (Kevin Hart, 2345), (Dwane Jhonson, 1234)])]
    a.sortPlanesByNumberOfPassengers()
    print(a.getAllPlanes())
    print()

    # 4th data example
    a.sortByNumberOfPassengersFirstName("Dwa")
    # [(2, Wizzair, 3, London, [(Blake Lively, 4567), (Salma Hayek, 5678)]), (1, Ryanair, 3, Dubai, [(Gal Gadot, 1235), (Kevin Hart, 2345), (Dwane Jhonson, 1234)])]
    print(a.getAllPlanes())
    print()

    # 5th data example
    a.sortPlanesAccordingToConcatenation()
    # [(2, Wizzair, 3, London, [(Blake Lively, 4567), (Salma Hayek, 5678)]), (1, Ryanair, 3, Dubai, [(Gal Gadot, 1235), (Kevin Hart, 2345), (Dwane Jhonson, 1234)])]
    print(a.getAllPlanes())
    print()

    # 6th data example
    print(a.identifyByPassengerFirst3())
    # [(1, Ryanair, 3, Dubai, [(Gal Gadot, 1235), (Kevin Hart, 2345), (Dwane Jhonson, 1234)])]
    print()

    # 7th data example
    print(a.identifyByNameContainingString(1,"Dwa"))
    # [(Dwane Jhonson, 1234)]
    print()

    # 8th data example
    print(a.identifyPlaneByPassengerName("Dwane Jhonson"))
    # [(1, Ryanair, 3, Dubai, [(Gal Gadot, 1235), (Kevin Hart, 2345), (Dwane Jhonson, 1234)])]
    print()

    # 9th data example
    a.add(Plane(3,"Tarom", 3, "Budapest", [Passenger("Addam", "Sandler", 4321)]))
    # [(2, Wizzair, 3, London, [(Blake Lively, 4567), (Salma Hayek, 5678)]), (1, Ryanair, 3, Dubai, [(Gal Gadot, 1235), (Kevin Hart, 2345), (Dwane Jhonson, 1234)]), (3, Tarom, 3, Budapest, [(Addam Sandler, 4321)])]
    print(a.getAllPlanes())
    print()

    # 10th data example
    print(a.identifyPlaneByPassengerName("Addam Sandler"))
    # [(3, Tarom, 3, Budapest, [(Addam Sandler, 4321)])]
    print()

dataExamples()