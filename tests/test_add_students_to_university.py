from University import University
from Student import Student
from helpers import difference


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
        real += str(x)+" | "
    if real[-3:] == " | ":
        real = real[:-3]

    expected = "Ahmad - 52-4094 | Omar - 52-4245 | Ibrahim - 49-4095"

    assert difference(real, expected)
