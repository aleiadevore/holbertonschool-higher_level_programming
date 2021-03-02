-- Lists all records of second_table with name
-- Displays score and name by high score
SELECT score, name from second_table
WHERE name IS NOT NULL
ORDER BY score DESC
