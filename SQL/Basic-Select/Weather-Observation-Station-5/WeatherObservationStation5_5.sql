-- MySQL
SELECT s.* FROM ((SELECT CITY, LENGTH(CITY)
                  FROM STATION
                  ORDER BY LENGTH(CITY), CITY ASC
                  LIMIT 1) UNION ALL (SELECT CITY, LENGTH(CITY)
                                      FROM STATION
                                      ORDER BY LENGTH(CITY) DESC
                                      LIMIT 1)) AS s;
