import main as ce
import chess as ch

class Main:

    def __init__(self, board=ch.Board):
        self.board = board

    #ihmisen liike
    def playHumanMove(self):
        try:
            print(self.board.legal_moves)

            #input ihmisen liikkeestä
            play = input("Liikkeesi: ")
            if (play=="undo"):
                self.board.pop()
                self.board.pop()
                self.playHumanMove()
                return
            self.board.push_san(play)
        except:
            self.playHumanMove()

    #koneen liike
    def playEngineMove(self, maxDepth, color):
        engine = ce.Engine(self.board, maxDepth, color)
        self.board.push(engine.getBestMove())

    #aloitus
    def startGame(self):
        #ottaa ihmisen värin
        color = None
        while(color!="b" and color!="w"):
            color = input("aloitus (b tai w)")
        maxDepth=None
        while(isinstance(maxDepth, int)==False):
            maxDepth = int(input("Syvyyshaun syvyys"))
        if color == "b":
            while (self.board.is_checkmate()==False):
                print("Kone miettii")
                self.playEngineMove(maxDepth, ch.WHITE)
                print(self.board)
                self.playHumanMove()
                print(self.board)
            print(self.board)
            print(self.board.outcome())
        elif color == "w":
            while (self.board.is_checkmate()==False):
                print(self.board)
                self.playHumanMove()
                print(self.board)
                print("Kone miettii")
                self.playEngineMove(maxDepth, ch.BLACK)
            print(self.board)
            print(self.board.outcome())
        #rese
        self.board.reset
        #uusi peli
        self.startGame()

#luo pelin
newBoard= ch.Board()
game = Main(newBoard)
bruh = game.startGame()