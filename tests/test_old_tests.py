import pytest  # type: ignore
from Course import Course
from helpers import difference
from Semester import Semester
from Student import Student
from University import University


def test_remove_with_no_students():
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

    math3 = Course("Math 3", "MATH301", 1)
    cs3 = Course("CS 3", "CSEN301", 1)
    math4 = Course("Math 4", "MATH401", 1)
    acl = Course("ACL", "CSEN702", 1)
    embedded = Course("Embedded", "CSEN703", 1)
    elective = Course("Elective", "CSEN904", 1)

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

    student_ahmad.register_course(acl)

    with pytest.raises(Exception):
        university.unregistration(student_ahmad, acl)


def test_remove_with_extra_students():
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

    math3 = Course("Math 3", "MATH301", 1)
    cs3 = Course("CS 3", "CSEN301", 1)
    math4 = Course("Math 4", "MATH401", 1)
    acl = Course("ACL", "CSEN702", 1)
    embedded = Course("Embedded", "CSEN703", 1)
    elective = Course("Elective", "CSEN904", 1)

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

    with pytest.raises(Exception):
        university.registration(student_ahmad, math3)

    university.registration(student_mohamed, cs3)
    university.registration(student_mohamed, math3)
    university.registration(student_ahmad, acl)
    university.registration(student_ahmad, embedded)

    with pytest.raises(Exception):
        university.registration(student_omar, acl)

    with pytest.raises(Exception):
        university.registration(student_omar, embedded)

    with pytest.raises(Exception):
        university.registration(student_ibrahim, acl)

    university.registration(student_ibrahim, elective)

    real = ""
    for x in acl.students:
        real += str(x) + " | "
    if real[-3:] == " | ":
        real = real[:-3]

    expected = "Ahmad - 52-4094"

    assert difference(real, expected)

    real = ""
    for x in embedded.students:
        real += str(x) + " | "
    if real[-3:] == " | ":
        real = real[:-3]

    expected = "Ahmad - 52-4094"

    assert difference(real, expected)

    real = ""
    for x in math3.students:
        real += str(x) + " | "
    if real[-3:] == " | ":
        real = real[:-3]

    expected = "Mohamed - 58-4096"

    assert difference(real, expected)

    real = ""
    for x in cs3.students:
        real += str(x) + " | "
    if real[-3:] == " | ":
        real = real[:-3]

    expected = "Mohamed - 58-4096"

    assert difference(real, expected)

    real = ""
    for x in math4.students:
        real += str(x) + " | "
    if real[-3:] == " | ":
        real = real[:-3]

    expected = ""

    assert difference(real, expected)

    real = ""
    for x in elective.students:
        real += str(x) + " | "
    if real[-3:] == " | ":
        real = real[:-3]

    expected = "Ibrahim - 49-4095"

    assert difference(real, expected)


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


def test_remove_course_from_semester():
    semester1 = Semester(1)
    course1 = Course("Python", "CSEN102", 1)

    semester1.add_course(course1)
    semester1.__str__()

    semester1.remove_course(course1)

    assert course1 not in semester1.courses

    with pytest.raises(Exception):
        semester1.remove_course(course1)


def test_course_unregister():
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

    university.add_course(math4, semester4)
    university.add_course(math3, semester3)
    university.add_course(cs3, semester3)
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
    university.registration(student_mohamed, cs3)
    university.registration(student_mohamed, math3)
    university.registration(student_ahmad, acl)
    university.registration(student_ahmad, embedded)
    university.registration(student_omar, acl)
    university.registration(student_omar, embedded)
    university.registration(student_ibrahim, elective)

    real = ""
    for x in acl.students:
        real += str(x) + " | "
    if real[-3:] == " | ":
        real = real[:-3]

    expected = "Ahmad - 52-4094 | Omar - 52-4245"

    assert difference(real, expected)

    university.unregistration(student_ahmad, acl)
    university.unregistration(student_omar, acl)
    university.unregistration(student_ibrahim, elective)

    with pytest.raises(Exception):
        university.unregistration(student_mohamed, acl)

    real = ""
    for x in acl.students:
        real += str(x) + " | "
    if real[-3:] == " | ":
        real = real[:-3]

    expected = ""

    assert difference(real, expected)

    real = ""
    for x in embedded.students:
        real += str(x) + " | "
    if real[-3:] == " | ":
        real = real[:-3]

    expected = "Ahmad - 52-4094 | Omar - 52-4245"

    assert difference(real, expected)

    university.unregistration(student_ahmad, embedded)

    real = ""
    for x in embedded.students:
        real += str(x) + " | "
    if real[-3:] == " | ":
        real = real[:-3]

    expected = "Omar - 52-4245"

    assert difference(real, expected)

    real = ""
    for x in elective.students:
        real += str(x) + " | "
    if real[-3:] == " | ":
        real = real[:-3]

    expected = ""

    assert difference(real, expected)


