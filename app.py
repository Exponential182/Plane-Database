''' Coded By Matthew Thomas, designed to draw information from a databse on military fighter jets'''
#Imports
import sqlite3

#Constants and Variables
DATABASE = 'fighters.db'


#Functions
def print_all_aircraft():
    '''Function to print all aircraft in the database nicely'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    query = 'SELECT * FROM fighters;'
    cursor.execute(query)
    results = cursor.fetchall()
    #loop through all the results
    for fighter in results:
        print(f"{fighter[1]:<40}{fighter[2]:<7}{fighter[3]:<7}{fighter[4]:<7}{fighter[5]:<7}{fighter[6]:<7}")
    #loop complete
    db.close()



#main
print_all_aircraft()




