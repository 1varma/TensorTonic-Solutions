-- Write your SQL query here
with daily_stats as (
    select order_date, count(*) as daily_count, sum(amount) as daily_revenue
    from orders
    group by order_date
)
select
    round(avg(daily_count), 2) as avg_daily_orders,
    round(avg(daily_revenue), 2) as avg_daily_revenue,
    (select daily_count from daily_stats order by daily_count desc limit 1) as busiest_day_orders
from daily_stats