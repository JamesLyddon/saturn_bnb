from lib.space import Space


class SpaceRepository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * FROM spaces')

        spaces = [Space(row['id'], row['title'], row['description'], row['price'], row['address'], row['host_id']) 
                for row in rows]
        
        return spaces
    
    def find(self, id):
        rows = self._connection.execute('SELECT * FROM spaces WHERE id = %s', [id])
        