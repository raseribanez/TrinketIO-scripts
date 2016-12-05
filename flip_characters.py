# Ben Woodfield
# This is not the solution itself, but the script I wrote to test the code
# This will easily merge with the games editor / automated testing
# Basically just wrap it all into the function they provide

# They asked for a program to FLIP the characters case - so previously
# I just had to convert ALL characters to upper or lower
# This time they are mixed case and they have 11 words to test
# You have to check the state of each character with isupper and islower (true or false)
# Then flip them - but keeping the punctuation (eg ! and ? or .)

# In the game you don't need ths first line it is just for my own testing
# And name_list[] has to go into the function
name = 'BaNaNaNa!!'
name_list = []

for i in name:
    if i.isupper():
        name_list.append(i.lower())
    elif i.islower():
        name_list.append(i.upper())
    else:
        name_list.append(i)

# then instead of print - use 'return' inside your function 
print (''.join(name_list))


# A shorter way to do this is:
name = "bAnAnAnAnAnAnAnA"
print(''.join(c.lower() if c.isupper() else c.upper() for c in name))

#  яaѕєя



'''
#################################################################

#def switch_case(string):
#    for i in string (lower)
#    string.capitalize()
    
    #if string isupper()
#################################################################


word = "aBcDeFgHiJkL" # 11 chars
if word[0:].isupper() == True:
    print("That character is Upper")
    print("The original word is:", word)
    new_word = word[0:5] + word[6].lower() + word[7:]
    print(new_word)
else:
    print("The character is Lower")
    
##########################################################

fruit = input('Enter Word: ')#'BaNaNa'
for char in fruit:
    print (char)
##########################################################

## print (len(fruit))
#index = 0
#while index < len(fruit):
#    letter = fruit[index]
#    print (letter)
#    index += 1
'''
