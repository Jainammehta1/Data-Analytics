select*from demo_1.esd;
select concat(JobTitle," - ", Department) as Designation from esd;  

select concat_ws(" - ", JobTitle,Department,Gender) as Employee_Details from esd;  

select length(Department) as Digitcount from esd;	/*Counts the length*/

select upper(Fullname) as Names from esd;	/*Converts into Uppercase*/

select lower(Fullname) as Names from esd;	/*Converts into lowercase*/

select left(FullName,4) as username from esd; /* The number of letters will come first based on number*/

select right(Fullname,3) as username from esd; /* The number of letters will come last based on number*/

select mid(Fullname,2,5)as midname from esd; /* [Column,startfrom,endfrom]The number of letters will come from mid based on number*/