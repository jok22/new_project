import json
import database.database_handler as db
import ui.interface as ui 

def main():
    with open('config.json' , 'r') as f:
        config = json.load(f)
        path = config['path_to_db']

    student= db.StudentRepository(path)
    teacher= db.TeacherRepository(path)
    class_= db.ClassRepository(path)
    enrollment= db.EnrollmentRepository(path)
    ui.Interface(student, class_, teacher, enrollment).main_menu()
    
if __name__ == '__main__':
    main()
