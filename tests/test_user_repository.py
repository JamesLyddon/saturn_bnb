from lib.user_repository import UserRepository
from lib.user import User 

def test_get_all_users(db_connection):
    db_connection.seed("seeds/bnb_seed.sql")
    repository = UserRepository(db_connection)
    users = repository.all()
    assert users == [
        User(1, 'johndoe', 'John', 'Doe', '$2b$12$cPXIOM/8O1d/dTrBKWkIZutAmDsucwW7YgjfK9z6WVWBfZKr5YEkq', 'john.doe@example.com', '01234567890'),
        User(2, 'janesmith', 'Jane', 'Smith', '$2b$12$cPXIOM/8O1d/dTrBKWkIZutAmDsucwW7YgjfK9z6WVWBfZKr5YEkq', 'jane.smith@example.com',  '12345678901'),
        User(3, 'petermiller', 'Peter', 'Miller', '$2b$12$cPXIOM/8O1d/dTrBKWkIZutAmDsucwW7YgjfK9z6WVWBfZKr5YEkq', 'peter.miller@example.com', '23456789012'),
        User(4, 'alicejones', 'Alice', 'Jones', '$2b$12$cPXIOM/8O1d/dTrBKWkIZutAmDsucwW7YgjfK9z6WVWBfZKr5YEkq', 'alice.jones@example.com', '34567890123'),
        User(5,'emilywhite', 'Emily', 'White', '$2b$12$cPXIOM/8O1d/dTrBKWkIZutAmDsucwW7YgjfK9z6WVWBfZKr5YEkq', 'emily.white@example.com', '45678901234' ),
    ]
    

def test_get_single_user(db_connection):
    db_connection.seed("seeds/bnb_seed.sql")
    repository = UserRepository(db_connection)
    user = repository.find(2)
    assert user == User(2, 'janesmith', 'Jane', 'Smith', '$2b$12$cPXIOM/8O1d/dTrBKWkIZutAmDsucwW7YgjfK9z6WVWBfZKr5YEkq', 'jane.smith@example.com',  '12345678901')
    

def test_create_user(db_connection):
    db_connection.seed("seeds/bnb_seed.sql")
    repository = UserRepository(db_connection)
    repository.create(User(None, "lizatara", "Liza", "Tarasova", "tarasova123", "liza.tara@email.com", "31612997323"))
    
    new_user = repository.find(6)
    
    result = repository.all()
    
    assert result == [
        User(1, 'johndoe', 'John', 'Doe', '$2b$12$cPXIOM/8O1d/dTrBKWkIZutAmDsucwW7YgjfK9z6WVWBfZKr5YEkq', 'john.doe@example.com', '01234567890'),
        User(2, 'janesmith', 'Jane', 'Smith', '$2b$12$cPXIOM/8O1d/dTrBKWkIZutAmDsucwW7YgjfK9z6WVWBfZKr5YEkq', 'jane.smith@example.com',  '12345678901'),
        User(3, 'petermiller', 'Peter', 'Miller', '$2b$12$cPXIOM/8O1d/dTrBKWkIZutAmDsucwW7YgjfK9z6WVWBfZKr5YEkq', 'peter.miller@example.com', '23456789012'),
        User(4, 'alicejones', 'Alice', 'Jones', '$2b$12$cPXIOM/8O1d/dTrBKWkIZutAmDsucwW7YgjfK9z6WVWBfZKr5YEkq', 'alice.jones@example.com', '34567890123'),
        User(5,'emilywhite', 'Emily', 'White', '$2b$12$cPXIOM/8O1d/dTrBKWkIZutAmDsucwW7YgjfK9z6WVWBfZKr5YEkq', 'emily.white@example.com', '45678901234' ),
        User(6, 'lizatara', 'Liza', 'Tarasova', new_user.password, 'liza.tara@email.com', '31612997323'),
    ]
    

def test_delete_user(db_connection):
    db_connection.seed("seeds/bnb_seed.sql")
    repository = UserRepository(db_connection)
    repository.delete(3)
    result = repository.all()
    assert result == [
        User(1, 'johndoe', 'John', 'Doe', '$2b$12$cPXIOM/8O1d/dTrBKWkIZutAmDsucwW7YgjfK9z6WVWBfZKr5YEkq', 'john.doe@example.com', '01234567890'),
        User(2, 'janesmith', 'Jane', 'Smith', '$2b$12$cPXIOM/8O1d/dTrBKWkIZutAmDsucwW7YgjfK9z6WVWBfZKr5YEkq', 'jane.smith@example.com',  '12345678901'),
        User(4, 'alicejones', 'Alice', 'Jones', '$2b$12$cPXIOM/8O1d/dTrBKWkIZutAmDsucwW7YgjfK9z6WVWBfZKr5YEkq', 'alice.jones@example.com', '34567890123'),
        User(5,'emilywhite', 'Emily', 'White', '$2b$12$cPXIOM/8O1d/dTrBKWkIZutAmDsucwW7YgjfK9z6WVWBfZKr5YEkq', 'emily.white@example.com', '45678901234' ),
    ]
    