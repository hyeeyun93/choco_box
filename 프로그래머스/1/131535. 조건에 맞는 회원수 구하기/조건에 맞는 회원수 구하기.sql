-- 코드를 입력하세요
SELECT COUNT(*) AS USER
FROM USER_INFO
WHERE AGE BETWEEN 20 AND 29 AND JOINED LIKE '%2021%'