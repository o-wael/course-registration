import pytest  # type: ignore
from Course import Course
from CourseRegistration import Course_Registration
from helpers import difference
from Semester import Semester
from Student import Student
from University import University


class Test_Course:
    def test_course_should_be_created_should_pass(self):
        course = Course("Introduction to Programming", "CS101", 3)

        assert course is not None

    def test_course_should_be_created_with_name_should_pass(self):
        course = Course("Introduction to Programming", "CS101", 3)

        assert course.name == "Introduction to Programming"

    def test_course_should_be_created_with_code_should_pass(self):
        course = Course("Introduction to Programming", "CS101", 3)

        assert course.code == "CS101"

    def test_course_should_be_created_with_max_students_should_pass(self):
        course = Course("Introduction to Programming", "CS101", 3)

        assert course.max_students == 3

    def test_course_should_be_created_with_no_students_should_pass(self):
        course = Course("Introduction to Programming", "CS101", 3)

        assert len(course.students) == 0

    def test_course_should_be_printed_should_pass(self):
        course = Course("Introduction to Programming", "CS101", 3)

        assert str(course) == "CS101 - Introduction to Programming"


class Test_Student:
    def test_student_should_be_created_should_pass(self):
        student = Student("Omar", "52-4245", 7)

        assert student is not None

    def test_student_should_be_created_with_name_should_pass(self):
        student = Student("Omar", "52-4245", 7)

        assert student.name == "Omar"

    def test_student_should_be_created_with_id_should_pass(self):
        student = Student("Omar", "52-4245", 7)

        assert student.id == "52-4245"

    def test_student_should_be_created_with_semester_should_pass(self):
        student = Student("Omar", "52-4245", 7)

        assert student.semester == 7

    def test_student_should_be_created_with_no_courses_should_pass(self):
        student = Student("Omar", "52-4245", 7)

        assert len(student.courses) == 0

    def test_student_should_be_printed_should_pass(self):
        student = Student("Omar", "52-4245", 7)

        assert str(student) == "Omar - 52-4245"


class Test_Course_Registration:
    def test_student_should_register_in_course_should_pass(self):
        course = Course("Introduction to Programming", "CS101", 3)
        student = Student("Omar", "52-4245", 7)

        course_registration = Course_Registration()
        course_registration.register_student_in_a_course(student, course)

        assert len(course.students) == 1
        assert len(student.courses) == 1

    def test_student_should_register_in_course_only_once_should_pass(self):
        course = Course("Introduction to Programming", "CS101", 3)
        student = Student("Omar", "52-4245", 7)

        course_registration = Course_Registration()
        course_registration.register_student_in_a_course(student, course)
        course_registration.register_student_in_a_course(student, course)

        assert len(course.students) == 1
        assert len(student.courses) == 1

    def test_student_should_unregister_from_course_should_pass(self):
        course = Course("Introduction to Programming", "CS101", 3)
        student = Student("Omar", "52-4245", 7)

        course_registration = Course_Registration()
        course_registration.register_student_in_a_course(student, course)
        course_registration.unregister_student_in_a_course(student, course)

        assert len(course.students) == 0
        assert len(student.courses) == 0


class Test_Semester:
    def test_semester_should_be_created_should_pass(self):
        semester = Semester(7)

        assert semester is not None

    def test_semester_should_be_created_with_number_should_pass(self):
        semester = Semester(7)

        assert semester.number == 7

    def test_semester_should_be_created_with_no_courses_should_pass(self):
        semester = Semester(7)

        assert len(semester.courses) == 0

    def test_semester_should_be_printed_should_pass(self):
        semester = Semester(7)

        assert str(semester) == "7"


