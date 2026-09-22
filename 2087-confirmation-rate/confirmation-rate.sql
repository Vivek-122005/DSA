# Write your MySQL query statement below
select s.user_id, 
    ROUND(
        COALESCE(AVG(c.action = 'confirmed'),0)
    ,2) as confirmation_rate
FROM Signups as s
left join Confirmations as c
on s.user_id = c.user_id
group by s.user_id