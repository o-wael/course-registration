from University import University
from Semester import Semester
from Course import Course
from helpers import difference


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
        real += str(x)+" | "
    if real[-3:] == " | ":
        real = real[:-3]

    real += "\n"
    for x in sem5.courses:
        real += str(x)+" | "
    if real[-3:] == " | ":
        real = real[:-3]

    real += "\n"
    for x in sem6.courses:
        real += str(x)+" | "
    if real[-3:] == " | ":
        real = real[:-3]

    expected = "MATH401 - Math 4 | CSEN402 - Game | CSEN403 - Concepts\n"
    expected += "CSEN502 - Theory | CSEN503 - Networks | MATH501 - Math 5\n"

    assert difference(real, expected)
