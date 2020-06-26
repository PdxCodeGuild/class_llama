class Player:
    def __init__(self,name,color):
        self.name = name
        self.color = color

    
class Game:
    def __init__(self):
        self.board = {(0,0):" ",(1,0):" ",(2,0):" ",(3,0):" ",(4,0):" ",(5,0):" ",(6,0):" ",
(0,1):" ",(1,1):" ",(2,1):" ",(3,1):" ",(4,1):" ",(5,1):" ",(6,1):" ",
(0,2):" ",(1,2):" ",(2,2):" ",(3,2):" ",(4,2):" ",(5,2):" ",(6,2):" ",
(0,3):" ",(1,3):" ",(2,3):" ",(3,3):" ",(4,3):" ",(5,3):" ",(6,3):" ",
(0,4):" ",(1,4):" ",(2,4):" ",(3,4):" ",(4,4):" ",(5,4):" ",(6,4):" ",
(0,5):" ",(1,5):" ",(2,5):" ",(3,5):" ",(4,5):" ",(5,5):" ",(6,5):" "}

    def __repr__(self):
        return f"""
        |0|1|2|3|4|5|6|
        |{self.board[0,0]}|{self.board[1,0]}|{self.board[2,0]}|{self.board[3,0]}|{self.board[4,0]}|{self.board[5,0]}|{self.board[6,0]}|
        |{self.board[0,1]}|{self.board[1,1]}|{self.board[2,1]}|{self.board[3,1]}|{self.board[4,1]}|{self.board[5,1]}|{self.board[6,1]}|
        |{self.board[0,2]}|{self.board[1,2]}|{self.board[2,2]}|{self.board[3,2]}|{self.board[4,2]}|{self.board[5,2]}|{self.board[6,2]}|
        |{self.board[0,3]}|{self.board[1,3]}|{self.board[2,3]}|{self.board[3,3]}|{self.board[4,3]}|{self.board[5,3]}|{self.board[6,3]}|
        |{self.board[0,4]}|{self.board[1,4]}|{self.board[2,4]}|{self.board[3,4]}|{self.board[4,4]}|{self.board[5,4]}|{self.board[6,4]}|
        |{self.board[0,5]}|{self.board[1,5]}|{self.board[2,5]}|{self.board[3,5]}|{self.board[4,5]}|{self.board[5,5]}|{self.board[6,5]}|

        """

test = Game()
print(repr(test))