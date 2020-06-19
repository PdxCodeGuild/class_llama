# Automated Readability Index

import math
import re
import string


# get the book
with open("metamorphosis.txt", "r") as text:
    content = text.read()

# find values for ari_score math
#remove punctuation first for a more accurate character count
punctuation = '!.?"'''
for x in content:
    if x in punctuation:
        content = content.replace(x, "")
characters = len(content)
print(characters)   
# regex above?
words = len(re.split(r"\s+", content))
print(words)
# below is the same thing without regex
# words2 = len(content.split())
# print(words2)
sentences = len(re.split(r"[.?!]\s", content))
print(sentences)
# below only splits on "." and so has less sentences
# sentences2 = len(content.split('.'))
# print(sentences2)

# get the decimal ari_num
ari_score = math.ceil(4.71 * (characters/words) + 0.5 * (words/sentences) - 21.43)
print(ari_score)


# fix dictionary format
ari_scale = {
     '1': {'ages': '5-6', 'grade': 'kindergarten'},
     '2': {'ages': '6-7', 'grade': '1st grade'},
     '3': {'ages': '7-8', 'grade': '2nd grade'},
     '4': {'ages': '8-9', 'grade': '3rd grade'},
     '5': {'ages': '9-10', 'grade': '4th grade'},
     '6': {'ages': '10-11', 'grade': '5th grade'},
     '7': {'ages': '11-12', 'grade': '6th grade'},
     '8': {'ages': '12-13', 'grade': '7th grade'},
     '9': {'ages': '13-14', 'grade': '8th grade'},
    '10': {'ages': '14-15', 'grade': '9th grade'},
    '11': {'ages': '15-16', 'grade': '10th grade'},
    '12': {'ages': '16-17', 'grade': '11th grade'},
    '13': {'ages': '17-18', 'grade': '12th grade'},
    '14': {'ages': '18-22', 'grade': 'college'}
}


# compare ari_score to ari_scale, print result
# if ari_score >= 14:
    # print("The ARI for gettysburg-address.txt is (ari_score)."/n"This corresponds to (ari_scale grade)-level difficulty,"/n"suitable for the average (ari_scale age) year old.")

