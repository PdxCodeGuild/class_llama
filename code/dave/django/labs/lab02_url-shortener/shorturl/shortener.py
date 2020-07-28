import random
import string

class ShortenCode:
    token_size = 5

    
    def __init__(self, token_size=None):
        # if token_size is not None:
        #     self.token_size = token_size
        # else:
        #     token_size = 5
        self.token_size = token_size if token_size is not None else 5 # one liner 

    def issue_token(self):
        letters = string.ascii_letters
        return ''.join(random.choice(letters) for i in range(self.token_size))