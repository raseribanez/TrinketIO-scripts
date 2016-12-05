name = 'Mr.Ed'
name_list = []

for i in name:
    if i.isupper():
        name_list.append(i.lower())
    elif i.islower():
        name_list.append(i.upper())
    else:
        name_list.append(i)

print (''.join(name_list))

 яaѕєя
# A shorter way to do this is:
name = "bAnAnAnAnAnAnAnA"
print(''.join(c.lower() if c.isupper() else c.upper() for c in name))






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
