"""
This module contains repositories for managing data related to a school database.
The repositories provide methods for inserting, deleting, and updating teacher, class,
and enrollment records in the database. Each repository is a subclass of the Database class,
which provides a context manager interface for managing the database connection.
Example usage:
    import database_handler
    teacher_repo = database_handler.TeacherRepository()
    teacher_repo.insert_teacher("Jonathas Santos")
"""


import sqlite3

class Database():
    """
    A context manager for managing connections to a SQLite database.
    Attributes:
    - path (str): The path to the SQLite database file.
    """
    def __init__(self, path):
        self.path = path

    def __enter__(self):
        self.conn = sqlite3.connect(self.path)
        return self.conn.cursor()

    def __exit__(self, exc_class, exc, traceback):
        self.conn.commit()
        self.conn.close()


class StudentRepository(Database):
    """
    A repository for managing students in a database.
    """
    def insert_student(self, name: str, gender: str, age: int) -> None:
        """
        Insert a new student record into the database.
        Args:
        - name (str): The name of the new student.
        - gender (str): The gender of the new student (should be 'M' or 'F').
        - age (int): The age of the new student.
        Returns:
        - None
        """
        with self as cursor:
            cursor.execute("INSERT INTO student (name, gender, age) VALUES (?, ?, ?)", (name, gender, age))

    def delete_student(self, student_id: int) -> None:
        """
        Delete a student record from the database.
        Args:
        - student_id (int): The ID of the student to delete.
        Returns:
        - None
        """
        with self as cursor:
            cursor.execute("DELETE FROM student WHERE student_id = ?", (student_id,))
            cursor.execute("DELETE FROM enrollments WHERE student_id = ?", (student_id,))

    def update_student(self, student_id: int, new_name: str) -> None:
        """
        Update the name of a student record in the database.
        Args:
        - student_id (int): The ID of the student to update.
        - new_name (str): The new name for the student.
        Returns:
        - None
        """
        with self as cursor:
            cursor.execute("UPDATE student SET name=? WHERE student_id=?", (new_name, student_id))

    def read_single_student(self, student_id: int) -> list:
        """
        Get a list of a single student and their ID from the database.

        Args:
        - student_id (int): The ID of the student to retrieve.

        Returns:
        - A list containing the student's ID, name, gender, and age.
        """
        with self as cursor:
            cursor.execute("SELECT student_id, name, gender, age FROM student WHERE student_id=?", (student_id,))
            return cursor.fetchone()
        
    def read_student(self) -> list:
        """
        Get a list of all students and their IDs from the database.

        Returns:
        - list: A list of (student_id, name, gender, age) tuples for all students in the database.
        """
        with self as cursor:
            cursor.execute("SELECT student_id, name, gender, age FROM student")
            return cursor.fetchall()


class TeacherRepository(Database):
    """
    A repository for managing teachers in a database.
    """
    def insert_teacher(self, name: str, gender: str, age: int) -> None:
        """
        Insert a new teacher record into the database.
        Args:
        - name (str): The name of the new teacher.
        - gender (str): The gender of the new teacher (should be 'M' or 'F').
        - age (int): The age of the new teacher.
        Returns:
        - None
        """
        with self as cursor:
            cursor.execute("INSERT INTO teacher (name, gender, age) VALUES (?, ?, ?)", (name, gender, age))

    def delete_teacher(self, teacher_id: int) -> None:
        """
        Delete a teacher record from the database.
        Args:
        - teacher_id (int): The ID of the teacher to delete.
        Returns:
        - None
        """
        with self as cursor:
            cursor.execute("DELETE FROM teacher WHERE teacher_id = ?", (teacher_id,))
            cursor.execute("DELETE FROM enrollments WHERE teacher_id =?", (teacher_id,))

    def update_teacher(self, teacher_id: int, new_name: str) -> None:
        """
        Update the name of a teacher record in the database.
        Args:
        - teacher_id (int): The ID of the teacher to update.
        - new_name (str): The new name of the teacher.
        Returns:
        - None
        """
        with self as cursor:
            cursor.execute("UPDATE teacher set name=? WHERE teacher_id = ?", (new_name, teacher_id))

    def read_single_teacher(self, teacher_id: int) -> list:
        """
        Get a list of a single teacher and their ID from the database.

        Args:
        - teacher_id (int): The ID of the teacher to retrieve.

        Returns:
        - A list containing the teacher's ID, name, gender, and age.
        """
        with self as cursor:
            cursor.execute("SELECT teacher_id, name, gender, age FROM teacher WHERE teacher_id=?", (teacher_id,))
            return cursor.fetchone()

    def read_teacher(self) -> list:
        """
        Get a list of all teachers and their IDs from the database.

        Returns:
        - list: A list of (teacher_id, name, gender, age) tuples for all teachers in the database.
        """
        with self as cursor:
            cursor.execute("SELECT teacher_id, name, gender, age FROM teacher")
            return cursor.fetchall()


