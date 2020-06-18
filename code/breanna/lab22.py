# Automated Readability Index

import decimal
import math


# get the book
with open("metamorphosis.txt", "r") as text:
    content = text.read()

# find values for ari_score math
characters = len(content)
print(characters)
words = len(content.split())
print(words)
sentences = len(content.split('.'))
print(sentences)


# figure out this math nonsense
# ceil() from math module rounds up
# decimal() to do math with decimals
# ari_score = math.ceil(float(4.71(characters/words)) + (0.5(words/sentences) - 21.43)
# print(ari_score)


# fix dictionary format
# ari_scale = {
#      1: {'ages': '5-6', 'grade': 'Kindergarten'},
#      2: {'ages': '6-7', 'grade': '1st Grade'},
#      3: {'ages': '7-8', 'grade': '2nd Grade'},
#      4: {'ages': '8-9', 'grade': '3rd Grade'},
#      5: {'ages': '9-10', 'grade': '4th Grade'},
#      6: {'ages': '10-11', 'grade': '5th Grade'},
#      7: {'ages': '11-12', 'grade': '6th Grade'},
#      8: {'ages': '12-13', 'grade': '7th Grade'},
#      9: {'ages': '13-14', 'grade': '8th Grade'},
#     10: {'ages': '14-15', 'grade': '9th Grade'},
#     11: {'ages': '15-16', 'grade': '10th Grade'},
#     12: {'ages': '16-17', 'grade': '11th Grade'},
#     13: {'ages': '17-18', 'grade': '12th Grade'},
#     14: {'ages': '18-22', 'grade': 'College'}
# }


# compare ari_score to ari_scale


# what it should print out after comparing ari_score to ari_scale
# print("The ARI for gettysburg-address.txt is 12."/n"This corresponds to 11th Grade level difficulty,"/n"suitable for the average 16-17 year old.")

