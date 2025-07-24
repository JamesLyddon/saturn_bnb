from lib.request import Request

class RequestRepository:
    def __init__(self, connection):
        self._connection = connection
    
    def all(self):
        rows = self._connection.execute(
            '''
            SELECT
                b.id AS booking_id,
                b.space_id,
                s.host_id,
                b.guest_id,
                b.date,
                b.status,
                s.price,
                s.title,
                s.description,
                s.address,
                s.image_url,
                host_user.email AS host_email,
                guest_user.email AS guest_email
            FROM
                bookings AS b
            JOIN
                spaces AS s ON b.space_id = s.id
            JOIN
                users AS guest_user ON b.guest_id = guest_user.id
            JOIN
                users AS host_user ON s.host_id = host_user.id;
            '''
        )
        requests = []
        for row in rows:
            item = Request(
                booking_id=row["booking_id"],
                space_id=row["space_id"],
                host_id=row["host_id"],
                guest_id=row["guest_id"],
                date=row["date"],
                status=row["status"],
                price=row["price"],
                title=row["title"],
                description=row["description"],
                address=row["address"],
                host_email=row["host_email"],
                guest_email=row["guest_email"],
                image_url=row["image_url"]
            )
            requests.append(item)
        return requests

    def find_by_booking_id(self, booking_id):
        all_requests = self.all()
        for request in all_requests:
            if request.booking_id == booking_id:
                return request
        return None
        
        
        
        # rows = self._connection.execute('SELECT * FROM requests WHERE booking_id = %s', [booking_id])
        # row = rows[0]
        # return Request(
        #         booking_id=row["booking_id"],
        #         space_id=row["space_id"],
        #         host_id=row["host_id"],
        #         guest_id=row["guest_id"],
        #         date=row["date"],
        #         status=row["status"],
        #         price=row["price"],
        #         title=row["title"],
        #         description=row["description"],
        #         address=row["address"],
        #         host_email=row["host_email"],
        #         guest_email=row["guest_email"],
        #         image_url=row["image_url"]
        #     )