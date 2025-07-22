from lib.space import Space

from lib.space_repository import SpaceRepository


def test_get_all_spaces(db_connection):
    db_connection.seed('seeds/bnb_seed.sql')
    space_repo = SpaceRepository(db_connection)
    all_spaces = space_repo.all()
    # Space(1, 'title1', 'description1', 100.5, 'address1', 2)
    assert all_spaces == [
        Space(1, 'Cozy Apartment in Central London', 'A charming one-bedroom apartment right in the heart of London, perfect for a couple or solo traveler.', 120.00, '10 Downing St, London, England, United Kingdom', 1),
        Space(2, 'Spacious Family Home in Countryside', 'Beautiful detached house with a large garden, ideal for family holidays. Close to scenic walking trails.', 250.00, 'Rural Lane 5, Oxford, England, United Kingdom', 1),
        Space(3, 'Beachfront Villa with Ocean Views', 'Luxury villa directly on the coast, stunning views and private beach access. Perfect for a relaxing getaway.', 350.50, 'Ocean Drive 123, Brighton, England, United Kingdom', 2),
        Space(4, 'Charming Edinburgh Loft', 'Stylish loft apartment in the historic Old Town of Edinburgh. Ideal for exploring the city on foot.', 150.00, 'Royal Mile 42, Edinburgh, Scotland, United Kingdom', 3),
        Space(5, 'Rustic Cottage in Scottish Highlands', 'Escape to the tranquil beauty of the Highlands in this quaint stone cottage. Perfect for nature lovers.', 90.00,'Loch Ness Road, Inverness, Scotland, United Kingdom', 4)
    ]


def test_find_space_by_id(db_connection):
    db_connection.seed('seeds/bnb_seed.sql')
    space_repo = SpaceRepository(db_connection)
    single_space = space_repo.find(1)

    assert single_space == Space(1, 'Cozy Apartment in Central London', 'A charming one-bedroom apartment right in the heart of London, perfect for a couple or solo traveler.', 120.00, '10 Downing St, London, England, United Kingdom', 1)