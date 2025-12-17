# Project Prompt:

import student_data
CPSID= input("Enter CPS ID")
FName = input("Enter First name")
LName = input("Enter last name")
MName = input("Enter middle name")
HR =input("Enter homeroom")
GL = input("Enter Grade Level")
primary_email = input("Enter Primary Email")
secondary_email = input("Enter Secondary Email")
print("Program running. Press 'q' to exit at any time.")

# print(student_data.students)
def lookup_student():
      students = student_data.students
      search_name = input("Enter student's full name: ").strip().lower()


# You are hired to build a Student Lookup Tool for a school front office. The secretary must be able to:

    # Enter a student’s full name

for students in student:
        if students ["Combo,Name"].lower() == search_name:
                print(CPSID)
                print(HR)
                print(primary_email)
                print(FName, LName, MName)
                print(GL)





while True:


    if keyboard.is_pressed('q'): 
        print("Loop terminated by user.")
        break








    # Instantly see:

            # CPS ID
 
            # Homeroom

            # Grade Level

            # Primary Email



            # Students must:

            # Describe the search process

## be able to add new data
# Your program must allow the secretary to ADD a brand new student
student_name = []
item= input
student_name.append(item)

# into the system while the program is running.
  # if student_name.count(item)
# Your job is to let the secretary type in a new student just like filling out a registration form.
# Once the form is complete, your program must turn that information into a dictionary and add it to the main list of students.
# If the student already exists (same CPS ID), your program must block the entry to prevent duplicates.

# The program should:
    # 1. Ask the user for the following information:
    #    - CPS ID
    #    - First Name
    #    - Last Name
    #    - Middle Name
    #    - Homeroom
    #    - Grade Level
    #    - Primary Email
    #    - Secondary Email

# 2. Combine the First and Last name into this format:
    #    "Last, First"  
print("LName", "FName")

# 3. Store all of the new information into ONE dictionary
    #    that matches the structure of the existing student data.

# 4. Add (append) that new dictionary into the main students list.

# 5. After adding the student, the program must:
    #    - Print a confirmation message
    #    - Print the total number of students in the system
    #    - Print the newly added student record

# 6. The program must NOT delete or overwrite any existing students.

# 7. If the CPS ID already exists in the system:
        #    - Do NOT add the student
        #    - Display an error message saying the CPS ID is already taken
