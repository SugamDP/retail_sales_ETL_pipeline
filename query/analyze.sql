-- Find the total sales by store type

SELECT ds.type, sum(fs.weekly_sales) FROM 
dim_store AS ds 
LEFT JOIN
fact_sales AS fs
ON  ds.store = fs.store
GROUP BY ds.type

-- Find total sales by department
SELECT
    dept,
    SUM(weekly_sales) AS total_sales
FROM fact_sales
GROUP BY dept
ORDER BY total_sales DESC;

-- Find the top 10 stores by total sales
SELECT
    store,
    SUM(weekly_sales) AS total_sales
FROM fact_sales
GROUP BY store
ORDER BY total_sales DESC
LIMIT 10;

-- Find total sales by year
SELECT
    dd.year,
    SUM(fs.weekly_sales) AS total_sales
FROM fact_sales AS fs
JOIN dim_date AS dd
    ON fs.date = dd.date
GROUP BY dd.year
ORDER BY dd.year;

-- Find total sales by year and month
SELECT
    dd.year,
    dd.month,
    SUM(fs.weekly_sales) AS total_sales
FROM fact_sales AS fs
JOIN dim_date AS dd
    ON fs.date = dd.date
GROUP BY dd.year, dd.month
ORDER BY dd.year, dd.month;

-- Compare sales during holiday and non-holiday weeks
SELECT
    dd.isholiday,
    SUM(fs.weekly_sales) AS total_sales
FROM fact_sales AS fs
JOIN dim_date AS dd
    ON fs.date = dd.date
GROUP BY dd.isholiday;

-- Find average weekly sales by store type
SELECT
    ds.type,
    AVG(fs.weekly_sales) AS avg_weekly_sales
FROM dim_store AS ds
JOIN fact_sales AS fs
    ON ds.store = fs.store
GROUP BY ds.type
ORDER BY avg_weekly_sales DESC;

-- Find total sales by store type and year
SELECT
    dd.year,
    ds.type,
    SUM(fs.weekly_sales) AS total_sales
FROM fact_sales AS fs
JOIN dim_store AS ds
    ON fs.store = ds.store
JOIN dim_date AS dd
    ON fs.date = dd.date
GROUP BY dd.year, ds.type
ORDER BY dd.year, ds.type;

-- Rank departments by sales within each store
SELECT
    store,
    dept,
    SUM(weekly_sales) AS total_sales,
    RANK() OVER (
        PARTITION BY store
        ORDER BY sum(weekly_sales) DESC
    ) AS sales_rank
FROM fact_sales
GROUP BY store, dept;

-- Compare temperature with sales
SELECT
    df.temperature,
    AVG(fs.weekly_sales) AS avg_weekly_sales
FROM fact_sales AS fs
JOIN dim_feature AS df
    ON fs.store = df.store
    AND fs.date = df.date
GROUP BY df.temperature
ORDER BY df.temperature;