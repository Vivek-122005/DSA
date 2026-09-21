# Write your MySQL query statement below
Select v.customer_id, count(v.visit_id) as count_no_trans
FROM Visits as v
left Join Transactions as t
on v.visit_id = t.visit_id
where t.transaction_id is NULL
group by v.customer_id