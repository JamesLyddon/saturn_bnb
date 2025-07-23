from flask_login import UserMixin

class Dummy(UserMixin):
    def __init__(self, id, username, first_name, last_name, password, email, phone_number):
        self.id = id
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.email = email
        self.phone_number = phone_number

    def __str__(self):
        return f"User({self.id}, {self.username}, {self.first_name}, {self.last_name}, {self.password}, {self.email}, {self.phone_number})"