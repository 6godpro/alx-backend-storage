-- Create a stored procedure AddBonus that adds a new correction for a student.
--
-- Requirements:
-- Procedure AddBonus is taking 3 inputs (in this order):
--      user_id, a users.id value (you can assume user_id is linked to an existing users).
--      project_name, a new or already exists projects - if no projects.name found in the
--      table, you should create it.
--      score, the score value for the correction.
DELIMITER //
CREATE PROCEDURE AddBonus(user_id INT, project_name VARCHAR(255), score INT)
BEGIN
    -- create a temporary variables
	DECLARE total INT;
	DECLARE project_id INT;
    -- check if the project exists
	SELECT COUNT(*) INTO total FROM projects WHERE name=project_name;
    -- if it doesn't exist, create a new project with the project_name given
	IF total = 0 THEN
	   INSERT INTO projects (name) VALUES (project_name);
       SET project_id = LAST_INSERT_ID();
    -- if it does, retrieve the id of the project with the given name
    ELSE
	   SELECT id INTO project_id FROM projects WHERE name=project_name;
	END IF;
    -- create a new corrections record with the details
	INSERT INTO corrections (user_id, project_id, score) VALUES (user_id, project_id, score);
END //
DELIMITER ;
