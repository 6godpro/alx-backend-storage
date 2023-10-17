-- Create a stored procedure ComputeAverageWeightedScoreForUser that
-- computes and store the average weighted score for all students.
-- Requirements:
--   Procedure ComputeAverageScoreForUser is not taking any input.
DELIMITER //
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    DECLARE weighted_average_score FLOAT;

    UPDATE users 
    INNER JOIN (
        SELECT user_id, SUM(weight * score) / SUM(weight) AS weighted_average_score
        FROM projects INNER JOIN corrections
        ON project_id=projects.id
        GROUP BY user_id
    ) AS temp
    ON id=user_id
    SET average_score=temp.weighted_average_score;
END //
DELIMITER ;
