from lib.booking_repository import BookingRepository
from lib.booking import Booking
from datetime import date

def test_get_all_bookings(db_connection):
    db_connection.seed("seeds/bnb_seed.sql")
    repository = BookingRepository(db_connection)
    bookings = repository.all()

    assert bookings == [
        Booking(1, 4, 1, date(2025, 8, 10), 'confirmed'),
        Booking(2, 5, 3, date(2025, 9, 1), 'pending'),
        Booking(3, 1, 4, date(2025, 8, 20), 'rejected'),
        Booking(4, 2, 5, date(2026, 1, 5), 'confirmed')
    ]

def test_get_single_booking(db_connection):
    db_connection.seed("seeds/bnb_seed.sql")
    repository = BookingRepository(db_connection)

    booking = repository.find(1)
    assert booking == Booking(1, 4, 1, date(2025, 8, 10), 'confirmed')

def test_create_booking(db_connection):
    db_connection.seed("seeds/bnb_seed.sql")
    repository = BookingRepository(db_connection)
    repository.create(Booking(None, 5, 3, date(2026, 3, 16), 'pending'))

    assert repository.all() == [
        Booking(1, 4, 1, date(2025, 8, 10), 'confirmed'),
        Booking(2, 5, 3, date(2025, 9, 1), 'pending'),
        Booking(3, 1, 4, date(2025, 8, 20), 'rejected'),
        Booking(4, 2, 5, date(2026, 1, 5), 'confirmed'),
        Booking(5, 5, 3, date(2026, 3, 16), 'pending')
    ]


def test_is_available_date(db_connection):
    db_connection.seed("seeds/bnb_seed.sql")
    repository = BookingRepository(db_connection)
    is_available = repository.is_available('2025-08-10', 1)
    assert is_available == False

def test_is_not_available_date(db_connection):
    db_connection.seed("seeds/bnb_seed.sql")
    repository = BookingRepository(db_connection)
    is_available = repository.is_available('2025-09-01', 3)
    assert is_available == True