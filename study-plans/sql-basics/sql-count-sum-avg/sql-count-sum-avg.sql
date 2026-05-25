-- Write your SQL query here
select
    category,
    count(*) as total_sales,
    sum(amount) as total_revenue,
    AVG(CAST(discount AS DECIMAL(10,2))) FILTER (WHERE discount IS NOT NULL) AS avg_discount,
from sales
group by category
order by total_revenue desc, category asc;