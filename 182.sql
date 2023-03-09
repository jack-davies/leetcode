# Write your MySQL query statement below
select email from
(select email, count(email) as c from Person
group by email) e
where e.c > 1
