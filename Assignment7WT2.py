#CSC 4110
#Assignment 7
#Created by Veronica Dean on 3/3/2022
#Work ticket 2

#Initialize lists

names = ['joe', 'tom', 'barb', 'sue', 'sally']
scores = [10, 23, 13, 18, 12]

# Using simple method to convert lists to dictionary

makeDictionary = {}
for key in names:
    for value in scores:
        makeDictionary[key] = value
        scores.remove(value)
        break

#print scoreDict
print("Resultant dictionary is : " + str(makeDictionary))

#Declare scoreDict
scoreDict = {}

#Assign scoreDict
scoreDict = dict(makeDictionary)

#Search for Barb using get method
name = '0'
while name != '1':
    name = input("Enter the name of the person's score you would like to see or 1 to exit: ")
    print(scoreDict.get(name))

