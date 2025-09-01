USE shop_db;

SELECT * FROM customers;

UPDATE customers SET Address='22 New Street' WHERE name='Bob';

DELETE FROM customers WHERE CustomerID=5;

SELECT * FROM customers WHERE name='Alice';

INSERT INTO orders(CustomerID,OrderDate,TotalAmount) VALUES (1, CURDATE(), 0);

SELECT * FROM orders WHERE CustomerID=1;

UPDATE orders o 
LEFT JOIN (SELECT OrderID, SUM(SubTotal) as tot FROM order_details GROUP BY OrderID) x
ON o.OrderID=x.OrderID
SET o.TotalAmount=COALESCE(x.tot,0)
WHERE o.OrderID=1;

DELETE FROM orders WHERE OrderID=2;

SELECT * FROM orders WHERE OrderDate >= CURDATE() - INTERVAL 30 DAY;

SELECT MAX(TotalAmount) AS Highest, MIN(TotalAmount) AS Lowest, ROUND(AVG(TotalAmount),2) AS Average FROM orders;

SELECT * FROM products ORDER BY Price DESC;

UPDATE products SET Price=Price*1.05 WHERE ProductName='Keyboard';

DELETE FROM products WHERE Stock=0;

SELECT * FROM products WHERE Price BETWEEN 500 AND 2000;

(SELECT * FROM products ORDER BY Price DESC LIMIT 1)
UNION ALL
(SELECT * FROM products ORDER BY Price ASC LIMIT 1);

INSERT INTO order_details(OrderID,ProductID,Quantity,SubTotal) VALUES
(1,2,1,999.00),(3,4,2,240.00),(3,5,1,780.00),(4,6,1,2100.00),(5,1,1,1299.00);

SELECT * FROM order_details WHERE OrderID=1;

SELECT SUM(SubTotal) AS TotalRevenue FROM order_details;

SELECT p.ProductName, SUM(d.Quantity) AS qty
FROM order_details d JOIN products p ON d.ProductID=p.ProductID
GROUP BY d.ProductID
ORDER BY qty DESC
LIMIT 3;

SELECT COUNT(*) AS times_sold FROM order_details d
JOIN products p ON d.ProductID=p.ProductID
WHERE p.ProductName='Keyboard';