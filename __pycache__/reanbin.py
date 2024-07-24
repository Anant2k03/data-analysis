import pickle

def display_high_scorers(filename):
    try:
        with open(filename, 'rb') as file:
            while True:
                try:
                    # Read student record from the binary file
                    student = pickle.load(file)

                    # Check if the student's marks are greater than 81
                    if student['marks'] > 81:
                        # Display the student record
                        print(f"Roll No: {student['roll_no']}, Name: {student['name']}, Marks: {student['marks']}")
                except EOFError:
                    # End of file reached
                    break
    except FileNotFoundError:
        print(f"The file {filename} does not exist.")

display_high_scorers('stu.dat')
