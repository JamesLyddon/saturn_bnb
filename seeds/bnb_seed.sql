DROP TABLE IF EXISTS bookings;
DROP TABLE IF EXISTS spaces;
DROP TABLE IF EXISTS users;

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(255) UNIQUE NOT NULL,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    phone_number VARCHAR(255) UNIQUE NOT NULL
);

CREATE TABLE spaces (
    id SERIAL PRIMARY KEY,
    host_id INT NOT NULL,
    title VARCHAR(255) NOT NULL,
    description TEXT,
    price NUMERIC(10, 2) NOT NULL,
    address VARCHAR(255) NOT NULL,
    FOREIGN KEY (host_id) REFERENCES users(id) ON DELETE CASCADE 
);

CREATE TABLE bookings (
    id SERIAL PRIMARY KEY,
    guest_id INT NOT NULL,
    space_id INT NOT NULL,
    date DATE NOT NULL,
    status VARCHAR(50) NOT NULL DEFAULT 'pending',
    FOREIGN KEY (space_id) REFERENCES spaces(id) ON DELETE CASCADE,
    FOREIGN KEY (guest_id) REFERENCES users(id) ON DELETE CASCADE
);


-- create users (hashed passwords are all 'SuperSecret999')
INSERT INTO users (username, first_name, last_name, password, email, phone_number) VALUES
('johndoe', 'John', 'Doe', '$2b$12$cPXIOM/8O1d/dTrBKWkIZutAmDsucwW7YgjfK9z6WVWBfZKr5YEkq', 'john.doe@example.com', '01234567890'),
('janesmith', 'Jane', 'Smith', '$2b$12$cPXIOM/8O1d/dTrBKWkIZutAmDsucwW7YgjfK9z6WVWBfZKr5YEkq', 'jane.smith@example.com',  '12345678901'),
('petermiller', 'Peter', 'Miller', '$2b$12$cPXIOM/8O1d/dTrBKWkIZutAmDsucwW7YgjfK9z6WVWBfZKr5YEkq', 'peter.miller@example.com', '23456789012'),
('alicejones', 'Alice', 'Jones', '$2b$12$cPXIOM/8O1d/dTrBKWkIZutAmDsucwW7YgjfK9z6WVWBfZKr5YEkq', 'alice.jones@example.com', '34567890123'),
('emilywhite', 'Emily', 'White', '$2b$12$cPXIOM/8O1d/dTrBKWkIZutAmDsucwW7YgjfK9z6WVWBfZKr5YEkq', 'emily.white@example.com', '45678901234' );


-- create spaces
-- johndoe
INSERT INTO spaces (host_id, title, description, price, address) VALUES
(1, 'Cozy Apartment in Central London', 'A charming one-bedroom apartment right in the heart of London, perfect for a couple or solo traveler.', 120.00, '10 Downing St, London, England, United Kingdom'),
(1, 'Spacious Family Home in Countryside', 'Beautiful detached house with a large garden, ideal for family holidays. Close to scenic walking trails.', 250.00, 'Rural Lane 5, Oxford, England, United Kingdom');

-- janesmith
INSERT INTO spaces (host_id, title, description, price, address) VALUES
(2, 'Beachfront Villa with Ocean Views', 'Luxury villa directly on the coast, stunning views and private beach access. Perfect for a relaxing getaway.', 350.50, 'Ocean Drive 123, Brighton, England, United Kingdom');

-- petermiller
INSERT INTO spaces (host_id, title, description, price, address) VALUES
(3, 'Charming Edinburgh Loft', 'Stylish loft apartment in the historic Old Town of Edinburgh. Ideal for exploring the city on foot.', 150.00, 'Royal Mile 42, Edinburgh, Scotland, United Kingdom');

-- alicejones
INSERT INTO spaces (host_id, title, description, price, address) VALUES
(4, 'Rustic Cottage in Scottish Highlands', 'Escape to the tranquil beauty of the Highlands in this quaint stone cottage. Perfect for nature lovers.', 90.00,'Loch Ness Road, Inverness, Scotland, United Kingdom');

-- create bookings
-- Alice Jones (user_id=4) books London Apartment (space_id=1)
INSERT INTO bookings (guest_id, space_id, date, status) VALUES
(4, 1, '2025-08-10', 'confirmed');

-- Emily White (user_id=5) books Beachfront Villa (space_id=3)
INSERT INTO bookings (guest_id, space_id, date, status) VALUES
(5, 3, '2025-09-01', 'pending');

-- John Doe (user_id=1) books Edinburgh Loft (space_id=4)
INSERT INTO bookings (guest_id, space_id, date, status) VALUES
(1, 4, '2025-08-20', 'rejected');

-- Jane Smith (user_id=2) books Rustic Cottage (space_id=5)
INSERT INTO bookings (guest_id, space_id, date, status) VALUES
(2, 5, '2026-01-05', 'confirmed');