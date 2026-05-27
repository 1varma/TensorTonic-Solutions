-- Write your SQL query here
with agg as(
    select
        customer,
        count(*) as order_count,
        sum(amount) as total_spent
    from orders
    group by customer       
)
select * from agg where order_count > 1 order by total_spent desc, customer asc;