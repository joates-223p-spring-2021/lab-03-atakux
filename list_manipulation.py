# -*- coding: utf-8 -*-
"""
angela deleo
CPSC 223P-01
Tue Jan 08, 2022
atakux707@csu.fullerton.edu
"""

#the lists
fruits = ["grape", "mango", "nectarine", "pineapple", "banana", 
          "apple", "orange", "pear", "strawberry", "avocado"]

vegetables = ["zucchini", "asparagus", "kale", "spinach", "broccoli",
              "celery", "beets", "bok choy", "brussels sprouts", "arugula"]



#combine the fruits and vegetables
combinedList = fruits + vegetables
length = len(combinedList)

print("There are", length, "elements in the combined list")



#sorted
sortedList = sorted(combinedList)



#prints the sorted list on separate lines
for produce in sortedList:
    print(produce)


#make new list
reversedList = []

#reverse the sorted list by using a swapping method
for produce in range(len(sortedList) - 1, -1, -1):
    #append the list
    reversedList.append(sortedList[produce])

#print reversed list
print(reversedList)
