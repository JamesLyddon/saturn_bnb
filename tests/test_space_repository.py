from lib.space import Space

from lib.space_repository import SpaceRepository


def test_get_all_spaces(db_connection):
    db_connection.seed('seeds/bnb_seed.sql')
    space_repo = SpaceRepository(db_connection)
    all_spaces = space_repo.all()
    
    assert all_spaces == [
        Space(1, 1, 'Cozy Apartment in Central London', 'A charming one-bedroom apartment right in the heart of London, perfect for a couple or solo traveler.', 120.00, '10 Downing St, London, England, United Kingdom', all_spaces[0].image_url),
        Space(2, 1, 'Spacious Family Home in Countryside', 'Beautiful detached house with a large garden, ideal for family holidays. Close to scenic walking trails.', 250.00, 'Rural Lane 5, Oxford, England, United Kingdom', all_spaces[1].image_url),
        Space(3, 2, 'Beachfront Villa with Ocean Views', 'Luxury villa directly on the coast, stunning views and private beach access. Perfect for a relaxing getaway.', 350.50, 'Ocean Drive 123, Brighton, England, United Kingdom', all_spaces[2].image_url),
        Space(4, 3, 'Charming Edinburgh Loft', 'Stylish loft apartment in the historic Old Town of Edinburgh. Ideal for exploring the city on foot.', 150.00, 'Royal Mile 42, Edinburgh, Scotland, United Kingdom', all_spaces[3].image_url),
        Space(5, 4, 'Rustic Cottage in Scottish Highlands', 'Escape to the tranquil beauty of the Highlands in this quaint stone cottage. Perfect for nature lovers.', 90.00,'Loch Ness Road, Inverness, Scotland, United Kingdom', all_spaces[4].image_url)
    ]


def test_find_space_by_id(db_connection):
    db_connection.seed('seeds/bnb_seed.sql')
    space_repo = SpaceRepository(db_connection)
    single_space = space_repo.find(1)

    assert single_space == Space(1, 1, 'Cozy Apartment in Central London', 'A charming one-bedroom apartment right in the heart of London, perfect for a couple or solo traveler.', 120.00, '10 Downing St, London, England, United Kingdom', single_space.image_url)

def test_create_space(db_connection):
    db_connection.seed('seeds/bnb_seed.sql')
    space_repo = SpaceRepository(db_connection)

    space_repo.create(Space(None, 3, 'Cozy Apartment in Leicester', 'A charming one-bedroom apartment right in the heart of Leicester', 100, 'one cabot place'))

    result = space_repo.all()

    assert result[-1] == Space(6, 3, 'Cozy Apartment in Leicester', 'A charming one-bedroom apartment right in the heart of Leicester', 100, 'one cabot place', result[-1].image_url)