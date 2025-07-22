
class User:
    
    def __init__(self, id, username, first_name, last_name, password, email, phone_number):
        self.id = id
        self.username = username 
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.email = email
        self.phone_number = phone_number
        
    def __eq__(self, other):
        return self.__dict__ == other.__dict__