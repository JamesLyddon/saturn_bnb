from lib.space import Space


class SpaceRepository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * FROM spaces')

        spaces = [Space(row['id'], row['host_id'], row['title'], row['description'], row['price'], row['address']) 
                for row in rows]
        
        return spaces
    
    def find(self, id):
        rows = self._connection.execute('SELECT * FROM spaces WHERE id = %s', [id])

        row = rows[0]

        return Space(row['id'], row['host_id'], row['title'], row['description'], row['price'], row['address'])
    
    def create(self, space):
        self._connection.execute("INSERT INTO spaces (host_id, title, description, price, address) VALUES (%s, %s, %s, %s, %s)", [space.host_id, space.title, space.description, space.price, space.address])

        return None