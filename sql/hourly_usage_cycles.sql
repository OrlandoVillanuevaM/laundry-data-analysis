CREATE TABLE hourly_usage_p AS
SELECT 
    hour,
    COUNT(*) AS active_cycles
FROM (
    SELECT 
        generate_series(
            DATE_TRUNC('hour', start_time),
            DATE_TRUNC('hour', end_time),
            interval '1 hour'
        ) AS hour
    FROM Usage_Cycles
) t
GROUP BY hour;
