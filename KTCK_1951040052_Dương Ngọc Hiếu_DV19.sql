#Câu 2
#Cho hai bảng dữ liệu thuộc cơ sở dữ liệu
a)Truy suất tổng điểm (grade) cho mỗi thành phố (city)
select city, SUM(grade) sum_grade from customer group by city
b) Truy suất tất cả khách hàng (customer) mà có người môi giới (sales_man) tương ứng có hoa hồng >0,12, sắp xếp theo customer_id
select customer_id, name, cust_name, commission
from customer cus join salesman sal
on cus.salesman_id=sal.salesman_id
where commission >0.12 order by customer_id