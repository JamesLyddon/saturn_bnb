
class Booking:
    
    def __init__ (self, id, guest_id, space_id, date, status):
        self.id = id
        self.guest_id = guest_id
        self.space_id = space_id
        self.date = date
        self.status = status
        
    def __repr__ (self):
        return f"Booking({self.id},{self.guest_id},{self.space_id}, {self.date}, {self.status})"
    
    def __eq__ (self, other):
        return self.__dict__ == other.__dict__