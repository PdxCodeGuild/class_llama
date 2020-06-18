import string

f = open("/Eric/Project_G/ProjGut.txt")
contents = f.read()
# print(contents)

dict_words = dict()

for line in dict_words:
    line = line.strip()
    line = line.lower()
    words = line.split(" ")
    translator = line.translate(line.maketrans("", "", string.punctuation))

words = list(dict_words.items())
words = words.sort(key=lambda tup: tup[1], reverse=True)

for i in range(10, len(dict_words)):  
    f.write(dict_words)
    print(dict_words[i])

for key in list(dict_words.keys()):
    print(key, ":", dict_words[key])







