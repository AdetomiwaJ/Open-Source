
'''
    Script Name: Valentine Flames
    Author: Adetomiwa Jeminiwa

    FLAMES is a popular game named after the acronym:
    Friends, Lovers, Admirers, Marriage, Enemies, Situationship.
    This game does not accurately predict whether or
    not an individual is right for you,
    but it can be fun to play this with your friends


   | F | L | A | M | E | S |
   | 1 | 2 | 3 | 4 | 5 | 6 |
     6   7   8   8 | 9 | 10|
     11  12  13  14| 15| 16|
     17  18  19  20| 21| 22|
     23  24  25  26| 27| 28|

    F = 1,6,11,17,23
    L = 2,7,12,18,24
    A = 3,8,13,19,25
    M = 4,9,14,20,26
    E = 5,10,15,21,27
    S = 6,11,16,22,28
'''

Name = input('Please enter your name & surname: ')

Name = Name.split()

Name = Name[0] + Name[1]

Other_Name = input("Please enter the other person\'s name & surname: ")

Other_Name = Other_Name.split()

Other_Name = Other_Name[0] + Other_Name[1]


All_Names = Name.upper() + Other_Name.upper()

unique_name = ''.join(set(All_Names)) # variable to store unique letters from both names

size = len(unique_name)



F = [1,6,11,17,23]
L = [2,7,12,18,24]
A = [3,8,13,19,25]
M = [4,9,14,20,26]
E = [5,10,15,21,27]
S = [6,11,16,22,28]

#big IF statements

if size in F:
    print ('You are FRIENDS!')
elif size in L:
    print ('You are LOVERS!')
elif size in A:
    print ('You are ADMIRERS!')
elif size in M:
    print ('You should be MARRIED!')
elif size in E:
    print ('Run! You are ENEMIES!')
elif size in S:
    print ('You are in a SITUATIONSHIP!')

















