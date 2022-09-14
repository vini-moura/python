my_dictonary = {
    'bug': 'an error in a program that is not expected',
    'function': 'a piece of code that can be call over again',
    'loop': 'the action of doing something over&over again',
    123: 'just a sequence of numbers'
}
print(my_dictonary['bug'])
print(my_dictonary[123])

#change/create new entries
my_dictonary['if loop'] = 'A loop that occurs IF a condition is met'
my_dictonary['bug'] = 'an insect'
print(f'{my_dictonary}\n')

#create empty dictionaries
#empty_dictionary = {}
#my_dictonary = {}
#print(f'my_dictonary\n')

#loop through
for key in my_dictonary:
    print(key)
print('\n')
for key in my_dictonary:
    print(my_dictonary[key])
    
