import time
start=time.time()

def Student_Marks():
        file = open("Ques.4&5(Marks).txt","r")
        marks=[]
        for i in file.readlines():
            x=i.rstrip("\n")
            y=x.split(" ")
            marks.append(y)
        return marks
    
def Grading(marks,ass_Detail):
    global final_tot_marks
    RECORDS=[]
    SUM=0
    temp=[]
    for i in marks:
        for j in range(1,len(i)):
            SUM+=round(int(eval((i[j])))*round(ass_Detail[j-1][1])/final_tot_marks[j-1])
        if 100>=SUM>=78:
            grade="A"
        elif 78>SUM>=63:
            grade="B"
        elif 63>SUM>=48:
            grade="C"
        elif 48>SUM>=38:
            grade="D"
        elif 38>SUM>=0:
            grade='F'
        for k in range(len(i)):
            temp.append(i[k])
        temp.append(SUM)
        temp.append(grade)
        RECORDS.append(temp)
        temp=[]
        SUM=0
    return RECORDS

def Course_Summary(name,Credits,list,Policy,data):
    print("-"*45)
    print("         Course Details")
    print("-"*45)
    print("Course Name: {}".format(name))
    print("Credit: {}".format(Credits))      
    print("List of assessment:")
    for i in range(len(list)):
        print("Assessment{}: {} {}".format(i+1,list[i][0],list[i][1])) 
    print("Policy: {}".format(Policy))
    grade_list={"A":0,"B":0,"C":0,"D":0,"F":0}
    for i in data:
        grade_list[i[len(i)-1]]=grade_list[i[len(i)-1]]+1
    print("Grades obtained:")
    for j in grade_list:
        print("{}:{}".format(j,grade_list[j]))
    print()

def display_Student_Record(data):
    file = open("Ques.5(Student_Record).txt","w+")
    for i in data:
        file.write("{}, {}, {}".format(i[0],str(i[len(i)-2]),i[len(i)-1]))
        file.write("\n")
    print("Check the student's grades in the file named Ques.5(Student_Record).txt.")
    file.close()
    
def Student_Search(data):
    roll_number = input("Enter the roll number to be searched: ")
    finded = False
    for i in data:
        if i[0]==roll_number:
            print("Roll NO: {}".format(roll_number))
            print("Total Marks Obtained: {}".format(i[len(i)-2]))
            print("Final Grade: {}".format(i[len(i)-1]))
            finded=True

    if not finded :
        print("\n         Entered Roll Number Does't Exists!!!!         \n")

name = input("Enter the name of the course: ")
Credits = input("Enter the credits of the course: ")
no=int(input("Enter the number of assessments during the course: "))
ass_Detail=[]
num=0
while num<no:
    print("Enter Detail of assessment {}".format(num+1))
    ass_name=input("Please Enter the name of the assessment:")
    ass_wt=int(input("Please Enter the weightage of assessment:"))
    ass_Detail.append((ass_name,ass_wt))
    num=num+1
Policy = [80,65,50,40]
final_tot_marks=list(map(int,input("Enter the total marks of each assessment[Enter spaced integers]:").split()))

Marks_Details = Student_Marks()
data=Grading(Marks_Details,ass_Detail)
print("-"*45)
print("Choose from the given below options:")
print("-"*45)
print("1-Generate Summary")
print("2-Print Grades of all students")
print("3-Search for the Student Record by Roll Number")
print("0-Exit")
print("-"*45)

for i in range(100):
    INPUT = int(input("Please Enter the Number(1,2,3) [0 for Exit] for Required Action: "))
    if INPUT==1:
       Course_Summary(name,Credits,ass_Detail,Policy,data)
    elif INPUT==2:
        display_Student_Record(data)
    elif INPUT==3:
        Student_Search(data)
    elif INPUT== 0:
        break
    else:
        print("Enter Valid Number!!!!")

end = time.time()
print("Time Taken (n=1000):")
print((end-start)*1000)