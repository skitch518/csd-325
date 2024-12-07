import json
from os import path

filename = 'student.json'

# Check if the file exists and open it
def open_json_file(filename):
    if not path.isfile(filename):
        raise Exception("File not found")

    with open(filename, 'r') as fp:
        student_list = json.load(fp)

    return student_list

# Print function
def print_student(student_list):
    for student in student_list:
        first_name = student.get('F_Name', 'N/A')
        last_name = student.get('L_Name', 'N/A')
        student_id = student.get('Student_ID', 'N/A')
        email = student.get('Email', 'N/A')
        print(f"{first_name} , {last_name} : ID = {student_id} , Email = {email}")

# Function to add a student
def add_student(student_list):
    new_student = {
        "F_Name": "Jason",
        "L_Name": "Schriner",
        "Student_ID": "36947",
        "Email": "jaschriner@my365.bellevue.edu"
    }
    student_list.append(new_student)

# Save updated information to the file
def write_json_file(filename, student_list):
    if not path.isfile(filename):
        raise Exception("File not found")

    with open(filename, 'w') as fp:
        json.dump(student_list, fp, indent=4)

# Main function
def main(filename):
    # Directly use the open_json_file function when passing to other functions
    student_list = open_json_file(filename)

    # Print the original student list
    print("\n--- Original Student List ---")
    print_student(student_list)

    # Add a student to the list   
    add_student(student_list)

    # Print the updated student list
    print("\n--- Updated Student List ---")
    print_student(student_list)

    # Save the updated information to the file
    write_json_file(filename, student_list)

    # Notify user that the file was updated
    print("\nThe student list has been successfully updated in the file.")

# Run the main function
main(filename)

