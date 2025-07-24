-- test sql queries

INSERT INTO bookings (guest_id, space_id, date, status) VALUES (1, 1, '2025-08-01', 'pending');

SELECT * FROM bookings 
WHERE date = '2025-08-10' AND status = 'confirmed' AND space_id = 2;