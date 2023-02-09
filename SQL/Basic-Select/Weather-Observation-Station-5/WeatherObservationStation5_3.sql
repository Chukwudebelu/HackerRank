-- MySQL
SELECT * FROM (SELECT CITY, LENGTH(CITY) 
               FROM STATION 
               WHERE LENGTH(CITY) = (SELECT MIN(LENGTH(CITY)) FROM STATION) 
               ORDER BY CITY) AS A 
               LIMIT 1;
SELECT * FROM (SELECT CITY, LENGTH(CITY) 
               FROM STATION 
               WHERE LENGTH(CITY) = (SELECT MAX(LENGTH(CITY)) FROM STATION) 
               ORDER BY CITY DESC) AS B 
               LIMIT 1;
