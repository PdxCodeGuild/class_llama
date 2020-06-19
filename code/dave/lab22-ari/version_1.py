"""
This program will
"""
import re


def main():
    with open("./gettysburg_address.txt") as f:
        file_contents = f.read()
        print(file_contents) # works

        # take out all punctuation
        no_punc = re.sub(r'[^\w\s]','',file_contents)
        print(no_punc) # works



main()