# -*- coding: utf-8 -*-
"""Warren.Dominique-Course_Registration-ITT103-F2024

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1LhG5oiaxNAPlNxnl6VkiyVeD9vW8ZEvb
"""

#Created a Course Class with the attributes of Course ID, Name and Fee
class Course:
  def __init__(self, course_ID, name, fee):
    self.course_ID = course_ID
    self.name = name
    self.fee = fee

#Created a Student Class with the necessary attributes
class Student:
  def __init__(self, student_ID, name, email):
    self.student_ID = student_ID
    self.name = name
    self.email = email
    self.courses = [] # A list of courses
    self.balance = 0.0 # Set balance to 0
# Checks wether the course was already added to the list given in self.courses then, Appends or adds whatever course if the course was not already within the list.
  def enroll(self, course):
    if course not in self.courses:
      self.courses.append(course)
      self.balance += course.fee # Adds the course fee and updates the student balance
    else:
      print(f"Student {self.name} is already enrolled in {course.name}")

# Retruns the total amount within the balance attribute
  def get_total_fee(self):
    return self.balance


class Registration_System:
  def __init__(self):
    self.courses = []
    self.students = {}

# Goes through each courses within the self.courses list then checks wether the course already exists
  def add_course(self, course_ID, name, fee):
    for course in self.courses:
      if course.course_ID == course_ID:
        print(f"Course with ID {course_ID} already exists.")
        return  # Exits early if the course exists

# Creates a new object using the Course Class and appended/added the new course within the list
    new_course = Course(course_ID, name, fee)
    self.courses.append(new_course)
    print(f'Course "{name}" added successfully.')

# Checks to see if the student ID is already in the dictionary of self.students
  def register_student(self,student_ID, name, email):
    if student_ID in self.students:
      print(f"Stduent {student_ID} is already registered")
    else:
# Adds the newly created student object to the dictionary of students using the student ID as a key
      student = Student(student_ID, name, email) # Created a new object using the student class
      self.students[student_ID] = student
      print(f'Student "{name}" registered successfully.')



  def enroll_in_course(self,student_ID, course_ID):
# Checks if student exists then searches for the course ID
    if student_ID not in self.students:
      print(f"Student with ID {student_ID} not found.")
      return
# Goes through the self.courses list then checks each course to see if the course_ID matches a given course_ID
    course = None # Set variable to none
    for i in self.courses:
      if i.course_ID == course_ID:
        course = i # If match is found will hold the course object
        break # Exits loop if the course is found

# Checks if course can be found
    if course is None:
      print(f"Course with ID {course_ID} not found.")
      return
 # Uses the student ID to to enroll a student in the founded courses
    student = self.students[student_ID]
    student.enroll(course)
    print(f"Student {student.name} successfully enrolled in {course.name}.")

# This line of code handles payments and shows how much a student owes
  def calculate_payment(self,student_ID):
    if student_ID not in self.students: # Checks to see if the student ID is within the dictionary
      print(f"Student with ID {student_ID} not found.")
      return

    student = self.students[student_ID] # Created an object using the student class and retrived the student ID
    total_fees = student.get_total_fee() # Returns the total amount of fees student owes

    if total_fees == 0:
      print(f"Student {student.name} is not enrolled in any courses.")
      return

    print(f"Total fee for {student.name}: {total_fees}")
    minimum_payment = 0.4 * total_fees
    try:
      payment = float(input("Enter payment minimum_payment: "))
    except ValueError:
      print("Please use numbers only")
      return

#Checks if payment made is less than the inteded target amount
    if payment < minimum_payment:
      print(f"Payment must be at least {minimum_payment}.")
      return
    else:
      student.balance -= payment # Subtracts payemnt and updaes the student balance
      print(f"Payment of {payment} accepted. Remaining balance: {student.balance}.")


  def check_student_balance(self,student_ID):
# Checks wether student exsits then shows their remaining balance
    if student_ID not in self.students:
      print(f"Student with ID {student_ID} not found.")
      return

    student = self.students[student_ID]
    print(f"Student {student.name} has a balance of {student.balance} remaining.")

# Shows the available courses
  def show_courses(self):
    print("All Courses Available: ")
    for course in self.courses:
      print(f"Course_ID: {course.course_ID}, Name: {course.name}, Fee: {course.fee}")

# Creates a loop to look through all items within the self.students dictonary
  def show_registered_students(self):
    for student_ID, student in self.students.items(): # Creates a loop to look through all items within the self.students dictonary
      print(f"Student ID: {student_ID}, Name: {student.name}, Email: {student.email}")

# Created a loop that goes over all the student object in self.students
  def show_students_in_course(self,course_ID):
    print(f"Students enrolled in Course ID {course_ID}:")
    for student in self.students.values(): # The .values() function retrives all values ignoring the keys
      for course in student.courses:
        if course.course_ID == course_ID:
          print(student.name)
          break
    else:
      print("No students found for this course.")

# Created a menu
def menu():
  system = Registration_System()
  while True:
    print("Welcome to our User Interface please select an option: ")
    print("1.Register Student")
    print("2.Add Course")
    print("3.Enroll Student within a Course")
    print("4.All Courses")
    print("5.Student Balance")
    print("6.Registered Students")
    print("7.Student within a course")
    print("8.Payments")
    print("9.Exit")

    user_choice = input("Please select an option: ")

    if user_choice == "1":
      student_ID = input("Enter student ID: ")
      name = input("Enter student name: ")
      email = input("Enter student email: ")
      system.register_student(student_ID, name, email)

    elif user_choice == "2":
     course_ID = input("Enter course ID: ")
     name = input("Enter course name: ")
     fee = float(input("Enter course fee: "))
     system.add_course(course_ID, name, fee)

    elif user_choice == "3":
      student_ID = input("Enter student ID: ")
      course_ID = input("Enter course ID: ")
      system.enroll_in_course(student_ID, course_ID)

    elif user_choice == "4":
      system.show_courses()

    elif user_choice == "5":
      student_ID = input("Enter student ID: ")
      system.check_student_balance(student_ID)


    elif user_choice == "6":
      system.show_registered_students()

    elif user_choice == "7":
      course_ID = input("Enter course ID: ")
      system.show_students_in_course(course_ID)

    elif user_choice == "8":
      student_ID = input("Enter student ID: ")
      system.calculate_payment(student_ID)

    elif user_choice == "9":
     print("Exiting system.")
     break

    else:
      print("Invalid choice. Please try again.")


menu()

#I CERTIFY THAT I HAVE NOT GIVEN OR RECEIVED ANY UNAUTHORIZED ASSISTANCE ON THIS ASSIGNMENT.