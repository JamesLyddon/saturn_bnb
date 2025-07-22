from lib.user import User 

class UserRepository:
    def __init__(self, connection):
        self._connection = connection
        
    def all(self):
        rows = self._connection.execute('SELECT * FROM users')
        users = []
        for row in rows:
            item = User(row["id"], row["username"], row["first_name"], row["last_name"], row["password"], row["email"], row["phone_number"])
            users.append(item)
        return users 
    
    def find(self, id):
        rows = self._connection.execute('SELECT * FROM users WHERE id = %s', [id]) 
        
        # return None if no user found
        if not rows:
            return None
        
        row = rows[0]
        return User(row["id"], row["username"], row["first_name"], row["last_name"], row["password"], row["email"], row["phone_number"])
    
    def create(self, user):
        self._connection.execute('INSERT INTO users (username, first_name, last_name, password, email, phone_number) VALUES (%s, %s, %s, %s, %s, %s)', 
                                [user.username, user.first_name, user.last_name, user.password, user.email, user.phone_number])
        return None 
    
    def delete(self, id):
        self._connection.execute('DELETE FROM users WHERE id = %s', [id])
        return None 