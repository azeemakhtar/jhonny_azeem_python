from collections import UserList
from multiprocessing.connection import wait
import random, sys
from select import select
from unicodedata import name

students_List_One = [
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

while True: #main while loop. use loop for capturing the user input
    user_chose() 
    user_value = input().lower()
    if user_value == 'q':
        sys.exit() #close the program
    
    elif user_value == 'l': 
        for student in students_List_One: #print the list of available studetns
            print(f"{student['name']}", sep = '\n')
        print('')#line space for next user command of action

        while True: 
            student_grade() #get user input to show grades of students from the list                    
            user_input = input()
                            
            if user_input == 'g':
                for student in students_List_One:
                    print(f"{student['name']} - {student['grades']}" , sep='\n',)
                    
                student_grade()
                user_input = input()

            elif user_input == 'p':
                for student in students_List_One:
                    print(f"{student['name']} - {student['student_id']} - {student['email']}" , sep='\n',)        
                    
                student_grade()
                user_input = input()
            
            elif user_input == 'b':
                 user_chose()
            
            break
                 
    user_value = input()

    if user_value == 'a':
        print('Provide the name of a student to add from the registry: ID: xxxxx - name')
        
        add_student = input()
        students_List_One.append(add_student)
        for i in students_List_One:
            print(i)
            break
    if user_value == 'r':
        print('Remove a student from the registry' '\n')
        
        remove_student = input()
        students_List_One.remove(remove_student)       
        for i in students_List_One:
            print(i)
            break
        print(remove_student + ' is removed.')

    user_chose()
    False 