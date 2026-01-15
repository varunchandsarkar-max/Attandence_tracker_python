student = {}


n = int(input("Enter total no of students:"))

for i in range(n):
    name =(input("Enter student's name:"))
    subjects = int(input("enter total no of subjects:"))
    
    total_classes = 0
    attended_classes = 0

    for j in range(subjects):
        subject = input("Enter sub name:")
        total = int(input("Total classes:"))
        attended = int(input("classes attanded:"))
    
        total_classes += total
        attended_classes += attended
    
        percentage = (attended_classes/total_classes)*100
        student[name] = percentage

print("----Student Report----!!")
for name , percent in student.items():
    print(name,":", round(percent, 2), "%")
    
print("----Students not elegible for exam(<75%)----!!")
for name , percent in student.items():
    if percent < 75:
        print(name,":",round(percent,2),"%","Not eligible for exams.!!")
        
    
    
    

    