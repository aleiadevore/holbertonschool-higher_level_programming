-- Creates a second table and several rows
CREATE TABLE IF NOT EXISTS second_table (
id INT,
name VARCHAR(256),
score INT);
INSERT INTO second_table
VALUES (1, 'John', 10);
INSERT INTO second_table
VALUES (2, 'Alex', 2);
INSERT INTO second_table
VALUES (3, 'Bob', 14);
INSERT INTO second_table
VALUES (4, 'George', 8);
