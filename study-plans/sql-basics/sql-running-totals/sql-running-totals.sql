-- Write your SQL query here
select
    account,
    txn_date,
    amount,
    sum(amount) over(partition by account order by txn_date asc) as running_total
from transactions
order by account asc, txn_date asc, id asc;