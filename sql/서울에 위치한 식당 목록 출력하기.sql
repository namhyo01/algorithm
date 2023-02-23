-- 코드를 입력하세요
SELECT ri.rest_id, rest_name, food_type, favorites,address,round(avg(review_score),2) as score
FROM rest_info ri, rest_review rr
where ri.rest_id = rr.rest_id
group by ri.rest_id, rest_name, food_type, favorites, address
having ri.address like '서울%'
order by score desc, favorites desc