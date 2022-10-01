from collections import UserList
from multiprocessing.connection import wait
import random
import sys
from select import select
from unicodedata import name

students_list_one = [
    {"name": "Tobias Fors", "email": "tobias.fors@yh.nackademin.se", "age": 30,  "student_id": 11230, "grades": 
    {"Pythonprogrammering 1": 1, "Databasteknik": 4}},
    {"name": "Karin Börjell", "email": "karin.borjell@yh.nackademin.se", "age": 32,  "student_id": 11231, "grades": 
    {"Pythonprogrammering 1": 1, "Pythonprogrammering 2": 3}},
    {"name": "Daniel Eliasson", "age": 29,  "email": "daniel.eliasson@yh.nackademin.se", "student_id": 11233, "grades": 
    {"Pythonprogrammering 1": 1, "Affärsmannaskap": 2}},
    {"name": "Magdalena Andersson", "age": 50,  "email": "magdalena.andersson@yh.nackademin.se", "student_id": 11234, "grades": 
    {"Pythonprogrammering 1": 1, "Webbramverk inom python": 5}},
]#this is the list of available students

print('Welcome to the greatest student system in the world.' '\n')
print('What would you like to do?')

def user_chose(): #put all the user inputs in a function
    print('[q] - Exit')
    print('[l] - List all students from the registry')
    print('[a] - Add a student from the registry')
    print('[r] - Remove a student from the registry')

def student_grade():
    print('[b] - Go Back')
    print('[g] - Show summary of grades')
    print('[p] - Personal information')
    

def student_detail(choice):
    if choice == "0":    
        student_grades()
    
def student_grades(choice):
    pass
    

while True: #main while loop. use loop for capturing the user input
    user_chose() 
    user_value = input().lower()
    if user_value == 'q':
        sys.exit() #close the program
    
    elif user_value == 'l': 
        for count, student in enumerate(students_list_one): #print the list of available studetns
            print(f"{count} : {student['name']}", sep = '\n')
        print('')#line space for next user command of action

        while True: 
            student_grade() #get user input to show grades of students from the list                    
            user_input = input()
            
            # make into a function
            def get_grades():
                print("Chose from student")
                user_input = input(str()).lower()
            

            # printing information
            if user_input == 'g':
                get_grades()
                for student in students_list_one:
                    print(f"{student['name']} - {student['grades']}" , sep='\n',)
            
            # make into a function
            # printing information  
            elif user_input == 'p':
                for student in students_list_one:
                    print(
                f"{student['name']} - {student['email']} - {student['age']} - {student['student_id']} - {student['email']}" , sep='\n',)        
                
            elif user_input == 'b':
                break
                 
    elif user_value == 'a':
        # Make this into a function
        
        stu = dict() # call dictionary to add new values

        print('Provide the name of a student to add from the registry - name. \n')
        
        add_name = input()
        stu["name"] = add_name #put new name against name index in student dict and similarly ID, email, age below
        
        print('Provide the student ID: 112XX')
        add_id = int(input())
        stu["student_id"] = add_id
        
        print('Provide the email of student')
        add_email = input()
        stu["email"] = add_email

        print('Provide the age of the student')
        add_age = int(input())
        stu["age"] = add_age

        print('Provide the number of courses the student is enrolled (number only)')
        i = "" # get the value i/number of courses that are to be added for a student 
        course_enrolled = dict()
        while(type(i) is not int): #catch if the user proveded value in not int and convert to int
            i = int(input())
        for i in range(0, i): #run the loop untill user added the number of courses to be added

            print('Enter the course name')
            course_name = input()

            print('Enter the grades for this course')
            course_grade = int(input())

            course_enrolled[course_name] = course_grade #put the valuse of new courses added into course_enrolled and provide a grade 

        stu["grades"] = course_enrolled 
        students_list_one.append(stu)
        for i in students_list_one:
            print(i)
            break

    elif user_value == 'r':
        print('Enter the student Id to be removed from the registry' '\n')
        
        remove_student = input()
        update_list = [i for i, _ in enumerate(students_list_one) if _[
            'student_id'] == int(remove_student)] #using temp variable to store the ID of the list value to enumerate from the list to remove that item later
        try:
            students_list_one.pop(update_list[0]) #remove the list item for the user specified index
            
            print(remove_student + ' is removed.')
        except IndexError:
            print('Something is not correct')