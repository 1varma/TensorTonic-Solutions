-- Write your SQL query here
select
    username,
    signup_date,
    extract('year' from signup_date) as signup_year,
    extract('month' from signup_date) as signup_month,
    extract('quarter' from signup_date) as signup_quarter,
    date_trunc('month', signup_date) as cohort_month
from signups
order by signup_date asc, username asc;