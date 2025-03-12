
--create table departments (
--id  serial primary key,
--name_ varchar (200)
-----
--);

create table employees (
id serial primary key,
first_name varchar(50),
last_name varchar(50),
position_ varchar(50),
salary money,
hire_date date,
department_id int references departments(id)
);


create table projects(
id serial primary key,
name_ varchar(200),
start_date date,
end_date date,
budget money
);




create table tasks (
id serial primary key,
name_ varchar(50),
description vachar (255),
status varchar (50),
project_id int references projects (id),
assignee_id int references employees (id)

);


create table employee_projects (
employee_id int references employees (id),
project_id int references projects (id),
role_ varchar (50)
)
