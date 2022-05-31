# pytest, Mock, fixture (creates class instance), tests parametrization

import pytest
from part2_task1 import *

aircraft_mig = Aircraft()
aircraft_su = Aircraft(1000, 50)
aircraft_jet = Aircraft(3000, 15)
aircraft_aa = Aircraft(5000, 150)


@pytest.fixture
def airline_instance():
    air_company = Airline('Air Company')
    return air_company


@pytest.fixture
def airline_instance_airports():
    air_company = Airline('Air Company')
    air_company.add_aircraft(aircraft_jet)
    air_company.add_aircraft(aircraft_aa)
    air_company.add_aircraft(aircraft_su)
    return air_company


def test_airline(airline_instance):
    assert airline_instance.name == 'Air Company'
    assert airline_instance.aircrafts == []
    assert airline_instance.base_country is None


@pytest.mark.parametrize('test_object, expected_res', [(Ticket(6235).flight_num, 6235),
                                                       (Ticket('6532D').flight_num, '6532D')])
def test_ticket(test_object, expected_res):
    assert test_object == expected_res


def test_ticket_from_file():
    ticket_ff = Ticket.from_file('../ticket.txt')
    assert ticket_ff[0].flight_num == '1300AB'


def test_ticket_from_json():
    ticket_js = Ticket.from_json('../ticket.json')
    assert ticket_js[0].flight_num == 5546


def test_aircraft():
    assert aircraft_mig.max_distance is None
    assert aircraft_mig.max_capacity == 1
    assert aircraft_su.max_distance == 1000
    assert aircraft_su.max_capacity == 50


def test_aircraft_capacity_getter(mocker):
    mocker.patch('part2_task1.Aircraft.capacity_getter', return_value=30)
    assert aircraft_su.capacity_getter() == 30


def test_aircraft_distance_getter():
    with pytest.raises(DistanceError):
        aircraft_mig.distance_getter()


def test_helicopter():
    helicopter = Helicopter()
    assert isinstance(helicopter, Helicopter)
    assert isinstance(helicopter, Aircraft)


def test_add_aircraft(airline_instance):
    airline_instance.add_aircraft(aircraft_su)
    assert airline_instance.aircrafts[0] == aircraft_su


def test_add_aircraft_wrong_type(airline_instance):
    with pytest.raises(AircraftError):
        airline_instance.add_aircraft('string')


def test_airline_sort_by_cap(airline_instance_airports):
    assert airline_instance_airports.sort_by_cap()[0] == aircraft_jet


def test_airline_sort_by_dist(airline_instance_airports):
    assert airline_instance_airports.sort_by_dist()[0] == aircraft_su


def test_airline_get_aircraft_maxcap(airline_instance_airports):
    assert airline_instance_airports.get_aircraft_maxcap() == aircraft_aa


def test_airline_get_aircraft_maxdist(airline_instance_airports):
    assert airline_instance_airports.get_aircraft_maxdist() == aircraft_aa
