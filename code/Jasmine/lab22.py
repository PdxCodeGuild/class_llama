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
        wordsList = line.split()
        lines += 1
        words += len(wordsList) # just get length of wordslist list
        chars += len(line) # gets length of line on each iteration of # of characters

print("sentences:" , lines)
print("characters:" , chars)
print("words:" , words)

# ARI formula 

ARI = 4.71*(int(chars) / int(words)) + 0.5* (int(words) / int(lines)) - 21.43

print("The ARI is:" , round(ARI))





 



