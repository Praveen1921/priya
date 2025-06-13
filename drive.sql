-- Step 1: Create the database
CREATE DATABASE IF NOT EXISTS placement_db;
USE placement_db;

-- Step 2: Table to store registered students
CREATE TABLE placement_registration (
    id INT AUTO_INCREMENT PRIMARY KEY,
    student_id VARCHAR(50) NOT NULL,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    phone VARCHAR(15) NOT NULL,
    department VARCHAR(50) NOT NULL,
    graduation_year YEAR NOT NULL,
    company VARCHAR(100),
    status VARCHAR(50)
);

select *from placement_registration;

-- Step 3: Table for company placement records (suthan.html - optional, for later use)
CREATE TABLE placements (
    id INT AUTO_INCREMENT PRIMARY KEY,
    company VARCHAR(100) NOT NULL,
    position VARCHAR(100) NOT NULL,
    package FLOAT NOT NULL
);
select *from placements;

-- Step 4: Table for student profiles (stu.html form)
CREATE TABLE student_profiles (
    id INT AUTO_INCREMENT PRIMARY KEY,
    student_id VARCHAR(50) NOT NULL,
    name VARCHAR(100) NOT NULL,
    course VARCHAR(100),
    email VARCHAR(100)
);
select *from student_profiles;
-- Step 5: Users table (for login - optional, if you add login logic later)
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password VARCHAR(100) NOT NULL  -- Ideally store hashed passwords!
);

CREATE TABLE student_profiles (
    id INT AUTO_INCREMENT PRIMARY KEY,
    student_id VARCHAR(50) NOT NULL,
    name VARCHAR(100) NOT NULL,
    course VARCHAR(100),
    email VARCHAR(100)
);

CREATE TABLE placements (
    id INT AUTO_INCREMENT PRIMARY KEY,
    student_id VARCHAR(50),
    company VARCHAR(100),
    position VARCHAR(100),
    package FLOAT,
    status VARCHAR(50)
);

INSERT INTO users (username, password) VALUES ('admin', 'admin123');

select *from users;