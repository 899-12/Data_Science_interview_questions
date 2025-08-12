"""
We’re given two tables, a users table with demographic information and the neighborhood they live in and a neighborhoods table.

Write a query that returns all neighborhoods that have 0 users. """

SELECT n.id,
       n.name
FROM neighborhoods n
LEFT JOIN users u
       ON n.id = u.neighborhood_id
WHERE u.id IS NULL;
