from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Student import Student


@dataclass
class Course:
    name: str
    code: str
    max_students: int
    students: set

    def __str__(self):
        return f"{self.code} - {self.name}"

    def __init__(self, name, code, max_students):
        self.name = name
        self.code = code
        self.max_students = max_students
        self.students = set()

    def __eq__(self, other: "Course"):
        return self.code == other.code

    def __hash__(self):
        return hash(self.code)

    def add_student(self, student: "Student"):
        if len(self.students) == self.max_students:
            raise Exception("Course is full")
        self.students.add(student)

    def remove_student(self, student: "Student"):
        if len(self.students) == 0:
            raise Exception("Course is empty")
        if student in self.students:
            self.students.remove(student)
        else:
            raise Exception("Student not registered in this course")
