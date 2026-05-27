--------------------------------------------------------------------------
---To find the highest temperature recorded in the dataset, I will use the following SQL query:
SELECT MAX(temperature) AS highest_temperature
FROM `single-actor-432513-n6.weather_data.Temperature`;

--------------------------------------------------------------------------
---To calculate the average temperature for each city, I will use the following SQL query:
SELECT
    city,
    AVG(temperature) AS avg_temperature
FROM `single-actor-432513-n6.weather_data.Temperature`
GROUP BY city
ORDER BY avg_temperature DESC;

--------------------------------------------------------------------------
---To find the number of temperature records for each city, I will use the following SQL query
SELECT
    city,
    COUNT(*) AS record_count
FROM `single-actor-432513-n6.weather_data.Temperature`
GROUP BY city
ORDER BY record_count DESC;

--------------------------------------------------------------------------
---To find the city with the highest temperature city, I will use the following SQL query:
SELECT
    city,
    MAX(temperature) AS max_temp
FROM `single-actor-432513-n6.weather_data.Temperature`
GROUP BY city
ORDER BY max_temp DESC
LIMIT 1;

--------------------------------------------------------------------------
---To find the average temperature for each month, I will use the following SQL query:
SELECT
    EXTRACT(MONTH FROM date) AS month,
    AVG(temperature) AS avg_temperature
FROM `single-actor-432513-n6.weather_data.Temperature`
GROUP BY month
ORDER BY month;

--------------------------------------------------------------------------