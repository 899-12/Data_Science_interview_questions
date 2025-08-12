"""
Write a query to identify the manager with the biggest team size.

You may assume there is only one manager with the largest team size."""
SELECT
       m.name AS manager,
       COUNT(e.id) AS team_size
FROM managers m
JOIN employees e
      ON m.id = e.manager_id
GROUP BY m.id, m.name, m.team
ORDER BY team_size DESC
LIMIT 1;
