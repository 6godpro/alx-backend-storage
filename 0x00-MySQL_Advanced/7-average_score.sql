-- Creates a stored procedure ComputeAverageScoreForUser
-- that computes and store the average score for a student.
-- Note: An average score can be a decimal
-- Requirements:
-- Procedure ComputeAverageScoreForUser is taking 1 input:
--      student_id, a users.id value (you can assume user_id is linked to an existing users)
DELIMITER //
CREATE PROCEDURE ComputeAverageScoreForUser(student_id INT)
BEGIN
    DECLARE average FLOAT;
    SELECT AVG(score) INTO average FROM corrections WHERE user_id=student_id;
    UPDATE users SET average_score = average WHERE id=student_id;
END //
DELIMITER ;
