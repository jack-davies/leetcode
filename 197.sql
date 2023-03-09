# Write your MySQL query statement below
select w1.id from Weather w1 left join Weather w2
on w2.recordDate = subdate(w1.recordDate, 1)
where w1.temperature > w2.temperature
