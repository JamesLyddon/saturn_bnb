from lib.booking import Booking

"""
Booking constructs with an id, guest_id, space_id, date, status
"""
def test_booking_constructs():
    booking = Booking(1,7,3,"18/12/25","pending")
    assert booking.id == 1
    assert booking.guest_id == 7 
    assert booking.space_id == 3
    assert booking.date == "18/12/25"
    assert booking.status == "pending"


"""
We can format booking to strings nicely
"""
def test_booking_formats_nicely():
    booking = Booking(1,7,3,"18/12/25","pending")
    assert str(booking) == 'Booking(1,7,3, 18/12/25, pending)'

"""
We can compare two identical bookings
And have them be equal
"""

def test_booking_is_equal():
    booking_1 = Booking(1,7,3,"18/12/25","pending")
    booking_2 = Booking(1,7,3,"18/12/25","pending")
    assert booking_1 == booking_2