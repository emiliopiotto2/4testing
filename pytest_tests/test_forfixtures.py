from forfixtures import *
import pytest

Hotel1=  Hotel(5,5)
Hotel2=  Hotel(4,4)
print(type(Hotel1),Hotel1.stars,Hotel1.location)

print(Hotel1.total_value())
print(Hotel1.hotel_classifier())
print(Hotel2.hotel_classifier())



@pytest.mark.parametrize("stars,location,expected", [
    (1, 2, 2),
    (2, 2, 4),
    (4, 5, 20),
    (5, 5, 25),
])

def test_parametrization(stars, location, expected):
    my_hotel = Hotel(stars,location)

    assert my_hotel.total_value() == expected

@pytest.fixture
def premium_hotel():
    '''Returns a premium Hotel instance'''
    hotel = Hotel(5,1)
    return hotel

# Hotel3 = Hotel(5,1)
# print(Hotel3.hotel_classifier())

def test_fixtures1(premium_hotel):
    assert premium_hotel.hotel_classifier() == ['Premium','Close range']
    

def test_fixtures2(premium_hotel):
    premium_hotel.location = 5
    assert premium_hotel.hotel_classifier() == ['Premium', 'Medium range']
 
def test_fixtures3(premium_hotel):
    premium_hotel.location = 8
    assert premium_hotel.hotel_classifier() == ['Premium', 'Long range']
   
    