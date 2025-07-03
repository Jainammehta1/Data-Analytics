use demo_1;

select products1.productName,orderdetails.quantityOrdered from products1 
inner join orderdetails
on products1.productCode= orderdetails.productCode;

select products1.productName,orderdetails.quantityOrdered from products1 
left join orderdetails
on products1.productCode= orderdetails.productCode;

select products1.productName,orderdetails.quantityOrdered from products1 
right join orderdetails
on products1.productCode= orderdetails.productCode;

select *from products1 cross join orderdetails
on products1.productCode= orderdetails.productCode;

/*

| Join Type    | Matches?                        | Notes                                |
| ------------ | ------------------------------- | ------------------------------------ |
| `INNER JOIN` | Both tables                     | Only matching rows are returned.     |
| `LEFT JOIN`  | All from left (`products1`)     | NULLs for no match in right.         |
| `RIGHT JOIN` | All from right (`orderdetails`) | NULLs for no match in left.          |
| `CROSS JOIN` | All combinations                | No ON clause; use `WHERE` if needed. |

*/
