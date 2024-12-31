-- 성분으로 구분한 아이스크림 총 주문량
select ii.ingredient_type,
       sum(fh.total_order) as total_order
from first_half as fh
join icecream_info as ii
on fh.flavor = ii.flavor
group by ii.ingredient_type
order by total_order