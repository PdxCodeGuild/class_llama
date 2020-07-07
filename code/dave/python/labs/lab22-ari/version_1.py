"""
This program will
"""
import re
import string
import math



# create main func
def main():

    # open gettysburg address file and display contents
    with open("./gettysburg_address.txt") as f:
        file_contents = f.read()
        # print(file_contents + "\n\n") # works


        # determine number of sentences and store in var 'num_sentences'
        sentences = re.split(r'[.!?]+', file_contents)
        num_sentences = len(sentences)
        # print(num_sentences) # works
        # print(type(num_sentences)) # type is int

        # determine number of words and store in var 'num_words'
        num_words = len(re.findall(r'\w+', file_contents))
        # print(num_words) # works

        # take out all punctuation
        no_punc = re.sub(r'[^\w\s]','',file_contents)
        # print(no_punc + "\n\n") # works

        # get number of characters
        num_chars = len(no_punc) - no_punc.count(' ')
        # print(num_chars) # works

        # calculate the score and round up if decimal
        score = 4 * (num_chars/num_words) + 0.5 * (num_words/num_sentences) - 21.43
        score = math.ceil(score)
        # print(score) # works
        if score > 14:
            score = 14

        # dictionary of ari scale values
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

        grade_level = ari_scale[score]
        
        message = '-'*100 + '\n'
        message += f"The ARI for gettysburg_address.txt is {score}. "
        message += f"\nThis corresponds to a {grade_level['grade_level']} level of difficulty"
        message += f"\nthat is suitable for an average person {grade_level['ages']} years old\n"
        message += '-'*100 + '\n'
        print(message)

main()