def test_course_registration():
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
    university.add_course(math4, semester4)
    university.add_course(cs3, semester3)
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

    with pytest.raises(Exception):
        university.registration(student_ahmad, math3)

    university.registration(student_mohamed, cs3)
    university.registration(student_mohamed, math3)
    university.registration(student_ahmad, acl)
    university.registration(student_ahmad, embedded)
    university.registration(student_omar, acl)
    university.registration(student_omar, embedded)

    with pytest.raises(Exception):
        university.registration(student_ibrahim, acl)

    university.registration(student_ibrahim, elective)

    real = ""
    for x in acl.students:
        real += str(x) + " | "
    if real[-3:] == " | ":
        real = real[:-3]

    expected = "Ahmad - 52-4094 | Omar - 52-4245"

    assert difference(real, expected)

    real = ""
    for x in embedded.students:
        real += str(x) + " | "
    if real[-3:] == " | ":
        real = real[:-3]

    expected = "Ahmad - 52-4094 | Omar - 52-4245"

    assert difference(real, expected)

    real = ""
    for x in math3.students:
        real += str(x) + " | "
    if real[-3:] == " | ":
        real = real[:-3]

    expected = "Mohamed - 58-4096"

    assert difference(real, expected)

    real = ""
    for x in cs3.students:
        real += str(x) + " | "
    if real[-3:] == " | ":
        real = real[:-3]

    expected = "Mohamed - 58-4096"

    assert difference(real, expected)

    real = ""
    for x in math4.students:
        real += str(x) + " | "
    if real[-3:] == " | ":
        real = real[:-3]

    expected = ""

    assert difference(real, expected)

    real = ""
    for x in elective.students:
        real += str(x) + " | "
    if real[-3:] == " | ":
        real = real[:-3]

    expected = "Ibrahim - 49-4095"

    assert difference(real, expected)


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
    real += str(University.check_semester(student_ahmad, math4)) + " | "
    real += str(University.check_semester(student_ibrahim, math4)) + " | "
    real += str(University.check_semester(student_omar, acl)) + " | "
    real += str(University.check_semester(student_ibrahim, acl)) + " | "
    real += str(University.check_semester(student_ahmad, embedded)) + " | "
    real += str(University.check_semester(student_omar, embedded))

    expected = "False | False | True | False | True | True"

    assert difference(real, expected)


def test_add_students_to_university():
    University.reset()
    university = University.getUniversity()

    student_ahmad = Student("Ahmad", "52-4094", 7)
    student_omar = Student("Omar", "52-4245", 7)
    student_ibrahim = Student("Ibrahim", "49-4095", 9)

    university.add_student(student_ahmad)
    university.add_student(student_omar)
    university.add_student(student_ibrahim)

    real = ""
    for x in university.students:
        real += str(x) + " | "
    if real[-3:] == " | ":
        real = real[:-3]

    expected = "Ahmad - 52-4094 | Omar - 52-4245 | Ibrahim - 49-4095"

    assert difference(real, expected)


def test_add_methods_in_university():
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

    semester11 = Semester(11)
    math11 = Course("Math 11", "MATH1101", 1)
    with pytest.raises(Exception):
        university.add_course(math11, semester11)

    university.remove_student(student_ibrahim)


def test_add_courses_to_semesters():
    University.reset()

    # uni = University.getUniversity()
    sem4 = Semester(4)
    sem5 = Semester(5)
    sem6 = Semester(6)

    # uni.add_semester(sem4)
    # uni.add_semester(sem5)
    # uni.add_semester(sem6)

    math4 = Course("Math 4", "MATH401", 3)
    cs4 = Course("Game", "CSEN402", 2)
    concepts = Course("Concepts", "CSEN403", 3)
    # uni.add_course(math4)
    # uni.add_course(cs4)
    # uni.add_course(concepts)
    sem4.add_course(math4)
    sem4.add_course(cs4)
    sem4.add_course(concepts)

    theory = Course("Theory", "CSEN502", 3)
    networks = Course("Networks", "CSEN503", 3)
    math5 = Course("Math 5", "MATH501", 3)
    sem5.add_course(theory)
    sem5.add_course(networks)
    sem5.add_course(math5)

    real = ""
    for x in sem4.courses:
        real += str(x) + " | "
    if real[-3:] == " | ":
        real = real[:-3]

    real += "\n"
    for x in sem5.courses:
        real += str(x) + " | "
    if real[-3:] == " | ":
        real = real[:-3]

    real += "\n"
    for x in sem6.courses:
        real += str(x) + " | "
    if real[-3:] == " | ":
        real = real[:-3]

    expected = "MATH401 - Math 4 | CSEN402 - Game | CSEN403 - Concepts\n"
    expected += "CSEN502 - Theory | CSEN503 - Networks | MATH501 - Math 5\n"

    assert difference(real, expected)
