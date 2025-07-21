from lib.space import Space

def test_space_initialises_with_required_data():
    space = Space(1, 'title1', 'description1', 100.5, 'address1', 2)

    assert space.id == 1
    assert space.title == 'title1'
    assert space.description == 'description1'
    assert space.price == 100.5
    assert space.address == 'address1'
    assert space.host_id == 2


def test_spaces_are_equal():
    space1 = Space(1, 'title1', 'description1', 100.5, 'address1', 2)
    space2 = Space(1, 'title1', 'description1', 100.5, 'address1', 2)

    assert space1 == space2

def test_space_formats_nicely():
    space = Space(1, 'title1', 'description1', 100.5, 'address1', 2)

    assert str(space) == "Space(1, title1, description1, 100.5, address1, 2)"