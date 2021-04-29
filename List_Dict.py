#list comprehension in python 

letters = ['a','b','c','d','e','f','g','h']
            
newletter = [letter for letter in letters]

print(newletter)

# Generator Comprehension

numbers = [1,2,3,4,5,6,7,8,9,10]

squareGen= (number**2 for number in numbers)
list(squareGen)

# Dictionary Comprehension

myDict = {"apple":1,"orange":4,"banana":10}
newDict = {key:myDict[key] for key in myDict.keys()}