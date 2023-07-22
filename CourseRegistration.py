from Student import Student
from Course import Course


class CourseRegistration:

    @staticmethod
    def register_student_in_a_course(student: Student, course: Course):
        if student.__class__.__name__ == "Student":
            if course.__class__.__name__ == "Course":
                student.register_course(course)
                course.add_student(student)

    @staticmethod
    def unregister_student_in_a_course(student: Student, course: Course):
        if student.__class__.__name__ == "Student":
            if course.__class__.__name__ == "Course":
                student.unregister_course(course)
                course.remove_student(student)


# def main() -> None:

#     student1 = Student("John", "123")
#     student2 = Student("Jane", "456")
#     student3 = Student("Jack", "789")

#     course1 = Course("Math", "MATH101", 2)
#     course2 = Course("English", "ENG101", 2)
#     course3 = Course("Science", "SCI101", 2)

#     course_reg = CourseRegistration()
#     course_reg.add_student(student1)
#     course_reg.add_student(student2)
#     course_reg.add_student(student3)

#     course_reg.add_course(course1)
#     course_reg.add_course(course2)
#     course_reg.add_course(course3)

#     real = course_reg.register_student(student1, course1)
#     real += "\n"+course_reg.register_student(student1, course2)
#     real += "\n"+course_reg.register_student(student2, course1)
#     real += "\n"+course_reg.register_student(student2, course2)
#     real += "\n"+course_reg.register_student(student3, course1)
#     real += "\n"+course_reg.register_student(student3, course2)

#     real += "\n"
#     for x in course_reg.get_students_for_course(course1):
#         real += x+" | "
#     if real[-3:] == " | ":
#         real = real[:-3]

#     real += "\n"
#     for x in course_reg.get_students_for_course(course2):
#         real += x+" | "
#     if real[-3:] == " | ":
#         real = real[:-3]

#     real += "\n"
#     for x in course_reg.get_students_for_course(course3):
#         real += x+" | "
#     if real[-3:] == " | ":
#         real = real[:-3]

#     real += "\n"
#     for x in course_reg.get_courses_for_student(student1):
#         real += x+" | "
#     if real[-3:] == " | ":
#         real = real[:-3]

#     real += "\n"
#     for x in course_reg.get_courses_for_student(student2):
#         real += x+" | "
#     if real[-3:] == " | ":
#         real = real[:-3]

#     real += "\n"
#     for x in course_reg.get_courses_for_student(student3):
#         real += x+" | "
#     if real[-3:] == " | ":
#         real = real[:-3]

#     real += "\n"
#     for x in course_reg.get_all_students():
#         real += x+" | "
#     if real[-3:] == " | ":
#         real = real[:-3]

#     real += "\n"
#     for x in course_reg.get_all_courses():
#         real += x+" | "
#     if real[-3:] == " | ":
#         real = real[:-3]

#     real += "\n"+course_reg.get_course_by_code("MATH101").__str__()
#     real += "\n"+course_reg.get_course_by_code("ENG101").__str__()
#     real += "\n"+course_reg.get_course_by_code("SCI101").__str__()

#     real += "\n"+course_reg.get_student_by_id("123").__str__()
#     real += "\n"+course_reg.get_student_by_id("456").__str__()
#     real += "\n"+course_reg.get_student_by_id("789").__str__()

#     real += "\n"+course_reg.unregister_student(student1, course1)
#     real += "\n"+course_reg.unregister_student(student1, course2)
#     real += "\n"+course_reg.unregister_student(student2, course1)
#     real += "\n"+course_reg.unregister_student(student2, course2)
#     real += "\n"+course_reg.unregister_student(student3, course1)
#     real += "\n"+course_reg.unregister_student(student3, course2)

#     real += "\n"
#     for x in course_reg.get_students_for_course(course1):
#         real += x+" | "
#     if real[-3:] == " | ":
#         real = real[:-3]

#     real += "\n"
#     for x in course_reg.get_students_for_course(course2):
#         real += x+" | "
#     if real[-3:] == " | ":
#         real = real[:-3]

#     real += "\n"
#     for x in course_reg.get_students_for_course(course3):
#         real += x+" | "
#     if real[-3:] == " | ":
#         real = real[:-3]

#     real += "\n"
#     for x in course_reg.get_courses_for_student(student1):
#         real += x+" | "
#     if real[-3:] == " | ":
#         real = real[:-3]

#     real += "\n"
#     for x in course_reg.get_courses_for_student(student2):
#         real += x+" | "
#     if real[-3:] == " | ":
#         real = real[:-3]

#     real += "\n"
#     for x in course_reg.get_courses_for_student(student3):
#         real += x+" | "
#     if real[-3:] == " | ":
#         real = real[:-3]

#     real += "\n"
#     for x in course_reg.get_all_students():
#         real += x+" | "
#     if real[-3:] == " | ":
#         real = real[:-3]

#     real += "\n"
#     for x in course_reg.get_all_courses():
#         real += x+" | "
#     if real[-3:] == " | ":
#         real = real[:-3]

#     expected = "Student John registered for course Math successfully\n"
#     expected += "Student John registered for course English successfully\n"
#     expected += "Student Jane registered for course Math successfully\n"
#     expected += "Student Jane registered for course English successfully\n"
#     expected += "Course Math is full\n"
#     expected += "Course English is full\n"
#     expected += "John - 123 | Jane - 456\n"
#     expected += "John - 123 | Jane - 456\n"
#     expected += "\n"
#     expected += "Math - MATH101 | English - ENG101\n"
#     expected += "Math - MATH101 | English - ENG101\n"
#     expected += "\n"
#     expected += "John - 123 | Jane - 456 | Jack - 789\n"
#     expected += "Math - MATH101 | English - ENG101 | Science - SCI101\n"
#     expected += "Math - MATH101\n"
#     expected += "English - ENG101\n"
#     expected += "Science - SCI101\n"
#     expected += "John - 123\n"
#     expected += "Jane - 456\n"
#     expected += "Jack - 789\n"
#     expected += "Student John unregistered for course Math successfully\n"
#     expected += "Student John unregistered for course English successfully\n"
#     expected += "Student Jane unregistered for course Math successfully\n"
#     expected += "Student Jane unregistered for course English successfully\n"
#     expected += "Student Jack not registered for course Math\n"
#     expected += "Student Jack not registered for course English\n"
#     expected += "\n"
#     expected += "\n"
#     expected += "\n"
#     expected += "\n"
#     expected += "\n"
#     expected += "\n"
#     expected += "John - 123 | Jane - 456 | Jack - 789\n"
#     expected += "Math - MATH101 | English - ENG101 | Science - SCI101\n"


# main()
