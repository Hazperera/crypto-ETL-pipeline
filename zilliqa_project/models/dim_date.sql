-- models/dim_date.sql

WITH dates AS (
  SELECT
    day
  FROM
    UNNEST(GENERATE_DATE_ARRAY('2020-01-01', '2030-12-31', INTERVAL 1 DAY)) AS day
)

SELECT
  day AS date,
  EXTRACT(YEAR FROM day) AS year,
  EXTRACT(MONTH FROM day) AS month,
  EXTRACT(DAY FROM day) AS day,
  EXTRACT(DAYOFWEEK FROM day) AS day_of_week,
  FORMAT_TIMESTAMP('%A', day) AS day_name,
  FORMAT_TIMESTAMP('%B', day) AS month_name,
  EXTRACT(WEEK FROM day) AS week,
  CASE
    WHEN EXTRACT(DAYOFWEEK FROM day) IN (1, 7) THEN 'Weekend'
    ELSE 'Weekday'
  END AS weekend_weekday
FROM
  dates
ORDER BY
  day
