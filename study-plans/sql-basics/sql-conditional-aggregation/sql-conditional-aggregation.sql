-- Write your SQL query here
select
    department,
    count(*) as total_tickets,
    count(status) filter(where status = 'open') as open_count,
    count(status) filter(where status = 'in_progress') as in_progress_count,
    count(status) filter(where status = 'closed') as closed_count
from tickets
group by department
order by total_tickets desc, department asc;