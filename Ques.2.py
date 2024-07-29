def Read_Data():
    record = open("Ques.2(Record).txt","r")
    Record_Lines = record.read().splitlines()
    Record_List = []
    Record_Dict = {}
    for i in Record_Lines:
        word_list = i.split(", ")
        Record_List.append(word_list)
    for j in Record_List:
        if j[0] not in Record_Dict:
            Data=[]
            for k in Record_List:
                if k[0]==j[0]:
                    Data.append([k[1],k[2],k[3]])
            Record_Dict[j[0]]=Data
    return Record_Dict,Record_List

def Student_Entry_Exit_Record(Record_Dict):
    student_name=input("Enter the name of the student: ")
    if student_name in Record_Dict: 
        file = open("Ques.2(TA_Entry_Exit_Record).txt","w")
        length=len(Record_Dict[student_name])
        print(Record_Dict[student_name][length-1][0])
        if Record_Dict[student_name][length-1][0]=="ENTER":
            print("{} is in Campus currently.".format(student_name))
        elif Record_Dict[student_name][length-1][0]=="EXIT":
            print("{} is not in Campus currently.".format(student_name))

        file.write("{}'s Entry/Exit Record".format(student_name))
        file.write("\n")
                  
        for i in Record_Dict[student_name]:
            file.write(str(tuple(i)))
            file.write("\n")
        file.close()
    else:
        print("Name doesn't exist.")

def entry_Exit_status(Record_List):
    start=input("Please Enter the starting time: ")
    end=input("Please Enter the end time: ")
    file = open("Ques.2(TA_Entry_Exit_Status).txt","w")
    file.write("Students that entered the campus from {} to {} : \n".format(start,end))

    for i in Record_List:
        if i[3]>=start and i[3]<=end:
            if i[1] == "ENTER":
                temp_Str = "{}, {}, {}".format(i[0],i[1],i[3])
                file.write(temp_Str)
                file.write("\n")
            else:
                temp_Str = "{}, {}, {}".format(i[0],i[1],i[3])
                file.write(temp_Str)
                file.write("\n")
    file.close()

def Count_Entry_Exit(Record_List):
    Gate=input("Enter the Gate number: ")
    Count_Enter,Count_Exit=0,0
    for i in Record_List:
        if i[2] == Gate:
            if i[1] == "ENTER":
                Count_Enter+=1
            elif i[1] == "EXIT":
                Count_Exit+=1
    print("Total Number of entries from gate no. {} is {}".format(Gate,Count_Enter))
    print("Total Number of exits from gate no. {} is {}".format(Gate,Count_Exit))


Record_Dict,Record_List = Read_Data()
print("Choose the required option(1/2/3):")
print("-"*20)
print("1-Get Record of Students Moving in/out of Campus")
print("2-Get Entry or Exit in Given time Slot")
print("3-Get Number of Times Students Have Entered and Exited From Given Gate")
print("-"*20)
print("                     ")
while True:
    number = int(input("Please Enter the Number (1/2/3) for Required Action: "))
    if number==1:
        Student_Entry_Exit_Record(Record_Dict)
        print("             ")
    elif number==2:
        entry_Exit_status(Record_List)
        print("             ")
    elif number==3:
        Count_Entry_Exit(Record_List)
        print("             ")
    else:
        print("Enter A Valid Number!!!")

"Ques.2(Record).txt".close()