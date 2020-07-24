import string

with open('file.txt') as f: 
    contents = f.read()

#print(contents)

 # all words to lower case and splits string into list
    contents = contents.lower()
    #print(contents)
#s.strip('contents')

    translator = str.maketrans('' , '' , string.punctuation)
    #print(translator)
    content = contents.translate(translator) 
    #print(content)

    #put content into a list of words
    content = content.split()
    #print(content) 
       

    #create dictionary 
    word_dict = {}

    #add words from content list to dictionary with count occurence, remove most commonly used words
    for i in range(len(content)): 
        stopwords = ['the' , 'of' , 'and' , 'to' , 'a' , 'is' , 'in' , 'or']
        if content in stopwords:
            content.remove(content)
        else:
            word_dict[content[i]] = content.count(content[i])
    print(word_dict)

    #word_dict 
    words = list(word_dict.items())
    #print(words)
    words.sort(key=lambda tup: tup[1], reverse=True)
    for i in range(min(10, len(words))):
        print(words[i])
        
        





    
 
