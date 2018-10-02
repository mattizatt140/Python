class Student(object):
    Id = 0
    def __init__(self, name):
        self.name = name
        self.lastName = self.name.split(' ')[-1]
        self.IdNum = Student.Id
        Student.Id += 1
    def __str__(self):
        return str(self.IdNum).zfill(4) + ": " + self.name
    def __lt__(self, other):
        if self.lastName == other.lastName:
            return self.name < other.name
        return self.lastName < other.lastName
    def getIdNum(self):
        return self.IdNum

class Grades(object):
    #A mapping from students to a list of grades
    def __init__(self):
        #Create empty grade book
        #Grades stores Student ID and corresponding grade
        self.students = []
        self.grades = {}
        self.isSorted = True
    def addStudent(self, student):
        #Assumes: student is of type Student
        #Adds student to the grade book
        assert type(student) == Student, 'addStudent arg(student) not of type Student' #Confirm proper data passed in
        if student in self.students: #Avoid duplicate entries
            raise ValueError('Duplicate student')

        self.students.append(student) 
        self.grades[student.getIdNum()] = []
        self.isSorted = False
    def addGrade(self, student, grade):
        #Assumes: grade is of type float or int
        #Adds student's grade to grade book
        assert type(grade) == int or type(grade) == float, 'addGrade arg(grade) not of type int or float'
        assert type(student) == Student, 'addGrade arg(student) not of type Student'

        try:
            self.grades[student.getIdNum()].append(grade)
        except KeyError:
            raise ValueError('Student not in grade book')
    def getGrade(self, student):
        #Assumes: student is of type Student
        #Returns student's grade from grade book
        assert type(student) == Student, 'getGrade arg(student) not of type Student'

        try:
            return self.grades[student.getIdNum()][:]
        except KeyError:
            raise ValueError('Student not in grade book')
    def allStudents(self):
        #Returns list of students in grade book
        if not self.isSorted:
            self.students.sort()
            self.isSorted = True
        for s in self.students:
            yield s

def gradeReport(course):
    #Assumes: course is of type grades
    #Return grade report
    assert type(course) == Grades, 'gradeReport arg(course) not of type Grades'
    report = []
    for s in course.allStudents():
        tot = 0.0
        numGrades = 0
        for g in course.getGrades(s):
            tot += g
            numGrades += 1
        try:
            average = tot/numGrades
            report.append(str(s) + '\'s mean grade is ' + str(average))
        except ZeroDivisionError:
            report.append(str(s) + ' has no grades')
    return '\n'.join(report)