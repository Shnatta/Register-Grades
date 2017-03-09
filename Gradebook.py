#Gradebook Project *Display a persons grades/where can he/she get a job!*
#Thanks to Subzidion(Twitch), LoveFeelings(Twitch), MichaelC212(Twitch)#
import time
from prettytable import PrettyTable

x = PrettyTable()
c = PrettyTable()

def Wait(x): # Wait x amount of time before next line is executed!
	time.sleep(x)

class Student():    # Class Student
    def __init__(self, Fullname, age, born, classes, grades): #Arguments
            self.Fullname = Fullname # Define
            self.age = age
            self.born = born
            self.classes = classes
            self.grades = grades
    def stats(self):
            return 'Fulll Name : {}, Age : {}, Born : {}, Grades : {}'.format(self.Fullname, self.age, self.born, self.grades)
    def name():
            return '{}'.format(Fullname)
    def age():
            return '{}'.format(age)
    def born():
            return '{}'.format(born)
    def grades():
            return '{}'.format(grades)
                        

def name():
        global name_
        name_ = input('Full name: ')
        if (len(name_) > 1):
            Wait(1)
        elif (int(name_) ):
            print("Error, only letters! (Try again)") #\n creates a new line!
            Wait(1.5)
            name()
def age():
    global age_
    age_ = input("Age: ")
    if (age_.isdigit() ):
        Wait(1.5)
    else:
        print("Error, please enter a valid number!")
        age()
def born():
    global born_
    born_ = input("Birthday(dd.mm.yy): ")
    if (born_):
        Wait(1.5)
    else:
        Wait(1.5)
        print("Error, please enter a valid birthday!")
        born()
def classes():
    global s_classes
    s_classes = [] # Empty index! Add item/word to the index (index name goes here).append(obj)
    add = input("Enter classes: ")
    if (add):
        s_classes.extend(add.split() ) #x.split() splits up a sentence(for index() ) / x.append(what you want to add)
        return (', '.join(s_classes) )
        print(s_classes)
        Wait(1.5)
    else:
        Wait(1.5)
        print("Error, something went wrong!")
        classes()
def Getgrades():
    global grades
    grades = []
    for cl in s_classes:
        while True:
            try:
                a = int(input("What did you get in {} ".format(cl)))
                print("Registered for {}.".format(cl))
                grades.append('{}: {}'.format(cl, a))
                break
            except ValueError:
                print("Please give a valid integer")

#mylist = ['spam', 'ham', 'eggs']
#print(mylist)
#print (', '.join(mylist) )

name()
age()
born()
classes()
Getgrades()


Student_1 = Student(name_, age_, born_, s_classes, grades)
test = (', \n'.join(grades) )
x.field_names = ["Name", "Born", "Age", "Grades"]
x.add_row([name_, born_ , age_, test])
print(x)
Wait(200)
