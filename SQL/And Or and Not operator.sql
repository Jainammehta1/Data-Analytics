Select*from demo_1.esd;
select FullName,JobTitle,City,AnnualSalary from demo_1.esd where JobTitle="Sr. Manger" and City="Seattle";
select FullName,JobTitle,Country,AnnualSalary from demo_1.esd where Gender="Female" or Country="China";
select*from demo_1.esd where not Gender="Female"