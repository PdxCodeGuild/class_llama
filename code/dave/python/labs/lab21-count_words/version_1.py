"""
This program analyzes a given text file containing a book for its vocabulary frequency and displays the most frequent words to the user in the terminal.
"""

import string

STOPWORDS = [',', 'e', 'i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't"]

# function provided by instructor Merrit
def sort_words(word_dict):
    """
    Sorts words in decending order by value
    """
    # word_dict is a dictionary where the key is the word and the value is the count
    words = list(word_dict.items()) # .items() returns a list of tuples
    words.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
    for i in range(min(10, len(STOPWORDS))):  # print the top 10 words, or all of them, whichever is smaller
        print(words[i])


def main():

    # open txt file 'countwords.txt' as countwords
    with open('the_prince.txt', 'r') as prince:

        # create a list of all words from txt file
        list_of_items = prince.read().lower()
        translator = str.maketrans('', '', string.punctuation)
        string_without_punct = list_of_items.translate(translator) # I am a string with punctuation
        wordlist = string_without_punct.split()


        # create an empty dictionary to keep track of
        word_dict = {}
        stoplist = []

        for word in wordlist:
            if word in STOPWORDS:
                pass
            else:
                stoplist.append(word)
        #   elif word not in word_dict:
        #       word_dict[word] = 1
        #   elif word in word_dict:
        #       word_dict[word] += 1
    #   word_list = list(word_dict.items())

        # iterate through each item in the list and add to dictionary. range is set to the length of the wordlist to prevent any errors and make it dynamic
        for word in stoplist:
            x = stoplist.index(word)
            word_dict[stoplist[x]] = stoplist.count(stoplist[x])
            # I am not 100% sure how this works found on YouTube 'Python Programming: Creating a dictionary from a list'
            # I understand how it works but not how I would come up with this on my own without more research.

            # longhand


        # iterate through each item in the dictionary and print the key and value for each. Formatted for readability
        for key, value in word_dict.items():
            print(key, ' : ', value)

        # call sorted_words func to display top 10 used words in decending order
        sort_words(word_dict)

# Don't forget to run the main method (happened to me once)
main()