from Course import Course
from Semester import Semester
import pytest  # type: ignore


def test_remove_course_from_semester():

    semester1 = Semester(1)
    course1 = Course("Python", "CSEN102", 1)

    semester1.add_course(course1)
    semester1.__str__()

    semester1.remove_course(course1)

    assert course1 not in semester1.courses

    with pytest.raises(Exception):
        semester1.remove_course(course1)
