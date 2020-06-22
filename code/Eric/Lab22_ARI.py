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
import math
import string

def main():
    with open("ARI_file.txt", encoding = 'utf-8') as f:
        contents = f.read()

# Counting characters in a text file or string
    characters = []
    for letter in contents:
      characters.append(letter)

    sentences = contents.split(".")

    translator = str.maketrans('','',string.punctuation)
    contents = contents.translate(translator)

    words = contents.split()

    ARI = math.ceil(4.71 * (len(characters)/len(words)) + .5 * (len(words)/len(sentences)) -21.43)


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

    for num in ari_scale:
        if num == ARI:
            age_level = ari_scale[num]

    if ARI > 14:
        print("This document has an ARI rating that exceeds college level. It should only be read by those masochistic enough for grad school.")
    else:
        print(f"This document has an ARI rating of {ARI}.\n This corresponds to a reading level of {age_level['grade_level']} comprehension. \n It is suitable for an average person who is {age_level['ages']} years old.")


if __name__ == "__main__":
    main()



