''' Coded By Matthew Thomas, designed to draw information from a databse on military fighter jets'''
#Imports
import sqlite3

#Constants and Variables
DATABASE = 'fighters.db'
user_input = None


#Functions
def print_all_aircraft():
    '''Function to print all aircraft in the database nicely'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    query = 'SELECT * FROM fighters;'
    cursor.execute(query)
    results = cursor.fetchall()
    #loop through all the results
    print("Name                                    Speed  Max G  Climb  Range  Payload")
    for fighter in results:
        print(f"{fighter[1]:<40}{fighter[2]:<7}{fighter[3]:<7}{fighter[4]:<7}{fighter[5]:<7}{fighter[6]:<7}")
    #loop complete
    db.close()
def print_all_aircraft_by_speed():
    
    '''Function to print all aircraft in the database by speed nicely'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    query = 'SELECT * FROM fighters ORDER BY speed DESC;'
    cursor.execute(query)
    results = cursor.fetchall()
    #loop through all the results
    print("Name                                    Speed  Max G  Climb  Range  Payload")
    for fighter in results:
        print(f"{fighter[1]:<40}{fighter[2]:<7}{fighter[3]:<7}{fighter[4]:<7}{fighter[5]:<7}{fighter[6]:<7}")
    #loop complete
    db.close()
def print_all_aircraft_by_max_g_then_speed():
    '''Function to print all aircraft in the database by maximum g-force then speed nicely'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    query = 'SELECT * FROM fighters ORDER BY max_g DESC, speed DESC;'
    cursor.execute(query)
    results = cursor.fetchall()
    #loop through all the results
    print("Name                                    Speed  Max G  Climb  Range  Payload")
    for fighter in results:
        print(f"{fighter[1]:<40}{fighter[2]:<7}{fighter[3]:<7}{fighter[4]:<7}{fighter[5]:<7}{fighter[6]:<7}")
    #loop complete
    db.close()
def print_all_aircraft_by_climb_rate():
    '''Function to print all aircraft in the database by maximum climbrate nicely'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    query = 'SELECT * FROM fighters ORDER BY climbrate DESC;'
    cursor.execute(query)
    results = cursor.fetchall()
    #loop through all the results
    print("Name                                    Speed  Max G  Climb  Range  Payload")
    for fighter in results:
        print(f"{fighter[1]:<40}{fighter[2]:<7}{fighter[3]:<7}{fighter[4]:<7}{fighter[5]:<7}{fighter[6]:<7}")
    #loop complete
    db.close()
def print_all_aircraft_by_range():
    '''Function to print all aircraft in the database by range nicely'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    query = 'SELECT * FROM fighters ORDER BY range DESC;'
    cursor.execute(query)
    results = cursor.fetchall()
    #loop through all the results
    print("Name                                    Speed  Max G  Climb  Range  Payload")
    for fighter in results:
        print(f"{fighter[1]:<40}{fighter[2]:<7}{fighter[3]:<7}{fighter[4]:<7}{fighter[5]:<7}{fighter[6]:<7}")
    #loop complete
    db.close()
def print_all_aircraft_by_payload():
    '''Function to print all aircraft in the database by payload nicely'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    query = 'SELECT * FROM fighters ORDER BY payload DESC;'
    cursor.execute(query)
    results = cursor.fetchall()
    #loop through all the results
    print("Name                                    Speed  Max G  Climb  Range  Payload")
    for fighter in results:
        print(f"{fighter[1]:<40}{fighter[2]:<7}{fighter[3]:<7}{fighter[4]:<7}{fighter[5]:<7}{fighter[6]:<7}")
    #loop complete
    db.close()


#main code
while True:
    print("\nWhat would you like to do.\n1. Print all aircraft\n2. Print all aircraft in descending speed order \n3. Print all aircraft by maximimum g-force, then speed \n4. Print all aircraft in descending climb rate order \n5. Print all aircraft in descending range order \n6. Print all aircraft in descending payload order \n7. Exit")
    user_input = input("")
    if user_input == "1":
        print_all_aircraft()
    elif user_input == "2":
        print_all_aircraft_by_speed()
    elif user_input == "3":
        print_all_aircraft_by_max_g_then_speed()
    elif user_input == "4":
        print_all_aircraft_by_climb_rate()
    elif user_input == "5":
        print_all_aircraft_by_range()
    elif user_input == "6":
        print_all_aircraft_by_payload()
    elif user_input == "7":
        break
    else:
        print("Invalid Input")



