-- MySQL
SELECT CITY, LENGTH(CITY) FROM STATION GROUP BY CITY ORDER BY LENGTH(CITY), CITY ASC LIMIT 1;
SELECT CITY, LENGTH(CITY) FROM STATION GROUP BY CITY ORDER BY LENGTH(CITY) DESC LIMIT 1;
