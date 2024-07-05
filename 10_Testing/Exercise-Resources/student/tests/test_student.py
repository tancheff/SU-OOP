from project.student import Student
from unittest import TestCase

class TestStudent(TestCase):
    def setUp(self):
        self.student = Student("test_name", {"test_course": ["test_notes"]})

    def test_object_initializes(self):
        self.assertEqual(self.student.name, "test_name")
        self.assertEqual(self.student.courses, {"test_course": ["test_notes"]})

    def test_obejct_initializes_without_courses(self):
        student = Student("test_name_0")
        self.assertEqual(student.name, "test_name_0")
        self.assertEqual(student.courses, {})

    def test_enroll_existing_course(self):
        self.student.enroll("test_course", ["more_notes_1", "more_notes_2"])
        self.assertEqual(self.student.courses,
                         {"test_course": ["test_notes", "more_notes_1", "more_notes_2"]})

    def test_enroll_existing_course_return_message(self):
        self.assertEqual(self.student.enroll("test_course", ["more_notes_1", "more_notes_2"]),
                         "Course already added. Notes have been updated.")

    def test_enroll_in_new_course_add_course_notes_Y(self):
        self.assertEqual(self.student.enroll("new_course", "new_notes", "Y"),
                         "Course and course notes have been added.")
        self.assertEqual(self.student.courses["new_course"], "new_notes")

    def test_enroll_with_add_course_notes_empty_string(self):
        self.assertEqual(self.student.enroll("new_course", "new_notes", ""),
                         "Course and course notes have been added.")
        self.assertEqual(self.student.courses["new_course"], "new_notes")

    def test_enroll_in_new_course_without_add_course_notes(self):
        self.assertEqual("Course has been added.",
                         self.student.enroll("new_course", "new_notes", "test_course_notes"),
                         "Course has been added.")
        self.assertEqual(self.student.courses["new_course"], [])

    def test_add_notes_with_existing_course(self):
        self.student.add_notes("test_course", "more_notes")
        self.assertEqual(self.student.courses["test_course"],
                         ["test_notes", "more_notes"])

    def test_add_notes_with_existing_course_return_message(self):
        self.assertEqual(self.student.add_notes("test_course", "more_notes"),
                         "Notes have been updated")

    def test_add_note_non_existent_course(self):
        with self.assertRaises(Exception) as ex:
            self.student.add_notes("missing_course", "some_notes")

        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))

    def test_leave_existing_course(self):
        self.assertEqual(self.student.leave_course("test_course"),
                         "Course has been removed")

        self.assertEqual(len(self.student.courses), 0)

    def test_leave_non_existent_course(self):
        with self.assertRaises(Exception) as ex:
            self.student.leave_course("non_existent_course")

        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))


if __name__ == "__main__":
    main()