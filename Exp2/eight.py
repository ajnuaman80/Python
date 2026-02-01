# too big question to write here :)

name = input("Enter your name: ")
sapid = input("Enter your SAP ID: ")
rollno = input("Enter your Rol No.: ")

pdm = float(input("Enter your PDS marks: "))
pym = float(input("Enter your Python marks: "))
chm = float(input("Enter your Chemistry marks: "))
egm = float(input("Enter your English marks: "))
phym = float(input("Enter your Physics marks: "))

percent = ((pdm + pym + chm + egm + phym)/500)*100
cgpa = percent / 10
grade = "x"   # declared grade to prevent the error if cgpa doesn't fall in any if-else condition

if(0 <= cgpa <= 3.4):          # didn't use range cuz range is used for integer values only
    grade = "F"
elif(3.5 <= cgpa <= 5):
    grade = "C+"
elif(5.1 <= cgpa <= 6):
    grade = "B"
elif(6.1 <= cgpa <= 7):
    grade = "B+"
elif(7.1 <= cgpa <= 8):
    grade = "A"
elif(8.1 <= cgpa <= 9):
    grade = "A+"
elif(9.1 <= cgpa <= 10):
    grade = "O"

print(
    "Name: ", name, 
    "\nRoll no.: ", rollno,
    "\nSAP ID: ", sapid,
    "\nSem: 1 Course: B.Tech. CSE AI&ML",
    "\nPDS: ", pdm,
    "\nPython: ", pym,
    "\nChemistry: ", chm,
    "\nEnglish: ", egm,
    "\nPhysics: ", phym,
    "\n\nPercentage: ", percent,
    "\nCGPA: ", cgpa,
    "\nGrade: ", grade
)


