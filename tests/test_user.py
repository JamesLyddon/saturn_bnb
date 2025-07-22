from lib.user import User 


def test_user_constructs():
    user = User(1, "saima19", "Saima", "Abdus", "saima1234", "saima.abd@email.com", "31412810493")
    assert user.id == 1
    assert user.username == "saima19"
    assert user.first_name == "Saima"
    assert user.last_name == "Abdus"
    assert user.password == "saima1234"
    assert user.email == "saima.abd@email.com"
    assert user.phone_number == "31412810493"
    

def test_user_format_nicely():
    user = User(1, "saima19", "Saima", "Abdus", "saima1234", "saima.abd@email.com", "31412810493")
    assert str(user) == "User(1, saima19, Saima, Abdus, saima1234, saima.abd@email.com, 31412810493)"