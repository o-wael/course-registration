from Course import Course
from Student import Student


class Course_Registration:
    @staticmethod
    def register_student_in_a_course(student: Student, course: Course):
        student.register_course(course)
        course.add_student(student)

    @staticmethod
    def unregister_student_in_a_course(student: Student, course: Course):
        student.unregister_course(course)
        course.remove_student(student)
