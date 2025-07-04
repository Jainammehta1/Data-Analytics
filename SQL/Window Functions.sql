use collegedb;
/* Gives each row a unique number*/
SELECT student_id, student_name, department,
       ROW_NUMBER() OVER (PARTITION BY department ORDER BY student_name) AS row_num
FROM Students;

/* Rank with gaps if marks are tied
If two students get 95, next rank will be 3 (1, 1, 3…)
*/
SELECT student_id, course_id, marks,
RANK() OVER (ORDER BY marks DESC) AS ran
FROM Marks;

/* Rank without gaps*/

SELECT student_id, marks,
       DENSE_RANK() OVER (ORDER BY marks DESC) AS denserank
FROM Marks;

/*Running total (or cumulative sum)*/
SELECT student_id, marks,
       SUM(marks) OVER (PARTITION BY student_id ORDER BY course_id) AS total_so_far
FROM Marks;

