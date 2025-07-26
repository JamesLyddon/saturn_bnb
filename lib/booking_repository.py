from lib.booking import Booking
class BookingRepository:
    
    def __init__(self, connection):
        self._connection = connection

    
    def all(self):
        rows = self._connection.execute('SELECT * FROM bookings')
        bookings = []
        for row in rows:
            item = Booking(row["id"], row["guest_id"], row["space_id"], row["date"], row["status"])
            bookings.append(item)
        return bookings
    
    def find(self,booking_id):
        rows = self._connection.execute('SELECT * FROM bookings WHERE id = %s', [booking_id])
        row = rows[0]
        return Booking(row["id"], row["guest_id"], row["space_id"], row["date"], row["status"])
    
    def create(self, booking):
        rows = self._connection.execute('INSERT INTO bookings (guest_id, space_id, date, status) VALUES (%s, %s, %s, %s) RETURNING id',
            [booking.guest_id, booking.space_id, booking.date, booking.status])
        new_id = rows[0]['id']
        return new_id
    
    def is_available(self, date, space_id):
        rows = self._connection.execute("SELECT * FROM bookings WHERE date = %s AND status = 'confirmed' AND space_id = %s", [date, space_id])

        if len(rows) == 0:
            return True

        return False

    def update_status(self, booking_id, new_status):
        self._connection.execute(
            'UPDATE bookings SET status = %s WHERE id = %s',
            [new_status, booking_id]
        )
        return None

    def reject_similar_pending(self, confirmed_space_id, confirmed_date, confirmed_booking_id):
        """
        Rejects all other pending bookings for a given space_id and date,
        excluding the booking that was just confirmed.
        Returns a list of booking IDs that were rejected.
        """
        # First, select the IDs of the bookings that will be rejected
        rejected_booking_ids_rows = self._connection.execute(
            """
            SELECT id FROM bookings
            WHERE
                space_id = %s AND
                date = %s AND
                status = 'pending' AND
                id != %s;
            """,
            [confirmed_space_id, confirmed_date, confirmed_booking_id]
        )

        # Then, perform the update
        self._connection.execute(
            """
            UPDATE bookings
            SET status = 'rejected'
            WHERE
                space_id = %s AND
                date = %s AND
                status = 'pending' AND
                id != %s;
            """,
            [confirmed_space_id, confirmed_date, confirmed_booking_id]
        )

        # Extract the IDs into a list
        rejected_booking_ids = [row['id'] for row in rejected_booking_ids_rows]
        return rejected_booking_ids
