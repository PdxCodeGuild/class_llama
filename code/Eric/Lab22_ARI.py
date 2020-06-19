"""
Score  Ages     Grade Level
     1       5-6    Kindergarten
     2       6-7    First Grade
     3       7-8    Second Grade
     4       8-9    Third Grade
     5      9-10    Fourth Grade
     6     10-11    Fifth Grade
     7     11-12    Sixth Grade
     8     12-13    Seventh Grade
     9     13-14    Eighth Grade
    10     14-15    Ninth Grade
    11     15-16    Tenth Grade
    12     16-17    Eleventh grade
    13     17-18    Twelfth grade
    14     18-22    College

Output should look like:

The ARI for gettysburg-address.txt is 12
This corresponds to a 11th Grade level of difficulty
that is suitable for an average person 16-17 years old.

"""
f = open("ARI_file.txt", "r")
for x in f:
  print(x)

# Counting characters in a text file or string
def count_chars(txt):
	result = 0
	for char in txt:
		result += 1     # same as result = result + 1
	return result
print(count_chars(txt))

# Counting words in text or string
test_string = "This is how to use the split() function while counting words in a sentence"
#original string
print ("The original string is : " + test_string)
# using split() function
res = len(test_string.split())
# total no of words
print ("The number of words in string are : " + str(res))


def ARI(text):
	score = 0.0 
	if len(text) > 0:
		score = 4.71 * (len(text) / len(text.split()) ) +  0.5 * ( len(text.split()) / len(text.split('.'))) - 21.43 
		return score if score > 0 else 0

"""
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
"""

# Python program to print list 
# using for loop 
a = [1, 2, 3, 4, 5] 
  
# printing the list using loop 
for x in range(len(a)): 
    print(a[x])



