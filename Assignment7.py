#CSC 4110 903 Individual Assignment 7
#Written by Veronica Dean on 3/3/2022
#Work ticket 1


#Initialize lists

names = ['Joe', 'tom', 'barb', 'sue', 'sally']
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
