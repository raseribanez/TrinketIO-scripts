# Ben Woodfield
# So heres the final version where it's wrapped in a function
# Flip the mixed case characters in a string (eg BaNaNaNa!)

def switch_case(string):
    string_list = [] 
    for i in string:
        if i.isupper():
            string_list.append(i.lower())
        elif i.islower():
            string_list.append(i.upper())
        else:
            string_list.append(i)

    return(''.join(string_list))
    
# test with
print switch_case("TrInKeT")
