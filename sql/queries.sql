SELECT * FROM sales;

SELECT country, SUM(amount) AS total_sales
FROM sales
GROUP BY country;

SELECT country, AVG(amount) AS avg_sales
FROM sales
GROUP BY country;

SELECT *,
       ROW_NUMBER() OVER (ORDER BY amount DESC) AS rn
FROM sales;