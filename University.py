from dataclasses import dataclass
from Student import Student
from Course import Course
from Semester import Semester
from CourseRegistration import CourseRegistration


@dataclass
class University:
    name: str = "GUC"
    courses: set = None
    students: set = None
    semesters: set = None
    __instance = None

    @staticmethod
    def getUniversity():
        if University.__instance is None:
            University.__instance = University()
        return University.__instance

    @staticmethod
    def reset():
        University.__instance = None
        University.courses = None
        University.students = None
        University.semesters = None

    def __init__(self):
        if University.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            University.__instance = self

    def __str__(self):
        return f"{self.name}"

    def add_course(self, course: Course, semester: Semester):
        if self.courses is None:
            self.courses = set()
        if semester not in self.semesters:
            raise Exception(f"Semester {semester.number} does not exist")
        semester.add_course(course)
        self.courses.add(course)

    def remove_course(self, course: Course):
        if course in self.courses:
            if len(course.students) != 0:
                raise Exception(f"Course {course.name} cannot be removed")
            for semester in self.semesters:
                if course in semester.courses:
                    semester.remove_course(course)
            self.courses.remove(course)
        else:
            raise Exception(f"Course {course.name} not registered")

    def add_student(self, student: Student):
        if self.students is None:
            self.students = set()
        self.students.add(student)

    def remove_student(self, student: Student):
        if student in self.students:
            if len(student.courses) != 0:
                for course in student.courses.copy():
                    self.unregistration(student, course)
            self.students.remove(student)
        else:
            raise Exception(f"Student {student.name} not registered")

    def add_semester(self, semester: Semester):
        if self.semesters is None:
            self.semesters = set()
        self.semesters.add(semester)

    def remove_semester(self, semester: Semester):
        flag = False
        if semester in self.semesters:
            if len(semester.courses) != 0:
                for course in semester.courses:
                    if course.students is not None:
                        if len(course.students) != 0:
                            flag = True
                            break
        else:
            raise Exception(f"Semester {semester.number} does not exist")

        if not flag:
            for course in semester.courses.copy():
                self.remove_course(course)
            self.semesters.remove(semester)
        else:
            raise Exception(f"Semester {semester.number} cannot be removed")

    @staticmethod
    def check_semester(student: Student, course: Course) -> bool:
        semesters = University.getUniversity().semesters
        for semester in semesters:
            if semester.number == student.semester:
                if course in semester.courses:
                    return True
        return False

    def registration(self, student: Student, course: Course):
        if University.check_semester(student, course):
            CourseRegistration.register_student_in_a_course(student, course)
        else:
            raise Exception(f"Student {student.name} cannot be registered")

    def unregistration(self, student: Student, course: Course):
        CourseRegistration.unregister_student_in_a_course(student, course)
