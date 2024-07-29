import time
start=time.time()

class Course:
    def __init__ (self,name,credit,l,records,policy):
        self.name = name
        self.credit = credit
        self.l1 = l
        self.records = records
        self.policy=policy

    def Course_Summary(self):
        print(" ")
        print("-"*45)
        print("         Course Info")
        print("-"*45)
        print("Course Name: {}".format(self.name))
        print("Credit: {}".format(self.credit))      
        print("List of assessment:")
        for i in range(len(self.l1)):
            print("Assessment{}: {} {}".format(i+1,self.l1[i][0],self.l1[i][1])) 
        print("Policy: {}".format(self.policy))
        grading_list={"A":0,"B":0,"C":0,"D":0,"F":0}
        '''
        for i in self.records:
            grading_list[i[len(i)-1]]=grading_list[i[len(i)-1]]+1
        '''
        for i in rec1.keys():
            grading_list[rec1[i][0][1][0]]=grading_list[rec1[i][0][1][0]]+1

        print("Grades obtained:")
        for j in grading_list:
            print("{}:{}".format(j,grading_list[j]))
        print()
        print("-"*30)
        print("")

def cutoff(list):
    global policy
    l=[]
    for i in policy:
        req=[]
        for j in list:
            mq=[]
            for p in j[1:]:
                mq.append(float(p))
            if i-2<=sum(mq)<=i+2:
                req.append(sum(mq))
        req.sort()
        req1=[req[i+1]-req[i] for i in range(len(req)-1)]
        if req1==[]:
            l.append(i)
        else:
            m=req1.index(max(req1))+1
            l.append(req[m])
    return l


class Student:
    def __init__(self,records):
        self.records = records
    '''
    def display_Student_Record(self):
        file = open("student_records.txt","w+")
        for i in self.records:
            file.write("{}, {}, {}".format(i[0],str(i[len(i)-2]),i[len(i)-1]))
            file.write("\n")
        print("Please Check the student grades in file named student_records.txt in current directory.")
        file.close()
    '''
    def display_Student_Record(self):
        file = open("student_records.txt","w+")      
        for i in rec1.keys():
            js=i+" "+str(rec1[i][0][0][0])+" "+str(rec1[i][0][1][0])+"\n"
            file.write(js)
        print("Please Check the student grades in file named student_records.txt in current directory.")
        file.close()
    
    def search_Student(self):
        print("")
        rollno = input("Enter the roll number to be searched: ")
        found = False
        '''
        for i in self.records:
            if i[0]==rollno:
                print("Roll NO: {}".format(rollno))
                print("Total Marks Obtained: {}".format(i[len(i)-2]))
                print("Grade Obtained: {}".format(i[len(i)-1]))
                found=True
        '''
        for i in rec1.keys():
            if i ==rollno:
                print("Roll NO: {}".format(rollno))
                print("Total Marks Obtained: {}".format(rec1[i][0][0][0]))
                print("Grade Obtained: {}".format(rec1[i][0][1][0]))
                found=True
        if not found :
            print("\n*Roll Number Not Found***\n")



def get_Student_Marks():
        file = open("Ques.4&5(Marks).txt","r")
        marks=[]
        for i in file.readlines():
            b=i.rstrip("\n")
            a=b.split(" ")
            marks.append(a)
        return marks

rec1={}
def calculate_Grading(marks_detail,ass_detail):
    global Final_marks,policy
    RECORD=[]
    RECORD1=[]

    sum=0
    temp=[]
    temp1=[]
    temp2=[]
    g=[]
    for i in marks_detail:
        sum=0
        for j in range(1,len(i)):
            sum+=int(int(eval((i[j])))*int(ass_Detail[j-1][1])/Final_marks[j-1])
        if sum>=policy[0]:
            grade="A"
        elif sum>=policy[1]:
            grade="B"
        elif sum>=policy[2]:
            grade="C"
        elif sum>=policy[3]:
            grade="D"
        else:
            grade='F'
        for j in range(len(i)):
            g.append(i[j])
            temp.append(i[j])
        temp.append(sum)
        temp.append(grade)
        RECORD.append(temp)
        temp1.append(sum)
        temp2.append(grade)
        RECORD1.append([temp1.copy(),temp2.copy()])
        rec1[g[0]]=RECORD1.copy()
        RECORD1.clear()
        temp1.clear()
        temp2.clear()
        g.clear()
    return RECORD

name = input("Enter the name of course: ")
credit = input("Enter the credit of course: ")
no=int(input("Enter number of assessments during the course: "))
ass_Detail=[]
for i in range(no):
    print("Enter Detail of assessment {}".format(i+1))
    ass_name=input("Please Enter the name of the assement:")
    ass_wt=int(input("Please Enter the weightage of assessment:"))
    ass_Detail.append((ass_name,ass_wt))

policy = [80,65,40,40]
Final_marks=list(map(int,input("Enter total marks of each assessment:").split()))
marks_Detials = get_Student_Marks()
stu=Student(marks_Detials)
policy=cutoff(marks_Detials)

record=calculate_Grading(marks_Detials,ass_Detail)
c = Course(name,credit,ass_Detail,record,policy)

print("-"*45)
print("Choose an option:")
print("-"*45)
print("1-Generate Summary")
print("2-Print Grades of all students")
print("3-Search for Student Record by Roll No.")
print("-"*45)
print("")

while True:
    INPUT = int(input("Please Enter the Number(1,2,3)[O to break] for Required Action: "))
    if INPUT==1:
       c.Course_Summary()
    elif INPUT==2:
        stu.display_Student_Record()
    elif INPUT==3:
        stu.search_Student()
    elif INPUT==0:
        break
    else:
        print("Enter Valid Number!!!!")

end = time.time()
print((end-start)*1000)