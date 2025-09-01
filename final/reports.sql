USE uni_manage;

INSERT INTO students(FirstName,LastName,Email,BirthDate,EnrollmentDate)
VALUES ('Ravi','Shah','ravi@univ.com','2002-02-02','2024-08-01');

SELECT * FROM students;

UPDATE courses SET Credits=5 WHERE CourseName='Algorithms';

DELETE FROM enrollments WHERE EnrollmentID=999;

SELECT * FROM students WHERE YEAR(EnrollmentDate) > 2022;

SELECT c.* FROM courses c
JOIN departments d ON c.DepartmentID=d.DepartmentID
WHERE d.DepartmentName='Mathematics' LIMIT 5;

SELECT c.CourseName, COUNT(e.StudentID) AS total_students
FROM courses c LEFT JOIN enrollments e ON c.CourseID=e.CourseID
GROUP BY c.CourseID
HAVING COUNT(e.StudentID) > 1;

SELECT s.StudentID, s.FirstName, s.LastName
FROM students s
WHERE s.StudentID IN (
   SELECT e1.StudentID FROM enrollments e1
   JOIN courses c1 ON e1.CourseID=c1.CourseID AND c1.CourseName='Introduction to SQL'
)
AND s.StudentID IN (
   SELECT e2.StudentID FROM enrollments e2
   JOIN courses c2 ON e2.CourseID=c2.CourseID AND c2.CourseName='Algorithms'
);

SELECT DISTINCT s.StudentID, s.FirstName, s.LastName
FROM students s
JOIN enrollments e ON s.StudentID=e.StudentID
JOIN courses c ON e.CourseID=c.CourseID
WHERE c.CourseName IN ('Introduction to SQL','Data Structures');

SELECT AVG(Credits) AS avg_credits FROM courses;

SELECT MAX(Salary) AS max_cs_salary
FROM instructors i JOIN departments d ON i.DepartmentID=d.DepartmentID
WHERE d.DepartmentName='Computer Science';

SELECT d.DepartmentName, COUNT(DISTINCT e.StudentID) AS students_count
FROM departments d
LEFT JOIN courses c ON d.DepartmentID=c.DepartmentID
LEFT JOIN enrollments e ON c.CourseID=e.CourseID
GROUP BY d.DepartmentID;

SELECT s.FirstName, c.CourseName
FROM students s
JOIN enrollments e ON s.StudentID=e.StudentID
JOIN courses c ON e.CourseID=c.CourseID;

SELECT s.FirstName, c.CourseName
FROM students s
LEFT JOIN enrollments e ON s.StudentID=e.StudentID
LEFT JOIN courses c ON e.CourseID=c.CourseID;

SELECT * FROM students
WHERE StudentID IN (
  SELECT StudentID FROM enrollments
  GROUP BY StudentID HAVING COUNT(*) > 1
);

SELECT StudentID, YEAR(EnrollmentDate) AS enroll_year FROM students;

SELECT CONCAT(FirstName,' ',LastName) AS InstructorName FROM instructors;

SELECT EnrollmentID, StudentID, EnrollmentDate,
       COUNT(*) OVER (ORDER BY EnrollmentDate, EnrollmentID) AS running_total
FROM enrollments;

SELECT FirstName, LastName, EnrollmentDate,
CASE WHEN TIMESTAMPDIFF(YEAR, EnrollmentDate, CURDATE()) >= 4 THEN 'Senior' ELSE 'Junior' END AS Level
FROM students;