class ClassRepository(Database):
    """
    A repository for managing classes in a database.
    """
    def insert_class(self, name: str, start_time: str, end_time: str) -> None:
        """
        Insert a new class record into the database.
        Args:
        - name (str): The name of the new class.
        - start_time (str): The start time of the new class.
        - end_time (str): The end time of the new class.
        Returns:
        - None
        """
        with self as cursor:
            cursor.execute("INSERT INTO class (class_name, start_time, end_time) VALUES (?, ?, ?)", (name, start_time, end_time))

    def delete_class(self, class_id: int) -> None:
        """
        Delete a class record from the database.
        Args:
        - class_id (int): The ID of the class to delete.
        Returns:
        - None
        """
        with self as cursor:
            cursor.execute("DELETE FROM enrollments WHERE class_id = ?", (class_id,))
            cursor.execute("DELETE FROM class WHERE class_id = ?", (class_id,))

    def update_class(self, class_id: int, new_class_name: str, new_start_time: str, new_end_time: str) -> None:
        """
        Update the name and time of a class record in the database.
        Args:
        - class_id (int): The ID of the class to update.
        - new_class_name (str): The new name of the class.
        - new_start_time (str): The new start time of the class.
        - new_end_time (str): The new end time of the class.
        Returns:
        - None
        """
        with self as cursor:
            cursor.execute("UPDATE class SET class_name = ?, start_time = ?, end_time = ? WHERE class_id = ?", (new_class_name, new_start_time, new_end_time, class_id))

    def read_single_class(self, class_id: int) -> list:
        """
        Get a single class and its information from the database.
        Args:
        - class_id (int): The ID of the class to retrieve.
        Returns:
        - tuple: A tuple containing the class information (class_id, class_name, start_time, end_time).
        """
        with self as cursor:
            cursor.execute("SELECT class_id, class_name, start_time, end_time FROM class WHERE class_id=?", (class_id,))
            return cursor.fetchone()

    def read_class(self) -> list:
        """
        Get a list of all classes and their IDs from the database.
        Returns:
        - list: A list of (class_id, class_name, start_time, end_time) tuples for all classes in the database.
        """
        with self as cursor:
            cursor.execute("SELECT class_id, class_name, start_time, end_time FROM class")
            return cursor.fetchall()


        
class EnrollmentRepository(Database):
    """
    A repository for managing enrollments in a database.
    """

    def insert_enrollment(self, class_id: int, student_id: int, teacher_id: int) -> None:
        """
        Insert a new enrollment record into the database.
        Args:
        - class_id (int): The ID of the class the student is enrolled in.
        - student_id (int): The ID of the student being enrolled.
        - teacher_id (int): The ID of the teacher who is responsible for the class.
        Returns:
        - None
        """
        with self as cursor:
            cursor.execute("INSERT INTO enrollments (class_id, student_id, teacher_id) VALUES (?, ?, ?)",
                           (class_id, student_id, teacher_id))

    def update_enrollment(self, new_class_id: int, new_student_id: int, new_teacher_id: int) -> None:
        """
        Update an existing enrollment record in the database.
        Args:
        - new_class_id (int): The ID of the class to update the enrollment to.
        - new_student_id (int): The ID of the student to update the enrollment to.
        - new_teacher_id (int): The ID of the teacher to update the enrollment to.
        Returns:
        - None
        """
        with self as cursor:
            cursor.execute("UPDATE enrollments SET class_id = ?, student_id = ?, teacher_id = ? WHERE enrollment_id = ?",
                            (new_class_id, new_student_id, new_teacher_id))

    def delete_enrollment(self, enrollment_id: int) -> None:
        """
        Delete an enrollment record from the database.
        Args:
        - enrollment_id (int): The ID of the enrollment to delete.
        Returns:
        - None
        """
        with self as cursor:
            cursor.execute("DELETE FROM enrollments WHERE enrollment_id =? ", (enrollment_id, ))
    def get_single_enrollments_info(self, enrollment_id: int) -> list:
        
        """Returns a list of dictionaries representing enrollment information with student, class, teacher, and class start and end times.
        Returns:
            list: A list of dictionaries, each representing an enrollment and containing the following keys:
                  - enrollment_id
                  - student_id
                  - student_name
                  - class_id
                  - class_name
                  - class_start_time
                  - class_end_time
                  - teacher_id
                  - teacher_name
        """
        with self as cursor:
            cursor.execute("""
                SELECT enrollments.enrollment_id, student.student_id, student.name, class.class_id, class.class_name, class.start_time, class.end_time, teacher.teacher_id, teacher.name
                FROM enrollments 
                JOIN student ON enrollments.student_id = student.student_id 
                JOIN class ON enrollments.class_id = class.class_id 
                JOIN teacher ON enrollments.teacher_id = teacher.teacher_id
                WHERE enrollments.enrollment_id = ?;
                """, (enrollment_id,))
            enrollments_info = cursor.fetchall()
            return enrollments_info

    def get_enrollments_info(self) -> list:
        """Returns a list of dictionaries representing enrollment information with student, class, teacher, and class start and end times.
        Returns:
            list: A list of dictionaries, each representing an enrollment and containing the following keys:
                  - enrollment_id
                  - student_id
                  - student_name
                  - class_id
                  - class_name
                  - class_start_time
                  - class_end_time
                  - teacher_id
                  - teacher_name
        """
        with self as cursor:
            cursor.execute("""
                SELECT enrollments.enrollment_id, student.student_id, student.name, class.class_id, class.class_name, class.start_time, class.end_time, teacher.teacher_id, teacher.name
                FROM enrollments 
                JOIN student ON enrollments.student_id = student.student_id 
                JOIN class ON enrollments.class_id = class.class_id 
                JOIN teacher ON enrollments.teacher_id = teacher.teacher_id;
            """)
            enrollments_info = cursor.fetchall()
            return enrollments_info
