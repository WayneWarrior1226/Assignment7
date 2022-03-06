#CSC 4110
#Assignment 7
#Created by Veronica Dean on 3/3/2022
#Work ticket 3

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

#Print menu
name = '0'
while name != '4':
    menuoption = input(" Enter 1 to search for a name from the dictionary.\n Enter 2 to add a name and score to the dictionary.\n Enter 3 to read dictionary.\n Enter 4 to exit.\n")
    
#Search for name
    if menuoption == '1':
        name = input("Enter the name of the person's score you would like to see: ")
        print(scoreDict.get(name))
#Append
    if menuoption == '2':
        data = input('Enter name & score separated by ":" ')
        temp = data.split(':')
        scoreDict[temp[0]] = int(temp[1])
          
#Display the new dictionary
    if menuoption == '3':
        for key, value in scoreDict.items():
            print('Name: {}, Score: {}'.format(key, value))
        
        

