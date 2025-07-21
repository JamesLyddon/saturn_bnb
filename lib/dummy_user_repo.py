from lib.dummy_user import Dummy

class DummyRepo:
    def __init__(self, connection):
        self._connection = connection

    # Retrieve all users
    def all(self):
        rows = self._connection.execute(
            """
            SELECT * from users
            """
            )
        users = []
        for row in rows:
            user = Dummy(
                id=row['id'],
                username=row['username'],
                first_name=row['first_name'],
                last_name=row['last_name'],
                password=row['password'],
                email=row['email'],
                phone_number=row['phone_number']
            )
            users.append(user)
        return users

    def find(self, user_id):
        rows = self._connection.execute(
            """
            SELECT * from users WHERE id = %s
            """
            , [user_id])
        row = rows[0]
        return Dummy(
                id=row['id'],
                username=row['username'],
                first_name=row['first_name'],
                last_name=row['last_name'],
                password=row['password'],
                email=row['email'],
                phone_number=row['phone_number']
            )

    # Create a new user
    def create(self, user):
        rows = self._connection.execute(
            """
            INSERT INTO users (username, first_name, last_name, password, email, phone_number) 
            VALUES (%s, %s, %s, %s, %s, %s) RETURNING id
            """
            , [user.username, user.first_name, user.last_name, user.password, user.email, user.phone_number])
        new_id = rows[0]['id']
        return self.find(new_id)