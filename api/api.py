from flask import Flask, jsonify, request

class StudentEnrollmentAPI:
    def __init__(self, students):
        self.students = students
        self.app = Flask(__name__)

        @self.app.route('/student/<int:student_id>')
        def get_student_enrollments(student_id):
            password = request.args.get('password')
            for student in self.students:
                if student['id'] == student_id:
                    if password == student['password']:
                        return jsonify(student['enrollments'])
                    else:
                        return jsonify({"error": "Invalid password"})
            return jsonify({"error": "Student not found"})

    def run(self):
        self.app.run(debug=True)
