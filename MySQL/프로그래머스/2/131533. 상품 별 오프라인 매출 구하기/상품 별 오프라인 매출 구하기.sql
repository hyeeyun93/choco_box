-- 상품 별 오프라인 매출 구하기
select p.product_code,
       sum(p.price * os.sales_amount) as `sales`
from offline_sale as os
left join product as p
on os.product_id = p.product_id
group by p.product_code
order by sales desc, p.product_code