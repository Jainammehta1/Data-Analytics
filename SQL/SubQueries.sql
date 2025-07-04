/*A subquery is a query inside another query. It is used to perform 
intermediate logic, like fetching a value or filtering rows, before the 
outer query runs
*/
SELECT student_name,
       (SELECT SUM(marks) 
        FROM Marks m 
        WHERE m.student_id = s.student_id) AS total_marks /*Inner Query*/
FROM Students s
ORDER BY total_marks DESC; /*Outer Query*/

select student_name
FROM students
WHERE student_id IN (
    SELECT student_id FROM Marks
    WHERE course_id = (
        SELECT course_id FROM Courses WHERE course_name = 'Database Systems'
    )
);


