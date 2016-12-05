# Characterize level
# Just change the FIRST letter of the word to a capital letter (uppercase)

# My first answer for this worked (it solved all 11 checks)
# But brought up errors as they wanted me to use Capitalize.
string = 'the brown fox'
print string[0].upper + string[1:]

# heres the capitalize way
string.capitalize()
