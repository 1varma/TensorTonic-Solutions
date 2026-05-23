-- Write your SQL query here
select
    name,
    salary,
    dept_name
from employees as e inner join departments as d on e.dept_id = d.id
order by name asc;