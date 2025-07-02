use demo_1;
select*from bigbasketproducts;

select product,market_price,	
case
	when market_price<250 then "Urgent Need of Stock"
    else"No requirements"
end as production_details
from bigbasketproducts;
