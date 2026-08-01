
CREATE TABLE students(
student_num CHAR(3),
student_Iname VARCHAR(25),
student_fname VARCHAR(25),
enrollment_date DATE,
age INTEGER
);

EXEC sp_help 'students';

INSERT INTO students
(student_num,student_Iname,student_fname,enrollment_date,age)
VALUES
('101','Mokoena','Thabo','2019-05-23',18),
('102','Shilubana','Ndivhuwo','2018-08-13',20),
('103','Baloyi','Tsakani','2017-11-09',19),
('104','Mgangatho','Lukhanyo','2020-03-17',17),
('105','Mofokeng','Lerato','2018-12-05',21),
('106','Mnguni','Nomsa','2018-08-13',18);

SELECT *
FROM students;

INSERT INTO students (student_num,age)
VALUES ('054',7);

SELECT *
FROM students;

INSERT INTO students 
(student_num,student_Iname,enrollment_date)
VALUES 
('076','Vukosi','2021-09-09');

SELECT *
FROM students;

SELECT student_num,age
FROM students;

UPDATE students
SET student_Iname = 'Mark'
WHERE student_num ='104';

UPDATE students
SET age = 22
WHERE enrollment_date < '2019-01-01';

SELECT *
FROM students;

DELETE FROM students
WHERE age = 18;

TRUNCATE TABLE students;

SELECT *
FROM students;