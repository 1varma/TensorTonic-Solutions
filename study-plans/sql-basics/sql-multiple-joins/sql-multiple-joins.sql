-- Write your SQL query here
select
    username,
    experiment_name,
    variant,
    revenue
from users as u 
    inner join experiment_assignments as e on u.id = e.user_id
    inner join conversions as c on c.user_id = u.id
order by experiment_name asc, revenue desc, username asc;