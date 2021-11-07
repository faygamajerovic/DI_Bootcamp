-- Database: bootcamp

-- DROP DATABASE IF EXISTS bootcamp;

-- select * from students
-- select
--    first_name,
--    last_name
-- from students;
-- select first_name, last_name from students where first_name = 'Marc'  and 
-- last_name = 'Benichou' ;
-- select first_name, last_name from students where first_name = 'Marc'  or 
-- last_name = 'Benichou' ;
-- select first_name, last_name from students where first_name LIKE '%a%';
-- -- select first_name, last_name from students where first_name LIKE 'a%';
-- select first_name, last_name from students where first_name LIKE '%a';
-- select first_name, last_name from students where first_name like '%a-';
-- select first_name, last_name from students where id = 1 or id = 3
select first_name, last_name, birth_date from students where birth_date >= '01-01-2000';
