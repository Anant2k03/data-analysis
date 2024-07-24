import pickle

# Define a function to add student records to the binary file
def add_student_records(filename):
    with open(filename, 'wb') as file:
        while True:
            # Get student details from the user
            roll_no = input("Enter student roll number: ")
            name = input("Enter student name: ")
            marks = float(input("Enter student marks: "))

            # Create a dictionary to store student details
            student = {
                'roll_no': roll_no,
                'name': name,
                'marks': marks
            }

            # Write the student details to the binary file using pickle
            pickle.dump(student, file)

            # Ask the user if they want to add another record
            cont = input("Do you want to add another student record? (yes/no): ").strip().lower()
            if cont != 'yes':
                break

# Call the function to add student records to the binary file
add_student_records('stu.dat')
