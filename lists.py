#LISTS
#Lists are array like structures, they start from 0 then 1...
varName = []
#Xtics of lists
#We can always edit our lists
#itmes in lists must be of the same type
#they work with index

studentNames = ["Deirdre", "Myra", "Faith", "Merlin"] #this list contains strings.
studentMarks = [ 90 , 95, 85, 75] #these are integers.
data = ['Sandra', 90, 'Kamwokya'] #mixed types

#Access the whole list
print(studentNames ,type(studentNames))

#Accessing list items
#positive indexing
print(studentNames[0]) #first item
print(studentNames[1]) #second item
print(studentNames[2]) #third item
print(studentNames[3]) #fourth item

#negative indexing
print(studentNames[-4])
print(studentNames[-3])
print(studentNames[-2])
print(studentNames[-1])


#Appending(adding) new items to the list
studentNames.append("Haulah")
print(studentNames)


#in a particular position
studentNames.insert(3,"Whitney")
print(studentNames)
