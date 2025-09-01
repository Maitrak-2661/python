DROP DATABASE IF EXISTS shop_db;
CREATE DATABASE shop_db;
USE shop_db;

CREATE TABLE customers (
  CustomerID INT PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(60),
  Email VARCHAR(80) UNIQUE,
  Address VARCHAR(120)
);

CREATE TABLE orders (
  OrderID INT PRIMARY KEY AUTO_INCREMENT,
  CustomerID INT,
  OrderDate DATE,
  TotalAmount DECIMAL(10,2),
  FOREIGN KEY (CustomerID) REFERENCES customers(CustomerID)
);

CREATE TABLE products (
  ProductID INT PRIMARY KEY AUTO_INCREMENT,
  ProductName VARCHAR(80),
  Price DECIMAL(10,2),
  Stock INT
);

CREATE TABLE order_details (
  OrderDetailID INT PRIMARY KEY AUTO_INCREMENT,
  OrderID INT,
  ProductID INT,
  Quantity INT,
  SubTotal DECIMAL(10,2),
  FOREIGN KEY (OrderID) REFERENCES orders(OrderID),
  FOREIGN KEY (ProductID) REFERENCES products(ProductID)
);

INSERT INTO customers(name,Email,Address) VALUES
('Alice','alice@mail.com','12 Lake Rd'),
('Bob','bob@mail.com','9 Pine St'),
('Carol','carol@mail.com','7 Hill Ave'),
('Dave','dave@mail.com','44 River Way'),
('Eve','eve@mail.com','1 Oak Lane');

INSERT INTO products(ProductName,Price,Stock) VALUES
('Backpack',1299.00,10),('Keyboard',999.00,5),('Mouse',450.00,0),
('Notebook',120.00,50),('Lamp',780.00,12),('Chair',2100.00,3);

INSERT INTO orders(CustomerID,OrderDate,TotalAmount) VALUES
(1, CURDATE() - INTERVAL 5 DAY, 0),
(2, CURDATE() - INTERVAL 40 DAY, 0),
(1, CURDATE() - INTERVAL 10 DAY, 0),
(3, CURDATE() - INTERVAL 2 DAY, 0),
(4, CURDATE() - INTERVAL 20 DAY, 0);

INSERT INTO order_details(OrderID,ProductID,Quantity,SubTotal) VALUES
(1,1,1,1299.00),
(1,4,3,360.00),
(2,2,1,999.00),
(3,6,1,2100.00),
(4,5,2,1560.00),
(5,4,5,600.00);

UPDATE orders o 
JOIN (SELECT OrderID, SUM(SubTotal) as tot FROM order_details GROUP BY OrderID) x
  ON o.OrderID=x.OrderID
SET o.TotalAmount=x.tot;