use sakila;
select*from payment;

select date(payment_date) as dates from payment;/*Generates the dates*/

select time(payment_date) as time from payment;/*Generates the tieme*/

select dayname(payment_date) as dayname from payment;/*Generates the name of the day*/

select monthname(payment_date) as monthname from payment;/*Generates the month name*/

select year(payment_date) as year from payment;/*Generates the year dates*/

select hour(payment_date) as hours from payment;/*Generates the hours in 24hrs format*/

select minute(payment_date) as dates from payment;/*Generates the minutes*/






