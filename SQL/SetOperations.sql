/*All unique records from both tables:*/
SELECT * FROM Employee_India
UNION
SELECT * FROM Employee_USA;

/*All records including duplicates:*/
SELECT * FROM Employee_India
UNION ALL
SELECT * FROM Employee_USA;

/*Only common row*/
SELECT * FROM Employee_India
WHERE (emp_id, emp_name, department, salary) IN (
    SELECT emp_id, emp_name, department, salary FROM Employee_USA
);

/*(Records in India not in USA*/
SELECT * FROM Employee_India
WHERE (emp_id, emp_name, department, salary) NOT IN (
    SELECT emp_id, emp_name, department, salary FROM Employee_USA
);


