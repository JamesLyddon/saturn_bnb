class Request:
    def __init__(self, booking_id, space_id, host_id, guest_id, date, status, price, title, description, address, host_email, guest_email, image_url):
        self.booking_id = booking_id
        self.space_id = space_id
        self.host_id = host_id
        self.guest_id = guest_id
        self.date = date
        self.status = status
        self.price = price
        self.title = title
        self.description = description
        self.address = address
        self.host_email = host_email
        self.guest_email = guest_email
        self.image_url = image_url