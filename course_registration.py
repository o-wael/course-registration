from dataclasses import dataclass


@dataclass
class Course:
    name: str
    code: str
    max_students: int
    students: list = None

    def __str__(self):
        return f"{self.name} - {self.code}"

    def add_student(self, student):
        if self.students is None:
            self.students = []
        self.students.append(student)

    def remove_student(self, student):
        if self.students is None:
            self.students = []
        if student in self.students:
            self.students.remove(student)


@dataclass
class Student:
    name: str
    id: str
    courses: list = None

    def __str__(self):
        return f"{self.name} - {self.id}"

    def register_course(self, course: Course):
        if self.courses is None:
            self.courses = []
        self.courses.append(course)

    def unregister_course(self, course: Course):
        if self.courses is None:
            self.courses = []
        if course in self.courses:
            self.courses.remove(course)


@dataclass
class Course_Registration:
    courses: list = None
    students: list = None

    def add_course(self, course: Course):
        if self.courses is None:
            self.courses = []
        self.courses.append(course)

    def add_student(self, student: Student):
        if self.students is None:
            self.students = []
        self.students.append(student)

    def register_student(self, student: Student, course: Course):
        if course.students is None:
            course.students = []
        if course in self.courses and student in self.students:
            if course.max_students > len(course.students):
                course.add_student(student)
                student.register_course(course)
                return_string = f"Student {student.name} registered "
                return_string += f"for course {course.name} successfully"
                return return_string
            else:
                return f"Course {course.name} is full"
        else:
            return "Student or course not found"

    def unregister_student(self, student: Student, course: Course):
        if course in self.courses and student in self.students:
            if student in course.students:
                course.remove_student(student)
                student.unregister_course(course)
                return_string = f"Student {student.name} unregistered "
                return_string += f"for course {course.name} successfully"
                return return_string
            else:
                return_string = f"Student {student.name} not registered "
                return_string += f"for course {course.name}"
                return return_string
        else:
            return "Student or course not found"

    def get_students_for_course(self, course: Course):
        if course in self.courses:
            res = []
            if course.students is None:
                course.students = []
            for student in course.students:
                res.append(student.__str__())
            return res
        else:
            return "Course not found"

    def get_courses_for_student(self, student: Student):
        if student in self.students:
            res = []
            if student.courses is None:
                student.courses = []
            for course in student.courses:
                res.append(course.__str__())
            return res
        else:
            return "Student not found"

    def get_all_students(self):
        res = []
        for student in self.students:
            res.append(f"{student.name} - {student.id}")
        return res

    def get_all_courses(self):
        res = []
        for course in self.courses:
            res.append(f"{course.name} - {course.code}")
        return res

    def get_course_by_code(self, code: str):
        for course in self.courses:
            if course.code == code:
                return course
        return "Course not found"

    def get_student_by_id(self, id: str):
        for student in self.students:
            if student.id == id:
                return student
        return "Student not found"


