select c.customer_id as Customer,c.age as Age,
i.item_name as Item,sum(o.quantity) as Quantity 
from customers c 
inner join sales s on c.customer_id = s.customer_id
inner join orders o on s.sales_id = o.sales_id
inner join items i on i.item_id = o.item_id 
where c.age between 18 and 35
and o.quantity > 0
group by

C.customer_id,c.age,item_name
