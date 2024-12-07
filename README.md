Author:
Dominique Warren

Date Created:
November 30 2024

Course:
ITT103

Purpose of code:

The purpose of this program is to create a basic program that enables administrators to add courses, register students, enroll students within courses and manage payments.

Since this program is a basic use of a registration and payment system it would most likely not be used for prefessional use with a huge amount of data. Below I show some limitations of this system

Lmimitations:
1. Allows user to enter numbers for names and special chracters
2. Will allow user to have a different course ID but with same course name 


How to run:

Insert the (code) into your IDE and hit control + enter to run

Once the code is active a menu should be displayed

Menu:

1. Register Student
2. Add Course
3. Enroll Student within a Course
4. All courses
5. Student Balance
6. Registered Students
7. Students within a course
8. Payments
9. Exit

Course 

A class which has the attributes of:

.Course_ID (Eg ITT211)
. Name ( Eg Computer Data Analysis)
. Fee

Student

A class with the attributes of:

. Student_ID
. Name
. Email

Methods:

. Enroll (Adds a course to the student’s list and updates their balance. Prevents duplicate enrollments.)

. get_total_fee(): Calculates the total fees for all enrolled courses.

Registration_System:

A course with the attributes of:

. Courses ( A list of available courses)

. Students (A dictionary of registered students, where the key is student_id and the value is the Student object.)


Methods:

. add_course(course_id, name, fee): Adds a new course.

. register_student(student_id, name, email): Registers a new student.

. enroll_in_course(student_id, course_id): Enrolls a student in a specified course

. calculate_payment(student_id): Processes payments. Requires at least 40% of the balance to confirm registration and updates the remaining balance

. check_student_balance(student_id): Displays the current balance of a specific student.

. show_courses(): Lists all available courses.

. show_registered_students(): Lists all registered students

. show_students_in_course(course_id): Lists all students enrolled in a specific course.
