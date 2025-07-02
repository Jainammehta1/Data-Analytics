use sakila;
select*from payment;
select sum(amount) as total_amount from payment;/*To calculate the total value*/

select count(customer_id)as countofstaff from customer;/*To calculate the number of assets*/

select avg(amount) as avgquantity from payment;/*Average Calculation*/

select min(amount) as minimumamount from payment;/*Minimum value*/

select max(amount) as minimumamount from payment;/*Maximum Value*/

select truncate(amount,0)as amount from payment;/*To eliminate decimal values*/

select ceil(amount) as ceil from payment;/*Round of to upper value*/

select floor(amount) as ceil from payment;/*Round of to lower value*/
