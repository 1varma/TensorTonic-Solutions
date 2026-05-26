-- Write your SQL query here
select
    name,
    (case when email is not null then email else 'N/A' end) as display_email,
    (case when deactivated_at is Null then 'active' else 'inactive' end) as status
from customers
where phone is not null
order by name asc;