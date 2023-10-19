-- displays the average temperature (Fahr) by city ordered by temperature(DESC)

SELECT `city`, AVG(`value`) AS `avg_temp`
FROM `temperatures`
GROUP BY `city`
ORDER BY `avg_temp` DESC;
