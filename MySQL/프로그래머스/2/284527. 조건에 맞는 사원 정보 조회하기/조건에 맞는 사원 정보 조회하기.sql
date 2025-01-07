select sum(hg.score) as score,
       he.emp_no,
       he.emp_name,
       he.position,
       he.email
from hr_employees as he
join hr_grade as hg
on he.emp_no = hg.emp_no
group by he.emp_no
order by score desc
limit 1