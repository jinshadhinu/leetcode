-- Write your PostgreSQL query statement below
with cte as(select min(order_date) as firstorder_date,
min(customer_pref_delivery_date) as delDate from Delivery group by customer_id )
select round(avg(case when firstorder_date =delDate then 1
else 0
end)*100,2) as immediate_percentage
from cte
;