def main() -> None:

    def difference(string1, string2):
        # Split both strings into list items
        string1 = string1.split()
        string2 = string2.split()

        A = set(string1)  # Store all string1 list items in set A
        B = set(string2)  # Store all string2 list items in set B

        str_diff = A.symmetric_difference(B)
        isEmpty = (len(str_diff) == 0)

        if isEmpty:
            print("Test Passed Successfully!")
        else:
            print("Test Failed!")
            print("The Difference is: ")
            print(str_diff)

    student1 = Student("John", "123")
    student2 = Student("Jane", "456")
    student3 = Student("Jack", "789")

    course1 = Course("Math", "MATH101", 2)
    course2 = Course("English", "ENG101", 2)
    course3 = Course("Science", "SCI101", 2)

    course_reg = Course_Registration()
    course_reg.add_student(student1)
    course_reg.add_student(student2)
    course_reg.add_student(student3)

    course_reg.add_course(course1)
    course_reg.add_course(course2)
    course_reg.add_course(course3)

    real = course_reg.register_student(student1, course1)
    real += "\n"+course_reg.register_student(student1, course2)
    real += "\n"+course_reg.register_student(student2, course1)
    real += "\n"+course_reg.register_student(student2, course2)
    real += "\n"+course_reg.register_student(student3, course1)
    real += "\n"+course_reg.register_student(student3, course2)

    real += "\n"
    for x in course_reg.get_students_for_course(course1):
        real += x+" | "
    if real[-3:] == " | ":
        real = real[:-3]

    real += "\n"
    for x in course_reg.get_students_for_course(course2):
        real += x+" | "
    if real[-3:] == " | ":
        real = real[:-3]

    real += "\n"
    for x in course_reg.get_students_for_course(course3):
        real += x+" | "
    if real[-3:] == " | ":
        real = real[:-3]

    real += "\n"
    for x in course_reg.get_courses_for_student(student1):
        real += x+" | "
    if real[-3:] == " | ":
        real = real[:-3]

    real += "\n"
    for x in course_reg.get_courses_for_student(student2):
        real += x+" | "
    if real[-3:] == " | ":
        real = real[:-3]

    real += "\n"
    for x in course_reg.get_courses_for_student(student3):
        real += x+" | "
    if real[-3:] == " | ":
        real = real[:-3]

    real += "\n"
    for x in course_reg.get_all_students():
        real += x+" | "
    if real[-3:] == " | ":
        real = real[:-3]

    real += "\n"
    for x in course_reg.get_all_courses():
        real += x+" | "
    if real[-3:] == " | ":
        real = real[:-3]

    real += "\n"+course_reg.get_course_by_code("MATH101").__str__()
    real += "\n"+course_reg.get_course_by_code("ENG101").__str__()
    real += "\n"+course_reg.get_course_by_code("SCI101").__str__()

    real += "\n"+course_reg.get_student_by_id("123").__str__()
    real += "\n"+course_reg.get_student_by_id("456").__str__()
    real += "\n"+course_reg.get_student_by_id("789").__str__()

    real += "\n"+course_reg.unregister_student(student1, course1)
    real += "\n"+course_reg.unregister_student(student1, course2)
    real += "\n"+course_reg.unregister_student(student2, course1)
    real += "\n"+course_reg.unregister_student(student2, course2)
    real += "\n"+course_reg.unregister_student(student3, course1)
    real += "\n"+course_reg.unregister_student(student3, course2)

    real += "\n"
    for x in course_reg.get_students_for_course(course1):
        real += x+" | "
    if real[-3:] == " | ":
        real = real[:-3]

    real += "\n"
    for x in course_reg.get_students_for_course(course2):
        real += x+" | "
    if real[-3:] == " | ":
        real = real[:-3]

    real += "\n"
    for x in course_reg.get_students_for_course(course3):
        real += x+" | "
    if real[-3:] == " | ":
        real = real[:-3]

    real += "\n"
    for x in course_reg.get_courses_for_student(student1):
        real += x+" | "
    if real[-3:] == " | ":
        real = real[:-3]

    real += "\n"
    for x in course_reg.get_courses_for_student(student2):
        real += x+" | "
    if real[-3:] == " | ":
        real = real[:-3]

    real += "\n"
    for x in course_reg.get_courses_for_student(student3):
        real += x+" | "
    if real[-3:] == " | ":
        real = real[:-3]

    real += "\n"
    for x in course_reg.get_all_students():
        real += x+" | "
    if real[-3:] == " | ":
        real = real[:-3]

    real += "\n"
    for x in course_reg.get_all_courses():
        real += x+" | "
    if real[-3:] == " | ":
        real = real[:-3]

    expected = "Student John registered for course Math successfully\n"
    expected += "Student John registered for course English successfully\n"
    expected += "Student Jane registered for course Math successfully\n"
    expected += "Student Jane registered for course English successfully\n"
    expected += "Course Math is full\n"
    expected += "Course English is full\n"
    expected += "John - 123 | Jane - 456\n"
    expected += "John - 123 | Jane - 456\n"
    expected += "\n"
    expected += "Math - MATH101 | English - ENG101\n"
    expected += "Math - MATH101 | English - ENG101\n"
    expected += "\n"
    expected += "John - 123 | Jane - 456 | Jack - 789\n"
    expected += "Math - MATH101 | English - ENG101 | Science - SCI101\n"
    expected += "Math - MATH101\n"
    expected += "English - ENG101\n"
    expected += "Science - SCI101\n"
    expected += "John - 123\n"
    expected += "Jane - 456\n"
    expected += "Jack - 789\n"
    expected += "Student John unregistered for course Math successfully\n"
    expected += "Student John unregistered for course English successfully\n"
    expected += "Student Jane unregistered for course Math successfully\n"
    expected += "Student Jane unregistered for course English successfully\n"
    expected += "Student Jack not registered for course Math\n"
    expected += "Student Jack not registered for course English\n"
    expected += "\n"
    expected += "\n"
    expected += "\n"
    expected += "\n"
    expected += "\n"
    expected += "\n"
    expected += "John - 123 | Jane - 456 | Jack - 789\n"
    expected += "Math - MATH101 | English - ENG101 | Science - SCI101\n"

    difference(real, expected)


main()
