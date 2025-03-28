select * from company_directory.employee_data;

delete from company_directory.employee_data where employee_name = 'nitish';

--getting annual tax amount using case salary <= 500000 10%tax, salary <= 1000000 15%tax, salary > 1000000 20%tax

select employee_name, salary,
	case
		when salary <= 500000 then salary * 0.10
		when salary <= 1000000 then salary * 0.15
		else salary * 0.20
	end as tax_amount
from company_directory.employee_data;

-- creating another address table with foreign key and joining both tables--

create table company_directory.employee_address (employee_id int, pincode int, city varchar(30), 
	foreign key(employee_id) references company_directory.employee_data(employee_id) on delete cascade); -- (ON DELETE CASCADE) if the primary key row is deleted, the foreign key row also be deleted automatically.

select * from company_directory.employee_address;

INSERT INTO company_directory.employee_address (employee_id, city, pincode) VALUES
(1001, 'Hyderabad', 500045),
(1002, 'Chennai', 500073),
(1000, 'Hyderabad', 500026),
(1005, 'Bangalore', 500088),
(1004, 'Delhi', 500060),
(1003, 'Mumbai', 500038),
(1009, 'Hyderabad', 500095),
(1010, 'Pune', 500032),
(1011, 'Delhi', 500057),
(1012, 'Mumbai', 500069),
(1013, 'Bangalore', 500079);

delete from company_directory.employee_data where employee_id = 1010;

select * from company_directory.employee_data 
	join company_directory.employee_address 
	on company_directory.employee_data.employee_id = company_directory.employee_address.employee_id;

insert into company_directory.employee_data (employee_name, reports_to, salary) values ('teja', 1000, 1000000);

INSERT INTO company_directory.employee_address (employee_id, city, pincode) VALUES (1062, 'Hyderabad', 500045); --gives error since foreign key doesnt present in primary key table.

select * from company_directory.employee_data natural join company_directory.employee_address; -- Natural join joins tables using common columns(employee_id)--

select company_directory.employee_data.employee_id, company_directory.employee_address.city
	from company_directory.employee_data natural join company_directory.employee_address; --extracting specific rows from 2 tables--

select * from company_directory.employee_data 
	inner join company_directory.employee_address 
	on company_directory.employee_data.employee_id = company_directory.employee_address.employee_id; --- Inner join joins tables on specific condition. This is useful if the there are no common table column names and you want to join tables using specific columns--

select company_directory.employee_data.employee_name, company_directory.employee_address.city from company_directory.employee_data
	join company_directory.employee_address -- INNER JOIN and JOIN both are same--
	on company_directory.employee_data.employee_id = company_directory.employee_address.employee_id
	where company_directory.employee_address.city = 'Hyderabad';

-- creating another table named employee_review (Good, neutral, bad) reviews as per year foreign key as employee_id--
create table company_directory.employee_review (
	employee_id int, review varchar(10), review_year int,
	foreign key(employee_id) references company_directory.employee_data(employee_id) on delete cascade);

insert into company_directory.employee_review (employee_id, review, review_year) values (1000, 'good', 2010),
	(1000, 'good', 2012),
	(1002, 'bad', 2020),
	(1005, 'average', 2010),
	(1053, 'bad', 2021),
	(1053, 'average', 2022),
	(1004, 'good', 2024),
	(1003, 'average', 2019),
	(1004, 'good', 2018);

select * from company_directory.employee_review;

select * from company_directory.employee_data
	left join company_directory.employee_review -- left join displays all the rows from left table even if they are not present in right table. The unavailable rows are displayed as null--
	on company_directory.employee_data.employee_id = company_directory.employee_review.employee_id;

select company_directory.employee_data.employee_name from company_directory.employee_data
	left join company_directory.employee_review -- displaying employees who didnt get a review--
	on company_directory.employee_data.employee_id = company_directory.employee_review.employee_id
	where company_directory.employee_review.review is null;

--display employee name, city and review who got good review in 2010--

select company_directory.employee_data.employee_name, company_directory.employee_address.city, company_directory.employee_review.review
	from company_directory.employee_data  -- multiple tables combined to get desired output--
	inner join company_directory.employee_review on company_directory.employee_data.employee_id = company_directory.employee_review.employee_id
	inner join company_directory.employee_address on company_directory.employee_data.employee_id = company_directory.employee_address.employee_id
	where company_directory.employee_review.review = 'good' and company_directory.employee_review.review_year = 2010;

select * from company_directory.employee_review
	right join company_directory.employee_data-- right join displays all the rows even if they are not avaialble in the left table--
	on company_directory.employee_review.employee_id = company_directory.employee_data.employee_id;

select * from company_directory.employee_data
	full join company_directory.employee_review --Full join is the combination both left and right join. It displays all the rows present in left table and right table
	on company_directory.employee_review.employee_id = company_directory.employee_data.employee_id;

select *
	from company_directory.employee_data ed
	cross join company_directory.employee_review er
	order by ed.employee_name; -- Cross join combines each row from table 1 with all the rows from table 2. It gives all possible combinations--

set schema 'company_directory'; 

select * from employee_data ed;