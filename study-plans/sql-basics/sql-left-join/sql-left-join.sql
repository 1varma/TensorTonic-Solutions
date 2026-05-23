-- Write your SQL query here
select
    name,
    city,
    sum(coalesce(amount, 0)) as total_spent
from customers as c left join orders as o on c.id = o.customer_id
group by name, city
order by total_spent desc, name asc;