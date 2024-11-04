studentsNames = ['Sandra' , 'Patricia', 'Phionah', 'Anitah']
studentsMarks = [80, 56, 78, 90]
#1.print Patricia, Faith , Phiona and Anitah.
#2.Add Masha to the 4th position.
#3.Update the name Phiona to  Phionah Aladinah
#4.Display the length of the student's lists
#5.Print all the students names using a for loop
#6.Calculate the total marks for the students marks variable and the answer= 304

#Answers
#1
studentsNames = ['Sandra','Patricia','Phionah','Anitah']
print(studentsNames)

#2
studentsNames.insert(3, 'Masha')
print(studentsNames)

#3
studentsNames[2]= ('Phiona Aladina')
print(studentsNames)

#4
length = len(studentsNames)
print(length)

#5
for names in studentsNames:  
  print(names)

#6
sum = (80 + 56 + 78 + 90)
print(f"The sum of the students marks is {sum}.")