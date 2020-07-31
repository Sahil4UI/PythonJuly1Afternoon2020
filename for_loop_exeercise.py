#Pattern problem->

'''
*
**
***
****
*****

for i in range(1,6):
    print("*"*i)
'''
'''
*****
****
***
**
*

for i in reversed(range(1,6)):
    print("*"*i)
'''
'''
   *
  ***
 *****
*******
#0-3 -> 0 ,1,2,3
for i in range(0,4):
    print(' '*(3-i)+"*"*(2*i+1))

'''


#->we have a given string and you have to count number of vowels, consonants in the string.
'''
string1 = input("Enter a string : ")
vowels = "aeiouAEIOU"
countVowels = 0
countConsonants = 0

for i in range(len(string1)):
    if (string1[i] >= 'a' and string1[i]<='z') or (string1[i] >= 'A' and string1[i]<='Z'):
        if string1[i] in vowels:
            countVowels +=1
        else:
            countConsonants+=1
print("vowels count : ",countVowels)
print("consonants count:",countConsonants)
'''
for i in range(65,91):
    print(chr(i))



