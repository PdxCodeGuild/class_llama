import string
import math

def main():
    with open('sherlock.txt', encoding = 'utf-8') as f:
        contents = f.read()

    characters = []
    for letter in contents:
        characters.append(letter)

    sentences = contents.split(".")


    translator = str.maketrans('','',string.punctuation)
    contents = contents.translate(translator)

    words = contents.split()

    ari = math.ceil(4.71 * (len(characters)/len(words)) + .5 * (len(words)/len(sentences)) -21.43)



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
        if num == ari:
            age_level = ari_scale[num]

    if ari > 14:
        print("This document has an ARI rating that exceeds college level. It should only be read by those masochistic enough for grad school.")
    else:
        print(f"This document has an ARI rating of {ari}.\n This corresponds to a reading level of {age_level['grade_level']} comprehension. \n It is suitable for an average person who is {age_level['ages']} years old.")


if __name__ == "__main__":
    main()