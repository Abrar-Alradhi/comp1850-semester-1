.headers on
.mode column
--Bronze:
SELECT * FROM drivers;
SELECT name, price FROM menu_items WHERE restaurant_id= 3;
SELECT name FROM restaurants WHERE cuisine = 'Indian';
SELECT COUNT(*) FROM customers; --180

--Silver:
SELECT restaurant_id, name, price FROM menu_items WHERE price < 8 AND is_vegetarian = 1 ORDER BY price ASC;
--SELECT t1.name, t2.rating FROM restaurants AS t1 JOIN reviews AS t2 ON t1.restaurant_id=t2 WHERE rating < 4 ORDER BY rating ASC; 
SELECT name, hygiene_rating FROM restaurants WHERE hygiene_rating < 4 ORDER BY hygiene_rating ASC; 
SELECT name, hygiene_rating FROM restaurants WHERE postcode LIKE 'LS6%' ORDER BY hygiene_rating DESC; 
SELECT name, email, joined_date FROM customers WHERE email LIKE '%@leeds.ac.uk' ORDER BY joined_date DESC;
SELECT * FROM orders WHERE status = 'cancelled' LIMIT 10; --10 most recent cancelled orders.
SELECT name FROM menu_items WHERE restaurant_id = 4 AND is_vegetarian = 1;
SELECT name FROM menu_items WHERE restaurant_id = 4 ORDER BY price DESC LIMIT 1;
--GOLD
SELECT customer_id, restaurant_id, order_time, status FROM orders WHERE status = 'placed' AND order_time LIKE %10;

-- Write your sql for each task here - you can use comment (start with --) to add notes or number them. Remember your ; at the end of each query!
-- with multiple queries in the file, sql will run then one after the other and print them all out, so I recommend testing after each one.

