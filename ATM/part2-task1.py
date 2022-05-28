# Design object model for given domain.
# Please demonstrate usage of: Classes, Inheritance, Polymorphism, Encapsulation
# Each class, method and variable should have meaningful name and purpose.
# You need to determine which classes are required. Inheritance should be used only when it makes sense.
# Classes should be grouped into corresponding packages. Work with console should be minimized
# (only required data for input, output correspond the info in task).
# It is expected that you will define classes hierarchy and implement it using OOP
# (inheritance or implementing interfaces). Each class should have methods and fields defined by you.
# Your program should create objects of different types

# 5. Airline. Define airplanes hierarchy. Create airline. Calculate total capacity and load capacity.
# (What is the difference between total and load?)
# Sort company's airplanes by predefined criteria (define criteria by yourself).
# Find airplane which will match predefined criteria (you could define one or several criteria).

class Airline:
    def __init__(self, name, base_country=None, aircrafts=[]):
        self.name = name
        self.base_country = base_country
        self.aircrafts = aircrafts

    def add_aircraft(self, aircraft):
        self.aircrafts.append(aircraft)

    def sort_by_cap(self):
        return sorted(self.aircrafts, key=Aircraft.capacity_getter)

    def sort_by_dist(self):
        return sorted(self.aircrafts, key=Aircraft.distance_getter)


class Flight:
    def __init__(self, dep_airport, dest_airport, dep_datetime, arr_datetime, flight_num, distance=None, aircraft=None):
        self.dep_airport = dep_airport
        self.dest_airport = dest_airport
        self.dep_datetime = dep_datetime
        self.arr_datetime = arr_datetime
        self.flight_num = flight_num
        self.distance = distance
        self.aircraft = aircraft

    def get_duration(self):
        return self.arr_datetime - self.dep_datetime


class Ticket:
    def __init__(self, flight_num):
        self.flight_num = flight_num


class Airport:
    def __init__(self, country, city):
        self.country = country
        self.city = city


class Aircraft:
    def __init__(self, max_distance=None, max_capacity=1):
        self.max_distance = max_distance
        self.max_capacity = max_capacity

    def __repr__(self):
        return f'Aircraft({self.max_distance}, {self.max_capacity})'

    def capacity_getter(self):
        return self.max_capacity

    def distance_getter(self):
        return self.max_distance


class Helicopter(Aircraft):
    pass


class Airplane(Aircraft):
    pass


modern_airline = Airline('Modern Airline')

aircraft1 = Aircraft(1000, 100)
aircraft2 = Aircraft(3000, 150)
aircraft3 = Aircraft(5000, 50)
aircraft_list = [aircraft1, aircraft2, aircraft3]

for x in aircraft_list:
    modern_airline.add_aircraft(x)

print(modern_airline.sort_by_cap())
print(modern_airline.sort_by_dist())
