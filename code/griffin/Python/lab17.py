

def check_palindrome(word):
    word = word.lower()
    wordlist = []
    #creates a list of letters
    for letter in word:
        wordlist.append(letter)

    #creates a reversal of that list
    new_wordlist = wordlist.copy()
    new_wordlist.reverse()

    #checks the two lists against each other to determine whether there is a palindrome
    if wordlist == new_wordlist:
        return True
    else:
        return False

def check_anagram(word1, word2):
    #deformats each word
    word1 = word1.lower()
    word2 = word2.lower()
    word1 = word1.replace(" ", "")
    word2 = word2.replace(" ", "")

    #creates and sorts lists of the letters in the words
    wordlist_1 = []
    wordlist_2 = []
    for letter in word1:
        wordlist_1.append(letter)
    for letter in word2:
        wordlist_2.append(letter)
    wordlist_1.sort()
    wordlist_2.sort()

    #checks to see if the two lists are the same
    if wordlist_1 == wordlist_2:
        return True
    else:
        return False



