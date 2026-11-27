.headers on
.mode column

-- add tasks below
-- sqlite3 database_file.db to open the database
-- .read sql_file.sql to run the queries
SELECT COUNT(*) AS cardinality FROM stations; 
SELECT COUNT(*) AS degree FROM pragma_table_info('stations');

--q5:
SELECT year_added FROM bikes WHERE bike_id= 12;
-- Q6:
SELECT COUNT(*) FROM stations WHERE capacity = 16;
--Q7:
SELECT COUNT(*) FROM stations WHERE capacity < 12;
--Q8:
SELECT bike_id FROM bikes 
WHERE year_added LIKE '%22' ;
--Q9:
SELECT * FROM stations WHERE name = 'Holbeck Road';
UPDATE stations SET name = 'Holbeck Village' WHERE name = 'holbeck road';
--Q10: