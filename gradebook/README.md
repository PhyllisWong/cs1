# Grade Book
Application written in Python to track student metrics and grades.

## Classroom class
- Class name
- Subject
- Student Roster
- Assignments (maybe)
- Will consist of various objects to keep track of student grades for each assignment

## Student class
- Student ID
- Student name
- Student attendance
- add assignment: nameOfAssignment, score {key : value}
- update assignment: delete, modify grade, get grade
- List of assignment objects with grade earned (maybe)
- Some way to calculate the total average for the class

### Assignment class
- Categories of work: Exams, quizzes, homework
- Weights of each category (STRETCH)
- Method to calculate the average of each category
- Method to calculate the total class grade
