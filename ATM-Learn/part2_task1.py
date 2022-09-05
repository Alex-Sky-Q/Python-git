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

# Part3.Task2. Enhance the scenarios with reading from file / writing data to file using I/O Streams
import json
import sys
from part3_task1 import *


class Airline:
    def __init__(self, name, base_country=None, aircrafts=None):
        if aircrafts is None:
            aircrafts = []
        self.name = name
        self.base_country = base_country
        self.aircrafts = aircrafts

    def add_aircraft(self, aircraft):
        if isinstance(aircraft, Aircraft):
            self.aircrafts.append(aircraft)
        else:
            raise AircraftError

    # Sort aircrafts by max capacity
    def sort_by_cap(self):
        return sorted(self.aircrafts, key=Aircraft.capacity_getter)

    # Sort aircrafts by max distance
    def sort_by_dist(self):
        try:
            return sorted(self.aircrafts, key=Aircraft.distance_getter)
        except DistanceError:
            print('Please set the distance for all aircrafts')
            sys.exit()

    def get_aircraft_maxcap(self):
        try:
            return self.sort_by_cap()[-1]
        except IndexError:
            print('There are no aircrafts in the Airline')

    def get_aircraft_maxdist(self):
        try:
            return self.sort_by_dist()[-1]
        except IndexError:
            print('There are no aircrafts in the Airline')
            sys.exit()


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
        if self.arr_datetime > self.dep_datetime:
            return self.arr_datetime - self.dep_datetime
        else:
            raise DurationError(self)


class Ticket:
    def __init__(self, flight_num):
        self.flight_num = flight_num

    def __repr__(self):
        return f'Ticket({self.flight_num})'

    @classmethod
    def from_file(cls, filename):
        with open(filename) as f:
            tickets_list = [cls(line.rstrip()) for line in f]
        return tickets_list

    @classmethod
    def from_json(cls, filename):
        with open(filename) as f:
            tickets_dict = json.load(f)
            tickets_list = [cls(val) for val in tickets_dict.values()]
        return tickets_list


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
        if self.max_distance is not None:
            return self.max_distance
        raise DistanceError(self)


class Helicopter(Aircraft):
    pass


class Airplane(Aircraft):
    pass


# modern_airline = Airline('Modern Airline')

# aircraft1 = Aircraft(1000, 100)
# aircraft2 = Aircraft(3000, 150)
# aircraft3 = Aircraft(5000, 50)
# aircraft_list = [aircraft1, aircraft2, aircraft3]
#
# for x in aircraft_list:
#     try:
#         modern_airline.add_aircraft(x)
#     except AircraftError:
#         print('Airline accepts only Aircraft objects')

# print(modern_airline.sort_by_cap())
# print(modern_airline.sort_by_dist())

# print(modern_airline.get_aircraft_maxcap())
# print(modern_airline.get_aircraft_maxdist())

# test_airline = Airline('test')
# print(test_airline.sort_by_dist())
