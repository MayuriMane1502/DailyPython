#Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
singlestr = 'Thirty ' + 'Days ' + 'Of ' + 'Python '
print(singlestr)

print('------------------------------------------------')
#Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
string1 = 'Coding'
string2 = 'For'
string3 = 'All'

result_string = string1 + ' ' + string2 + ' ' + string3
print(result_string)
print('--------------------------------------------------')

#Declare a variable named company and assign it to an initial value "Coding For All".
company = "Coding For All"

#Print the variable company using print().
print(company)
#Print the length of the company string using len() method and print().
print(len(company))

#Change all the characters to uppercase letters using upper() method.
print(company.upper())

#Change all the characters to lowercase letters using lower() method.
print(company.lower())

#Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
print(company.capitalize())
print(company.title())
print(company.swapcase())

#Cut(slice) out the first word of Coding For All string.
original_string = "Coding For All"
cut_out_first_word = original_string[len("Coding")+1:] ## Using string slicing to cut out the first word
#original_string[len("Coding")+1:] slices the original string starting from the index after the space following "Coding," effectively cutting out the first word.
print(cut_out_first_word)

#Check if Coding For All string contains a word Coding using the method index, find or other methods.
string = 'Coding For All'
sub_string = 'Coding'
sub_string2 = 'For'
print(string.index(sub_string))# it will return the index of starting character = 0
print(string.index(sub_string2)) # index 7 is output

#Replace the word coding in the string 'Coding For All' to Python.
string ='Coding For All'
print(string.replace('Coding', 'Python'))

#Change Python for Everyone to Python for All using the replace method or other methods.
substring = string.replace('Coding', 'Python')
print(substring.replace('All','Everyone'))

#Split the string 'Coding For All' using space as the separator (split()) .
print(string.split()) #['Coding', 'For', 'All']

#"Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
string = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(string.split(','))

#What is the character at index 0 in the string Coding For All.
string = 'Coding For All'
print(string[0]) #C

#What is the last index of the string Coding For All.
print(string[-1]) #l

#What character is at index 10 in "Coding For All" string.
print(string[10]) #space

#Create an acronym or an abbreviation for the name 'Python For Everyone'.
name = "Python For Everyone"
acronym = ''.join(word[0].upper() for word in name.split()) # Acronym

print("Original phrase:", name)
print("Acronym:", acronym) #PFE

#Create an acronym or an abbreviation for the name 'Coding For All'.
name = "Coding For All"
acronym = ''.join(word[0].upper() for word in name.split())
print("original name: ",name)
print("acronym: ",acronym)

#Use index to determine the position of the first occurrence of C in Coding For All.
string ="Coding For All"
print(string.find('C')) #0

#Use index to determine the position of the first occurrence of F in Coding For All.
print(string.find('F')) #7

#Use rfind to determine the position of the last occurrence of l in Coding For All People.
print(string.rfind('l')) #13

#Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
sentence = 'You cannot end a sentence with because because because is a conjunction'
print(sentence.find('because'))

#Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print(sentence.rindex('because'))

#Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
original_sentence = 'You cannot end a sentence with because because because is a conjunction'
start_index = original_sentence.find('because') ## Finding the index of the first occurrence of 'because'
sliced_phrase = original_sentence[start_index:start_index + len('because because because')] # Slicing out the phrase
print(sliced_phrase)

#Find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print(sentence.find('because'))

#Does ''Coding For All' start with a substring Coding?
string ='Coding For All'
print(string.startswith('Coding'))

#Does 'Coding For All' end with a substring coding?
print(string.endswith('Coding'))

#'   Coding For All      '  , remove the left and right trailing spaces in the given string.'''
string = '   Coding For All      '
print(string)
print(string.strip())

#Which one of the following variables return True when we use the method isidentifier():
#30DaysOfPython
#thirty_days_of_python
challenge = '30DaysOfPython'
print(challenge.isidentifier()) # False, because it starts with a number
challenge = 'thirty_days_of_python'
print(challenge.isidentifier()) # True

#The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
string = '# '.join(libraries)
print(string)

#Use the new line escape sequence to separate the following sentences.
#I am enjoying this challenge.
#I just wonder what is next.
print('I am enjoying this challenge.\nI just wonder what is next.')

'''Use a tab escape sequence to write the following lines.
Name      Age     Country   City
Mayuri  250     Finland   Helsinki'''
print('Name\tAge\tCountry\tCity')
print('Mayuri\t250\tFinland\tHelsinki')

''''Use the string formatting method to display the following:
radius = 10
area = 3.14 * radius ** 2
The area of a circle with radius 10 is 314 meters square. '''
radius = 10
pi = 3.14
area = pi * radius ** 2
formated_string = 'The area of a circle with a radius {} is {}.'.format(radius, area) # 2 digits after decimal
result_string = f'The area of a circle with a radius {radius} is {area}.'
print(formated_string)
print(result_string)

'''Make the following using string formatting methods:
8 + 6 = 14
8 - 6 = 2
8 * 6 = 48
8 / 6 = 1.33
8 % 6 = 2
8 // 6 = 1
8 ** 6 = 262144'''

a = 8
b = 6

print('{} + {} = {}'.format(a, b, a + b))
print('{} - {} = {}'.format(a, b, a - b))
print('{} * {} = {}'.format(a, b, a * b))
print('{} / {} = {:.2f}'.format(a, b, a / b)) # limits it to two digits after decimal
print('{} % {} = {}'.format(a, b, a % b))
print('{} // {} = {}'.format(a, b, a // b))
print('{} ** {} = {}'.format(a, b, a ** b))
