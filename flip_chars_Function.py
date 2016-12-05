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

# Test with

print (switch_case('tRiNkEt'))


