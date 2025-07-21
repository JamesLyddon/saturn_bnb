

class Space:
    def __init__(self, id, title, description, price, address, host_id):
        self.id = id
        self.title = title
        self.description = description
        self.price = price
        self.address = address
        self.host_id = host_id
    

    def __eq__(self, value):
        return self.__dict__ == value.__dict__

    def __repr__(self):
        
        return f"Space({self.id}, {self.title}, {self.description}, {self.price}, {self.address}, {self.host_id})"