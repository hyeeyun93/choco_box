-- 입양 시각 구하기(1)
select hour(datetime) as `hour`,
       count(*) as `count`
from animal_outs
where hour(datetime) between 9 and 20
group by hour
order by hour ;