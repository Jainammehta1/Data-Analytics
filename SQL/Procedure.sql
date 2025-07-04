/*A Stored Procedure is a precompiled block of SQL statements 
stored in the database. You can call it whenever needed. It's useful for
 repetitive tasks, business logic, and complex operations.
 */
 
Delimiter &&
create procedure get_data()
begin
	select*from students;
end &&
Delimiter ;
call get_data()

/*To get Student info*/
DELIMITER $$

CREATE PROCEDURE GetStudentInfo(IN stu_id INT)
BEGIN
    SELECT * FROM Students
    WHERE student_id = stu_id;
END $$

DELIMITER ;
CALL GetStudentInfo(1);

/*Procedure to Insert a New Student*/

DELIMITER $$

CREATE PROCEDURE AddStudent(
    IN id INT,
    IN name VARCHAR(100),
    IN age INT,
    IN dept VARCHAR(50)
)
BEGIN
    INSERT INTO Students(student_id, student_name, age, department)
    VALUES (id, name, age, dept);
END $$

DELIMITER ;
CALL AddStudent(5, 'Neha', 22, 'CS');

/*Drop Procedure-Not Reccomended
DROP PROCEDURE IF EXISTS GetStudentInfo;
*/


    
