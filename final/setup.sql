DROP DATABASE IF EXISTS uni_manage;
CREATE DATABASE uni_manage;
USE uni_manage;

CREATE TABLE students (
  StudentID INT PRIMARY KEY AUTO_INCREMENT,
  FirstName VARCHAR(40),
  LastName VARCHAR(40),
  Email VARCHAR(80),
  BirthDate DATE,
  EnrollmentDate DATE
);

CREATE TABLE departments (
  DepartmentID INT PRIMARY KEY AUTO_INCREMENT,
  DepartmentName VARCHAR(60)
);

CREATE TABLE courses (
  CourseID INT PRIMARY KEY AUTO_INCREMENT,
  CourseName VARCHAR(80),
  DepartmentID INT,
  Credits INT,
  FOREIGN KEY (DepartmentID) REFERENCES departments(DepartmentID)
);

CREATE TABLE instructors (
  InstructorID INT PRIMARY KEY AUTO_INCREMENT,
  FirstName VARCHAR(40),
  LastName VARCHAR(40),
  Email VARCHAR(80),
  DepartmentID INT,
  Salary DECIMAL(10,2) DEFAULT 60000.00,
  FOREIGN KEY (DepartmentID) REFERENCES departments(DepartmentID)
);

CREATE TABLE enrollments (
  EnrollmentID INT PRIMARY KEY AUTO_INCREMENT,
  StudentID INT,
  CourseID INT,
  EnrollmentDate DATE,
  FOREIGN KEY (StudentID) REFERENCES students(StudentID),
  FOREIGN KEY (CourseID) REFERENCES courses(CourseID)
);

INSERT INTO students(FirstName,LastName,Email,BirthDate,EnrollmentDate) VALUES
('John','Doe','john.doe@email.com','2000-01-15','2022-08-01'),
('Jane','Smith','jane.smith@email.com','1999-05-25','2021-08-01'),
('Kia','Patel','kia@univ.com','2001-04-11','2023-08-01');

INSERT INTO departments(DepartmentName) VALUES ('Computer Science'),('Mathematics'),('Physics');

INSERT INTO courses(CourseName,DepartmentID,Credits) VALUES
('Introduction to SQL',1,3),
('Data Structures',2,4),
('Algorithms',1,4),
('Calculus I',2,3);

INSERT INTO instructors(FirstName,LastName,Email,DepartmentID,Salary) VALUES
('Alice','Johnson','alice.johnson@univ.com',1,73000),
('Bob','Lee','bob.lee@univ.com',2,65000),
('Nina','Roy','nina.roy@univ.com',1,80000);

INSERT INTO enrollments(StudentID,CourseID,EnrollmentDate) VALUES
(1,1,'2022-08-01'),(2,2,'2021-08-01'),(1,3,'2022-08-10'),
(3,1,'2023-08-01'),(3,3,'2023-08-02'),(2,1,'2021-08-10');