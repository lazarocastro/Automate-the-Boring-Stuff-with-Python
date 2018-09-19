#This program says hello and asks for name.

print('Hello world!')
print('What is your name?') #asks for their name
myName = input()
print('It is good to meed you, ' + myName)
print('The lenght od your name is: ')
print(len(myName))
print('What is your age?') # ask for their age
myAge = input()
print('You will be ' + str(int(myAge) + 1) + ' in a year.')
