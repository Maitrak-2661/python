DROP DATABASE IF EXISTS corp_analytics;
CREATE DATABASE corp_analytics;
USE corp_analytics;

CREATE TABLE customers (
  CustomerID INT PRIMARY KEY AUTO_INCREMENT,
  FirstName VARCHAR(40),
  LastName VARCHAR(40),
  Email VARCHAR(80),
  RegistrationDate DATE
);

CREATE TABLE orders (
  OrderID INT PRIMARY KEY AUTO_INCREMENT,
  CustomerID INT,
  OrderDate DATE,
  TotalAmount DECIMAL(10,2),
  FOREIGN KEY (CustomerID) REFERENCES customers(CustomerID)
);

CREATE TABLE employees (
  EmployeeID INT PRIMARY KEY AUTO_INCREMENT,
  FirstName VARCHAR(40),
  LastName VARCHAR(40),
  Department VARCHAR(40),
  HireDate DATE,
  Salary DECIMAL(10,2)
);

INSERT INTO customers(FirstName,LastName,Email,RegistrationDate) VALUES
('John','Doe','john.doe@email.com','2022-03-15'),
('Jane','Smith','jane.smith@email.com','2021-11-02'),
('Alan','Turing','alan@lab.com','2023-08-14');

INSERT INTO orders(CustomerID,OrderDate,TotalAmount) VALUES
(1,'2023-07-01',150.50),(2,'2023-07-03',200.75),(1,'2024-02-01',400.00);

INSERT INTO employees(FirstName,LastName,Department,HireDate,Salary) VALUES
('Mark','Johnson','Sales','2020-01-15',50000.00),
('Susan','Lee','HR','2021-03-20',55000.00),
('Priya','Shah','Sales','2019-06-10',62000.00),
('Vik','Patel','IT','2018-09-05',75000.00);