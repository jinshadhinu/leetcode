# Write your MySQL query statement below
select v.customer_id, count(t.transaction_id is NULL)
as count_no_trans
from Visits v
left JOIN Transactions t
on v.visit_id = t.visit_id
where t.transaction_id is NULL
group by v.customer_id;