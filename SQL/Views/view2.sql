SELECT * FROM collegedb.studentview;

CREATE VIEW TotalMarks AS
SELECT student_id, SUM(marks) AS total
FROM Marks
GROUP BY student_id;