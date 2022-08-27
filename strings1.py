#         0123456789012345678901234567  
from operator import le


letter = "abcdefghijklmnopqrstuvwxyz"

print(letter[15])
print(letter[17])
print(letter[8])
print(letter[19])
print(letter[4])
print(letter[18])
print(letter[7])

print(letter[15] + letter[17] + letter [8] + letter[19] + letter[4] + letter[18] + letter[7])
print(letter[16:19])
print(letter[:])
print(letter[15] + letter[17] + letter[8] + letter[13] +letter[18] +letter[8])

print(letter[16:13:-1])


#slice the string to produce edcba
print(letter[4::-1])

#slice the string to produce the last 8 character, in reverse order
print(letter[:-9:-1])

print(letter[-4:])