class Test_University:
    def test_university_be_created_should_pass(self):
        university = University()

        assert university is not None

    def test_university_be_singleton_should_pass(self):
        University.reset()
        university1 = University.get_university()
        university2 = University.get_university()

        assert university1 == university2

    def test_check_semester(self):
        University.reset()
        university = University.get_university()

        student_ahmad = Student("Ahmad", "52-4094", 7)
        student_omar = Student("Omar", "52-4245", 7)
        student_ibrahim = Student("Ibrahim", "49-4095", 9)

        university.add_student(student_ahmad)
        university.add_student(student_omar)
        university.add_student(student_ibrahim)

        semester4 = Semester(4)
        semester5 = Semester(5)
        semester6 = Semester(6)
        semester7 = Semester(7)

        university.add_semester(semester4)
        university.add_semester(semester5)
        university.add_semester(semester6)
        university.add_semester(semester7)

        math4 = Course("Math 4", "MATH401", 3)
        acl = Course("ACL", "CSEN702", 2)
        embedded = Course("Embedded", "CSEN703", 3)
        university.add_course(math4, semester4)
        university.add_course(acl, semester7)
        university.add_course(embedded, semester7)

        real = ""
        real += str(University.check_semester(student_ahmad, math4)) + " | "
        real += str(University.check_semester(student_ibrahim, math4)) + " | "
        real += str(University.check_semester(student_omar, acl)) + " | "
        real += str(University.check_semester(student_ibrahim, acl)) + " | "
        real += str(University.check_semester(student_ahmad, embedded)) + " | "
        real += str(University.check_semester(student_omar, embedded))

        expected = "False | False | True | False | True | True"

        assert difference(real, expected)

    def test_university_add_course_should_pass(self):
        University.reset()
        university = University.get_university()
        course = Course("Introduction to Programming", "CS101", 3)
        semester = Semester(7)

        university.add_semester(semester)
        university.add_course(course, semester)

        assert len(university.courses) == 1

    def test_university_remove_course_should_pass(self):
        University.reset()
        university = University.get_university()
        course = Course("Introduction to Programming", "CS101", 3)
        semester = Semester(7)

        university.add_semester(semester)
        university.add_course(course, semester)
        university.remove_course(course)

        assert len(university.courses) == 0

    def test_university_add_student_should_pass(self):
        University.reset()
        university = University.get_university()
        student_ahmad = Student("Ahmad", "52-4094", 7)
        university.add_student(student_ahmad)

        assert len(university.students) == 1

        student = Student("Omar", "52-4245", 7)
        student_ibrahim = Student("Ibrahim", "49-4095", 9)

        university.add_student(student)
        university.add_student(student_ibrahim)

        real = ""
        for x in university.students:
            real += str(x) + " | "
        if real[-3:] == " | ":
            real = real[:-3]

        expected = "Ahmad - 52-4094 | Omar - 52-4245 | Ibrahim - 49-4095"

        assert difference(real, expected)

    def test_university_remove_student_should_pass(self):
        University.reset()
        university = University.get_university()
        student = Student("Omar", "52-4245", 7)

        university.add_student(student)
        university.remove_student(student)

        assert len(university.students) == 0

    def test_university_add_semester_should_pass(self):
        University.reset()
        university = University.get_university()
        semester = Semester(7)

        university.add_semester(semester)

        assert len(university.semesters) == 1

    def test_university_remove_semester_should_pass(self):
        University.reset()
        university = University.get_university()
        semester = Semester(7)

        university.add_semester(semester)
        university.remove_semester(semester)

        assert len(university.semesters) == 0

    def test_university_register_student_in_course_should_pass(self):
        University.reset()
        university = University.get_university()
        course = Course("Introduction to Programming", "CS101", 3)
        student = Student("Omar", "52-4245", 7)
        semester = Semester(7)

        university.add_semester(semester)
        university.add_course(course, semester)
        university.add_student(student)
        university.registration(student, course)

        assert len(course.students) == 1
        assert len(student.courses) == 1

    def test_university_unregister_student_from_course_should_pass(self):
        University.reset()
        university = University.get_university()
        course = Course("Introduction to Programming", "CS101", 3)
        student = Student("Omar", "52-4245", 7)
        semester = Semester(7)

        university.add_semester(semester)
        university.add_course(course, semester)
        university.add_student(student)
        university.registration(student, course)
        university.unregistration(student, course)

        assert len(course.students) == 0
        assert len(student.courses) == 0

    def test_university_register_student_in_correct_course_should_pass(self):
        University.reset()
        university = University.get_university()
        semester = Semester(7)
        student = Student("Omar", "52-4245", 7)
        course = Course("Introduction to Programming", "CS101", 3)

        university.add_student(student)
        university.add_semester(semester)
        university.add_course(course, semester)
        university.registration(student, course)

        assert len(semester.courses) == 1
        assert len(student.courses) == 1

    def test_university_register_student_wrong_semester_should_raise(self):
        University.reset()
        university = University.get_university()
        semester = Semester(8)
        student = Student("Omar", "52-4245", 7)
        course = Course("Introduction to Programming", "CS101", 3)

        semester.add_course(course)

        university.add_student(student)
        university.add_semester(semester)
        university.add_course(course, semester)

        with pytest.raises(Exception):
            university.registration(student, course)

    def test_university_register_students_in_correct_courses_should_pass(self):
        University.reset()
        university = University.get_university()
        semester = Semester(7)
        student1 = Student("Omar", "52-4245", 7)
        student2 = Student("Ali", "52-4246", 7)
        course1 = Course("Introduction to Programming", "CS101", 3)
        course2 = Course("Introduction to Programming", "CS102", 3)

        university.add_student(student1)
        university.add_student(student2)
        university.add_semester(semester)
        university.add_course(course1, semester)
        university.add_course(course2, semester)
        university.registration(student1, course1)
        university.registration(student2, course2)

        assert len(semester.courses) == 2
        assert len(student1.courses) == 1
        assert len(student2.courses) == 1

    def test_register_extra_student_should_raise(self):
        University.reset()
        university = University.get_university()
        semester = Semester(7)
        student1 = Student("Omar", "52-4245", 7)
        student2 = Student("Ali", "52-4246", 7)
        course1 = Course("Introduction to Programming", "CS101", 1)

        university.add_student(student1)
        university.add_student(student2)
        university.add_semester(semester)
        university.add_course(course1, semester)
        university.registration(student1, course1)
        with pytest.raises(Exception):
            university.registration(student2, course1)

    def test_unregister_with_no_students_should_raise(self):
        University.reset()
        university = University.get_university()
        student = Student("Omar", "52-4245", 7)
        course = Course("Introduction to Programming", "CS101", 3)

        university.add_student(student)
        university.add_semester(Semester(7))
        university.add_course(course, Semester(7))

        with pytest.raises(Exception):
            university.unregistration(student, course)

    def test_unregister_student_from_wrong_course_should_raise(self):
        University.reset()
        university = University.get_university()
        semester = Semester(7)
        student = Student("Omar", "52-4245", 7)
        course1 = Course("Introduction to Programming", "CS101", 3)
        course2 = Course("Introduction to Programming", "CS102", 3)

        university.add_student(student)
        university.add_semester(semester)
        university.add_course(course1, semester)
        university.add_course(course2, semester)
        university.registration(student, course1)

        with pytest.raises(Exception):
            university.unregistration(student, course2)

    def test_unregister_student_should_pass(self):
        University.reset()
        university = University.get_university()
        semester = Semester(7)
        student = Student("Omar", "52-4245", 7)
        course = Course("Introduction to Programming", "CS101", 3)

        university.add_student(student)
        university.add_semester(semester)
        university.add_course(course, semester)
        university.registration(student, course)
        university.unregistration(student, course)

        assert len(semester.courses) == 1
        assert len(student.courses) == 0
