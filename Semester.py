from dataclasses import dataclass
from Course import Course


@dataclass
class Semester:
    number: int
    courses: set

    def __str__(self):
        return f"{self.number}"

    def __init__(self, number):
        self.number = number
        self.courses = set()

    def __eq__(self, other: "Semester"):
        return self.number == other.number

    def __hash__(self):
        return hash(self.number)

    def add_course(self, course: Course):
        self.courses.add(course)

    def remove_course(self, course: Course):
        if course in self.courses:
            self.courses.remove(course)
        else:
            raise Exception(f"Course {course.name} not registered")
