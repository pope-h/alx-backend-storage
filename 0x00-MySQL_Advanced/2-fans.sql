-- Lists ranks country origins of bands, ordered by number of fans
SELECT origin, SUM(fans) as nb_fans
FROM metal_bands
GROUP BY origin
ORDER BY nb_fans DESC;
