'''
LAB 22 ARI 

Compute the ARI for a given body of text loaded in from a file. 
The automated readability index (ARI) is a formula for computing the U.S. grade level for 
a given block of text. The general formula to compute the ARI is as follows:

ARI Formula
4.71(characters/words) + 0.5 (words/sentences) - 21.43

The score is computed by multiplying the number of characters divided by the number of words 
by 4.17, adding the number of words divided by the number of sentences multiplied by 0.5, 
and subtracting 21.43. If the result is a decimal, always round up. Scores greater than 
14 should be presented as having the same age and grade level as scores of 14.

'''
import string
import math
# create string for reading characters of a document (ARI)
# string should output a score between (1 and 14)


#ARI = int(4.71* (/w[a-zA-Z]+ / [a-zA-Z]+) + 0.5* ([a-zA-Z]+) - 21.43)
#find number of characters
#find number of words
#find number of sentences
#set variables
filename = "gettysaddress.txt"
lines = 0
chars = 0
words = 0


with open(filename, 'r') as file:
    for line in file: 
        wordsList = line.split() # returns list of word in str 
        lines += 1
        words += len(wordsList) # just get length of wordslist list
        chars += len(line) # gets length of line on each iteration of # of characters

print("lines:" , lines)
print("characters:" , chars)
print("words:" , words)

# ARI formula 

ari = math.ceil(4.71*(int(chars) / int(words)) + 0.5* (int(words) / int(lines)) - 21.43)

print("The ARI of this material is:" , ari) #rounds ARI 

# use a dictionary to look up the age range and grade level equated with ARI
# first step create dictionary 

ari_scale = {
     1: {'ages':   '5-6', 'grade_level': 'Kindergarten'},
     2: {'ages':   '6-7', 'grade_level':    '1st Grade'},
     3: {'ages':   '7-8', 'grade_level':    '2nd Grade'},
     4: {'ages':   '8-9', 'grade_level':    '3rd Grade'},
     5: {'ages':  '9-10', 'grade_level':    '4th Grade'},
     6: {'ages': '10-11', 'grade_level':    '5th Grade'},
     7: {'ages': '11-12', 'grade_level':    '6th Grade'},
     8: {'ages': '12-13', 'grade_level':    '7th Grade'},
     9: {'ages': '13-14', 'grade_level':    '8th Grade'},
    10: {'ages': '14-15', 'grade_level':    '9th Grade'},
    11: {'ages': '15-16', 'grade_level':   '10th Grade'},
    12: {'ages': '16-17', 'grade_level':   '11th Grade'},
    13: {'ages': '17-18', 'grade_level':   '12th Grade'},
    14: {'ages': '18-22', 'grade_level':      'College'}
}

#function should loop through the dict to find the grade level that correponds to the ARI score

print(ari_scale[int(ari)]['ages'])

    




    

     



 



