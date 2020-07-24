import string, math

with open("/Users/justinchambers/Projects/class_llama/code/justin/manifesto.txt", "r") as file:
    text = file.read()    
  
    def characters_in(contents):
        new_string = str.strip(contents)
        chars = [char for char in new_string]
        return len(chars)
            
    def words_in(contents):
        translator = str.maketrans('', '', string.punctuation)
        contents = text.translate(translator).lower().split()
        return len(contents)
  
    def sentences_in(contents):
        sentences = 0
        for char in contents:
            if char in [".", "!", "?"]:
                sentences += 1
        return sentences


    def ari_calc(chars, words, sents):
        ari = 4.71 * (float(chars) / float(words)) + (0.5 * (float(words) / (float(sents))) - 21.43)
        return ari

    chars = characters_in(text)
    words = words_in(text)
    sentences = sentences_in(text)
    final_score = math.ceil(ari_calc(chars, words, sentences))

    if final_score > 14:
        final_score = 14
 
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
        14: {'ages': '18+', 'grade_level':      'College'},
        }

    grade_level = ari_scale[final_score]

    print(f"The ARI for manifesto.txt is {final_score}")
    print(f"This corresponds to a {grade_level['grade_level']} level of difficulty.")
    print(f"That is suitable for an average person {grade_level['ages']} years old.")

