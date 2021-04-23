-- Create TABLE

CREATE TABLE Persons (
    PersonID int,
    LastName varchar(255),
    FirstName varchar(255),
    Address varchar(255),
    City varchar(255)
);
--Adding column
ALTER TABLE Persons
ADD age int;

--modigying datatype of a column
alter table persons modify( age varchar(14));


--primary key
CREATE TABLE Persons (
    ID int NOT NULL PRIMARY KEY,
    LastName varchar(255) NOT NULL,
    FirstName varchar(255),
    Age int
);

--sir's option wuth multiple column
create table dependent (
essn references employee,
dependent_name varchar(20),
gender char(1),
bdate date,
relationship varchar(12), 
primary key(essn, dependent_name) );

--to see the schema
desc persons;

--entering value
insert into employee values 
('Richard', 'K', 
'Marini', '653653653', '30-dec-82', '98 Oak 
Forest, Katy, TX', 'M', 37000, '888665555', 4 );

--entering 

INSERT into vaccination_center values(&hospital_name,&address,&phone_no,&opening_time,&closing_time);