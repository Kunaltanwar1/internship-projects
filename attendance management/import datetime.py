import datetime

class attendance_project_system:
    def __init__(self):
        self.u = {"kunal": "kunal"}
        self.students_records = {}
        self.students_attendance = {}

    def login(self):
        while True:
            print("Attendance Management System")
            v = input("Press * for login and press # for exit")
            if v == "*":
                username = input("Enter the username: ")
                pwd = input("Enter the password: ")
                if username in self.u and self.u[username] == pwd:
                    print("You are an authenticated user")
                    print("Successful login")
                    break
                else:
                    print("Invalid Credentials.")
            else:
                print("Exit")
                break

    def add_records(self, student_id, student_name):
        self.students_records[student_id] = student_name

    def mark_attendance(self, date, student_id, p):
        if date not in self.students_attendance:
            self.students_attendance[date] = {}
        self.students_attendance[date][student_id] = p

    def view_records(self, student_id):
        print("Attendance:", self.students_records.get(student_id, 'N/A'))
        for date, p in self.students_attendance.items():
            if student_id in p:
                print(date, "present")
            else:
                print(date, "Absent")

    def del_records(self, student_id):
        if student_id in self.students_records:
            del self.students_records[student_id]
            for date, attendance in self.students_attendance.items():
                if student_id in attendance:
                    del attendance[student_id]
            print("Successful deletion")
        else:
            print("Student ID not found")

    def update_records(self, student_id, student_name):
        print("What do you want to update: 1. Records 2. Attendance")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            print("What do you want to update: 1. Name 2. ID")
            up = int(input("1. Name & 2. ID: "))
            if up == 1:
                student_name = input("Enter the updated student name: ")
                self.students_records[student_id] = student_name
                print("Successfully updated name")
            elif up == 2:
                new_student_id = input("Enter the new student ID: ")
                if new_student_id != student_id:
                    if new_student_id in self.students_records:
                        print("Student ID already exists. Choose a different one.")
                    else:
                        self.students_records[new_student_id] = self.students_records[student_id]
                        del self.students_records[student_id]
                        for date, attendance in self.students_attendance.items():
                            if student_id in attendance:
                                attendance[new_student_id] = attendance.pop(student_id)
                        print("Successfully updated ID")
                else:
                    print("New ID is the same as the current ID.")
            else:
                print("Enter a valid choice")
        elif choice == 2:
            date = input("Enter the date (yyyy-mm-dd): ")
            p = input("Enter 'p' for present and 'a' for absent: ")
            if date in self.students_attendance and student_id in self.students_attendance[date]:
                self.students_attendance[date][student_id] = p
                print("Successfully updated attendance")
            else:
                print("Record not found for the given date and student ID")
        else:
            print("Enter a valid choice")

def main():
    attendance_project = attendance_project_system()
    attendance_project.login()

    counter = 0
    while True:
        counter += 1
        print("Choice: 1. Add records 2. Mark records 3. Update records 4. Delete records 5. View attendance 6. Exit")
        inp = int(input("Enter your choice: "))

        if inp == 1:
            student_id = input("Enter student ID: ")
            student_name = input("Enter student name: ")
            attendance_project.add_records(student_id, student_name)
            print("Successful Addition")
        elif inp == 2:
            date_str = input("Enter the date (yyyy-mm-dd) for attendance: ")
            date = datetime.datetime.strptime(date_str, '%Y-%m-%d').date()
            student_id = input("Enter the student ID: ")
            p = input("Enter 'p' for present and 'a' for absent: ")
            attendance_project.mark_attendance(date, student_id, p)
        elif inp == 3:
            student_id = input("Enter the student ID: ")
            student_name = input("Enter the updated student name: ")
            attendance_project.update_records(student_id, student_name)
        elif inp == 4:
            student_id = input("Enter the student ID: ")
            attendance_project.del_records(student_id)
        elif inp == 5:
            student_id = input("Enter the student ID: ")
            attendance_project.view_records(student_id)
        elif inp == 6:
            print("Exit")
            break
        else:
            print("Invalid choice. Enter a valid one.")

        if counter == 3:
            break

if __name__ == "__main__":
    main()
