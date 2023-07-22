from University import University
from Student import Student
from Course import Course
from Semester import Semester
from helpers import difference


def test_check_semester():

    University.reset()
    university = University.getUniversity()

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
    real += str(University.check_semester(student_ahmad, math4))+" | "
    real += str(University.check_semester(student_ibrahim, math4))+" | "
    real += str(University.check_semester(student_omar, acl))+" | "
    real += str(University.check_semester(student_ibrahim, acl))+" | "
    real += str(University.check_semester(student_ahmad, embedded))+" | "
    real += str(University.check_semester(student_omar, embedded))

    expected = "False | False | True | False | True | True"

    assert difference(real, expected)
