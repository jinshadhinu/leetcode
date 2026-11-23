-- Write your PostgreSQL query statement below
select b.unique_id,a.name
from Employees a
left join EmployeeUNI b
on a.id=b.id
order by b.unique_id desc;