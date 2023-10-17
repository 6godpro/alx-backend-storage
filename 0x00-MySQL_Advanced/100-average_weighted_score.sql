-- Create a stored procedure ComputeAverageWeightedScoreForUser that
-- computes and store the average weighted score for a student.
-- Requirements:
--   Procedure ComputeAverageScoreForUser is taking 1 input:
--   user_id, a users.id value (you can assume user_id is linked to an existing users)
DELIMITER //
CREATE PROCEDURE ComputeAverageWeightedScoreForUser(id INT)
BEGIN
    DECLARE weighted_average_score FLOAT;

    SELECT SUM(weight * score) / SUM(weight) INTO weighted_average_score
    FROM projects
    INNER JOIN corrections ON project_id=projects.id
    WHERE user_id = id;

    UPDATE users SET average_score=weighted_average_score WHERE users.id=id;
END //
DELIMITER ;
