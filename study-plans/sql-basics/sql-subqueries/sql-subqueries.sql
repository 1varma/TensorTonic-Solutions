-- Write your SQL query here
select
    name,
    price,
    round(price - (select avg(price) from products), 2) as vs_avg
from products
where id in (select distinct product_id from sales)
order by vs_avg desc, name asc;