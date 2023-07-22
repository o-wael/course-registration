from University import University
from Course import Course
from Semester import Semester
from Student import Student
import pytest  # type: ignore


def test_remove_methods_in_university():

    University.reset()
    university = University.getUniversity()

    semester3 = Semester(3)
    semester4 = Semester(4)
    semester5 = Semester(5)
    semester6 = Semester(6)
    semester7 = Semester(7)
    semester8 = Semester(8)
    semester9 = Semester(9)
    university.add_semester(semester3)
    university.add_semester(semester4)
    university.add_semester(semester5)
    university.add_semester(semester6)
    university.add_semester(semester7)
    university.add_semester(semester8)
    university.add_semester(semester9)

    math3 = Course("Math 3", "MATH301", 3)
    cs3 = Course("CS 3", "CSEN301", 3)
    math4 = Course("Math 4", "MATH401", 3)
    acl = Course("ACL", "CSEN702", 2)
    embedded = Course("Embedded", "CSEN703", 3)
    elective = Course("Elective", "CSEN904", 3)

    university.add_course(math3, semester3)
    university.add_course(cs3, semester3)
    university.add_course(math4, semester4)
    university.add_course(acl, semester7)
    university.add_course(embedded, semester7)
    university.add_course(elective, semester9)

    student_ahmad = Student("Ahmad", "52-4094", 7)
    student_omar = Student("Omar", "52-4245", 7)
    student_ibrahim = Student("Ibrahim", "49-4095", 9)
    student_mohamed = Student("Mohamed", "58-4096", 3)

    university.add_student(student_ahmad)
    university.add_student(student_omar)
    university.add_student(student_ibrahim)
    university.add_student(student_mohamed)

    university.registration(student_ahmad, acl)
    university.registration(student_omar, acl)
    university.registration(student_omar, embedded)

    math11 = Course("Math 11", "MATH1101", 1)
    with pytest.raises(Exception):
        university.remove_course(math11)  # remove unregisterd course
    with pytest.raises(Exception):
        university.remove_course(acl)  # remove course with students
    university.remove_course(elective)  # remove course without students

    semester11 = Semester(11)
    university.remove_semester(semester8)  # remove semester without courses
    with pytest.raises(Exception):
        university.remove_semester(semester11)  # remove unregisterd semester
    with pytest.raises(Exception):
        university.remove_semester(semester7)  # remove semester with NEcourses
    university.remove_semester(semester3)  # remove semester with Ecourses

    university.remove_student(student_ibrahim)
    university.remove_student(student_omar)  # remove student with courses
    student_ali = Student("Ali", "52-6565", 7)
    with pytest.raises(Exception):
        university.remove_student(student_ali)  # remove student not registered
