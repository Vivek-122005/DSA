# Write your MySQL query statement below
select ROUND(COUNT(distinct a.player_id)/ COUNT(distinct f.player_id), 2) as fraction
From (
select player_id, min(event_date) as first_login
from Activity
group by player_id
)f
left join Activity a
on a.player_id = f.player_id
and a.event_date = Date_add(f.first_login, interval 1 day)