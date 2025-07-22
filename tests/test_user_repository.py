from lib.user_repository import UserRepository
from lib.user import User 

def test_get_all_users(db_connection):
    db_connection.seed("seeds/bnb_seed.sql")
    repository = UserRepository(db_connection)
    users = repository.all()
    assert users == [
        User(1, 'johndoe', 'John', 'Doe', 'hashedpassword123', 'john.doe@example.com', '01234567890'),
        User(2, 'janesmith', 'Jane', 'Smith', 'anotherhash456', 'jane.smith@example.com',  '12345678901'),
        User(3, 'petermiller', 'Peter', 'Miller', 'millerspass789', 'peter.miller@example.com', '23456789012'),
        User(4, 'alicejones', 'Alice', 'Jones', 'joneshash101', 'alice.jones@example.com', '34567890123'),
        User(5,'emilywhite', 'Emily', 'White', 'whitepass202', 'emily.white@example.com', '45678901234' ),
    ]
    

def test_get_single_user(db_connection):
    db_connection.seed("seeds/bnb_seed.sql")
    repository = UserRepository(db_connection)
    user = repository.find(2)
    assert user == User(2, 'janesmith', 'Jane', 'Smith', 'anotherhash456', 'jane.smith@example.com',  '12345678901')
    

def test_create_user(db_connection):
    db_connection.seed("seeds/bnb_seed.sql")
    repository = UserRepository(db_connection)
    repository.create(User(None, "lizatara", "Liza", "Tarasova", "tarasova123", "liza.tara@email.com", "31612997323"))
    
    result = repository.all()
    
    assert result == [
        User(1, 'johndoe', 'John', 'Doe', 'hashedpassword123', 'john.doe@example.com', '01234567890'),
        User(2, 'janesmith', 'Jane', 'Smith', 'anotherhash456', 'jane.smith@example.com',  '12345678901'),
        User(3, 'petermiller', 'Peter', 'Miller', 'millerspass789', 'peter.miller@example.com', '23456789012'),
        User(4, 'alicejones', 'Alice', 'Jones', 'joneshash101', 'alice.jones@example.com', '34567890123'),
        User(5,'emilywhite', 'Emily', 'White', 'whitepass202', 'emily.white@example.com', '45678901234' ),
        User(6, 'lizatara', 'Liza', 'Tarasova', 'tarasova123', 'liza.tara@email.com', '31612997323'),
    ]
    

def test_delete_user(db_connection):
    db_connection.seed("seeds/bnb_seed.sql")
    repository = UserRepository(db_connection)
    repository.delete(3)
    result = repository.all()
    assert result == [
        User(1, 'johndoe', 'John', 'Doe', 'hashedpassword123', 'john.doe@example.com', '01234567890'),
        User(2, 'janesmith', 'Jane', 'Smith', 'anotherhash456', 'jane.smith@example.com',  '12345678901'),
        User(4, 'alicejones', 'Alice', 'Jones', 'joneshash101', 'alice.jones@example.com', '34567890123'),
        User(5,'emilywhite', 'Emily', 'White', 'whitepass202', 'emily.white@example.com', '45678901234' ),
    ]
    