# Count Words: Metamorphosis

import string
# import pprint


with open("metamorphosis.txt", "r") as file_m:
    content = file_m.read()
    # print(content)


# keep writing over "content" variable


# make everything lowercase
content = content.lower()
# print(content)


# strip puntuation and split into list of words
translator = str.maketrans('', '', string.punctuation)

content = content.translate(translator)

content = str.split(content)
# print(content)


# create a list that counts the words
word_count = []

for word in content:
    word_count.append(content.count(word))

word_count = list(zip(content, word_count))
# print(word_count)


# change list to dictionary
word_dict = dict(word_count)
# pprint.pprint(dict(word_count))


# remove the stop words, pass over any not included in the dictionary
stopwords = ['gregor', 'gregors', 'i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't"]

for key in stopwords:

    if key not in word_dict:
        pass
    else:
        del word_dict[key]

# print(a_dictionary)


# .items() returns a list of tuples
words = list(word_dict.items())


# sort words largest to smallest based on count
words.sort(key=lambda tup: tup[1], reverse=True)


# print the top 10 words
for i in range(min(10, len(words))):
    print(words[i])
    
