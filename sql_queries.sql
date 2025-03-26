--Group by using pagination (LIMIT specifies the number of rows to display from top, OFFSET dsplays the rows from specified number--

select * from company_directory.employee_data;

insert into company_directory.employee_data (employee_name, reports_to, salary) values ('nitish', 1002, 500000),('kumar', 1000, 500000), ('kumar', 1000, 500000);

update company_directory.employee_data set reports_to = 1000 where employee_id = 1013;

select * from company_directory.employee_salary;

select employee_name, employee_id from company_directory.employee_data group by employee_name,employee_id order by employee_id;

select * from company_directory.employee_data limit 5; --displays first 5 rows--

select * from company_directory.employee_data limit 5 offset 5; --displays 5 rows after the first 5--

select employee_id, employee_name, salary from company_directory.employee_data order by salary desc limit 5 offset 1; -- ignoring the highest salary--

select employee_name, count(employee_name) as no_of_duplicates from company_directory.employee_data where salary > 300000 group by employee_name having count(employee_name) > 1;

-- In postgresql we cannot write having condition using alias name such as no_of_duplicates form above query

--Having clause is used to filter groups--

select employee_name, count(employee_name) as no_of_duplicates from company_directory.employee_data where salary > 300000 group by employee_name having count(employee_name) > 1 order by no_of_duplicates asc;



