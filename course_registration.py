from dataclasses import dataclass


@dataclass
class Course:
    name: str
    code: str
    max_students: int
    students: list = None

    def __str__ (self):
        return f"{self.name} - {self.code}"
    
    def addStudent(self, student):
        if self.students == None:
            self.students = []
        self.students.append(student)

    def removeStudent(self, student):
        if self.students == None:
            self.students = []
        if student in self.students:
            self.students.remove(student)

@dataclass
class Student:
    name: str
    id: str
    courses: list = None

    def __str__ (self):
        return f"{self.name} - {self.id}"

    def registerCourse(self, course: Course):
        if self.courses == None:
            self.courses = []
        self.courses.append(course)

    def unregisterCourse(self, course: Course):
        if self.courses == None:
            self.courses = []
        if course in self.courses:
            self.courses.remove(course)

@dataclass
class CourseRegistration:
    courses: list = None
    students: list = None

    def addCourse(self, course: Course):
        if self.courses == None:
            self.courses = []
        self.courses.append(course)

    def addStudent(self, student: Student):
        if self.students == None:
            self.students = []
        self.students.append(student)

    def registerStudent(self, student: Student, course: Course):
        if course.students == None:
            course.students = []
        if course in self.courses and student in self.students:
            if  course.max_students > len(course.students):
                course.addStudent(student)
                student.registerCourse(course)
                print(f"Student {student.name} registered for course {course.name} successfully")
            else:
                print(f"Course {course.name} is full")
        else:
            print("Student or course not found")

    def unregisterStudent(self, student: Student, course: Course):
        if course in self.courses and student in self.students:
            if student in course.students:
                course.removeStudent(student)
                student.unregisterCourse(course)
                print(f"Student {student.name} unregistered for course {course.name} successfully")
            else:
                print(f"Student {student.name} not registered for course {course.name}")
        else:
            print("Student or course not found")

    def getStudentsForCourse(self, course: Course):
        if course in self.courses:
            res = []
            if course.students == None:
                course.students = []
            for student in course.students:
                res.append(student.__str__())
            return res
        else:
            print("Course not found")

    def getCoursesForStudent(self, student: Student):
        if student in self.students:
            res = []
            if student.courses == None:
                student.courses = []
            for course in student.courses:
                res.append(course.__str__())
            return res
        else:
            print("Student not found")

    def getAllStudents(self):
        res = []
        for student in self.students:
            res.append(f"{student.name} - {student.id}")
        return res

    def getAllCourses(self):
        res = []
        for course in self.courses:
            res.append(f"{course.name} - {course.code}")
        return res

    def getCourseByCode(self, code: str):
        for course in self.courses:
            if course.code == code:
                return course
        print("Course not found")

    def getStudentById(self, id: str):
        for student in self.students:
            if student.id == id:
                return student
        print("Student not found")
    

def main():
    student1 = Student("John", "123")
    student2 = Student("Jane", "456")
    student3 = Student("Jack", "789")

    course1 = Course("Math", "MATH101", 2)
    course2 = Course("English", "ENG101", 2)
    course3 = Course("Science", "SCI101", 2)

    course_reg = CourseRegistration()
    course_reg.addStudent(student1)
    course_reg.addStudent(student2)
    course_reg.addStudent(student3)

    course_reg.addCourse(course1)
    course_reg.addCourse(course2)
    course_reg.addCourse(course3)

    course_reg.registerStudent(student1, course1)
    course_reg.registerStudent(student1, course2)
    course_reg.registerStudent(student2, course1)
    course_reg.registerStudent(student2, course2)
    course_reg.registerStudent(student3, course1)
    course_reg.registerStudent(student3, course2)

    print(course_reg.getStudentsForCourse(course1))
    print(course_reg.getStudentsForCourse(course2))
    print(course_reg.getStudentsForCourse(course3))
    
    print(course_reg.getCoursesForStudent(student1))
    print(course_reg.getCoursesForStudent(student2))
    print(course_reg.getCoursesForStudent(student3))

    print(course_reg.getAllStudents())
    print(course_reg.getAllCourses())

    print(course_reg.getCourseByCode("MATH101"))
    print(course_reg.getCourseByCode("ENG101"))
    print(course_reg.getCourseByCode("SCI101"))

    print(course_reg.getStudentById("123"))
    print(course_reg.getStudentById("456"))
    print(course_reg.getStudentById("789"))

    course_reg.unregisterStudent(student1, course1)
    course_reg.unregisterStudent(student1, course2)
    course_reg.unregisterStudent(student2, course1)
    course_reg.unregisterStudent(student2, course2)
    course_reg.unregisterStudent(student3, course1)
    course_reg.unregisterStudent(student3, course2)

    print(course_reg.getStudentsForCourse(course1))
    print(course_reg.getStudentsForCourse(course2))
    print(course_reg.getStudentsForCourse(course3))

    print(course_reg.getCoursesForStudent(student1))
    print(course_reg.getCoursesForStudent(student2))
    print(course_reg.getCoursesForStudent(student3))

    print(course_reg.getAllStudents())
    print(course_reg.getAllCourses())

main()
