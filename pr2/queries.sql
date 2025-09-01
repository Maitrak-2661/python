USE corp_analytics;

SELECT o.OrderID, o.TotalAmount, c.FirstName, c.LastName
FROM orders o
INNER JOIN customers c ON o.CustomerID=c.CustomerID;

SELECT c.CustomerID, c.FirstName, o.OrderID, o.TotalAmount
FROM customers c LEFT JOIN orders o ON c.CustomerID=o.CustomerID;

SELECT c.CustomerID, c.FirstName, o.OrderID, o.TotalAmount
FROM customers c RIGHT JOIN orders o ON c.CustomerID=o.CustomerID;

SELECT c.CustomerID, c.FirstName, o.OrderID, o.TotalAmount
FROM customers c LEFT JOIN orders o ON c.CustomerID=o.CustomerID
UNION
SELECT c.CustomerID, c.FirstName, o.OrderID, o.TotalAmount
FROM customers c RIGHT JOIN orders o ON c.CustomerID=o.CustomerID;

SELECT DISTINCT c.*
FROM customers c JOIN orders o ON c.CustomerID=o.CustomerID
WHERE o.TotalAmount > (SELECT AVG(TotalAmount) FROM orders);

SELECT * FROM employees WHERE Salary > (SELECT AVG(Salary) FROM employees);

SELECT OrderID, YEAR(OrderDate) AS yr, MONTH(OrderDate) AS mo FROM orders;

SELECT OrderID, DATEDIFF(CURDATE(), OrderDate) AS days_old FROM orders;

SELECT OrderID, DATE_FORMAT(OrderDate, '%d-%b-%Y') AS pretty_date FROM orders;

SELECT CONCAT(FirstName,' ',LastName) AS FullName FROM customers;

SELECT REPLACE(Email,'john','jonathan') FROM customers WHERE FirstName='John';

SELECT UPPER(FirstName), LOWER(LastName) FROM customers;

SELECT TRIM('   spaced text   ') AS trimmed;

SELECT OrderID, TotalAmount,
       SUM(TotalAmount) OVER (ORDER BY OrderDate, OrderID) AS running_total
FROM orders;

SELECT OrderID, TotalAmount, RANK() OVER (ORDER BY TotalAmount DESC) as rnk
FROM orders;

SELECT OrderID, TotalAmount,
CASE 
  WHEN TotalAmount > 1000 THEN '10% off'
  WHEN TotalAmount > 500 THEN '5% off'
  ELSE 'No discount'
END AS offer
FROM orders;

SELECT FirstName, Salary,
CASE 
  WHEN Salary >= 70000 THEN 'High'
  WHEN Salary >= 50000 THEN 'Medium'
  ELSE 'Low'
END AS category
FROM employees;