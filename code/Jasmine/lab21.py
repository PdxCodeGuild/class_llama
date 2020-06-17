import string

with open('file.txt') as f: 
    contents = f.read()

#print(contents)

#s = 'contents'
    contents = contents.lower()
    contents = contents.split()
    print(contents)
#s.strip('contents')

    translator = str.maketrans('' , '' , string.punctuation)
    print(translator)
    content = contents.translate(translator) 
    print(content)

    # content_1 = []
    # for in content: 
    #     for content in item.split(): 
    #         content_1.append(item)
    # print(content_1)
    

#each word to single string from multi word string 
    #content_1 = content.split(',')
    #print(content_1)

    #con = list(content_1)
    #print(con)

#create list to populate dictionary 
#dictionary of words 
#content_dict = {"": 0}