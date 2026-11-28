-- Write your PostgreSQL query sta_tement below
select round(count(distinct a.player_id)::numeric/(select count(distinct player_id)from Activity),2) as fraction
from Activity a
join (select player_id,min(event_date)as first_login from Activity
group by player_id) b
on a.player_id=b.player_id
and a.event_date=b.first_login+INTERVAL '1 day'
;