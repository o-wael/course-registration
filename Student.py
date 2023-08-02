from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Course import Course


@dataclass
class Student:
    name: str
    id: str
    semester: int
    courses: set

    def __str__(self):
        return f"{self.name} - {self.id}"

    def __init__(self, name, id, semester):
        self.name = name
        self.id = id
        self.semester = semester
        self.courses = set()

    def __eq__(self, other: "Student"):
        return self.id == other.id

    def __hash__(self):
        return hash(self.id)

    def register_course(self, course: "Course"):
        self.courses.add(course)

    def unregister_course(self, course: "Course"):
        if course in self.courses:
            self.courses.remove(course)
        else:
            raise Exception("Course not registered")
