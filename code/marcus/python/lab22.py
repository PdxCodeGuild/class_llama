import re
import math
import string

from lab22t import moontotal

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
# turns the input text into a string so regex can read it better
moontotal_new = str(moontotal)

# removes punctuation from input text
moontotal_words = re.sub(r'[^\w\s]','',moontotal_new)

# breaks up every word into the characters and puts it into a list
moontotal_charac_list = list(moontotal_words)

# turns input text into a list of words
moontotal_words_list = moontotal_words.split(' ')

# turns input text into a list of sentences
moontotal_sentence_list = moontotal_new.split(".")

moonmath_ch_wor = float(4.71*(int(len(moontotal_charac_list)/len(moontotal_words_list))))

moonmath_ch_wor_round = math.ceil(moonmath_ch_wor)


moonmath_wor_sent = float(0.5*(int(len(moontotal_words_list)/len(moontotal_sentence_list))))

moonmath_wor_sent_round = math.ceil(moonmath_wor_sent)


we_choose_to_go_to_the_moon = dict(math.ceil(float((moonmath_wor_sent_round + moonmath_ch_wor_round) - 21.43)))


for x in ari_scale:
    we_choose_to_go_to_the_moon == ari_scale['x']
    if we_choose_to_go_to_the_moon >= ari_scale['14']:
        print("The ARI for We Choose To Go To The Moon is 23.""This corresponds to a college-level difficulty,""suitable for the average 18-22 year old.")
