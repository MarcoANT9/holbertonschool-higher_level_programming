-- This script sets the score value of "Bob" to 10 without using its name
UPDATE `second_table`
SET
	`score` = 10
WHERE `second_table`.`score` = 14;
