

class Space:
    def __init__(self, id, host_id, title, description, price, address, image_url='https://bulma.io/assets/images/placeholders/1280x960.png'):
        self.id = id
        self.title = title
        self.description = description
        self.price = price
        self.address = address
        self.host_id = host_id
        self.image_url = image_url

    def __eq__(self, value):
        return self.__dict__ == value.__dict__

    def __repr__(self):
        
        return f"Space({self.id}, {self.host_id}, {self.title}, {self.description}, {self.price}, {self.address})"