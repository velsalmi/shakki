import chess as ch
import random as rd


class Engine:

    def __init__(self, board, maxDepth, color):
        self.board = board
        self.color = color
        self.maxDepth = maxDepth

    def getBestMove(self):
        return self.engine(None, 1)

    def evalFunct(self):
        compt = 0

        for i in range(64):
            compt += self.squareResPoints(ch.SQUARES[i])
        compt += self.mateOpportunity() + self.openning() + 0.001 * rd.random()
        return compt

    def mateOpportunity(self):
        if (self.board.legal_moves.count() == 0):
            if (self.board.turn == self.color):
                return -999
            else:
                return 999
        else:
            return 0

    # Aloitus tietokoneelle, jotta tekee liikkeen nopeammin.
    def openning(self):
        if (self.board.fullmove_number < 10):
            if (self.board.turn == self.color):
                return 1 / 30 * self.board.legal_moves.count()
            else:
                return -1 / 30 * self.board.legal_moves.count()
        else:
            return 0


    def squareResPoints(self, square):
        pieceValue = 0
        if (self.board.piece_type_at(square) == ch.PAWN):
            pieceValue = 1
        elif (self.board.piece_type_at(square) == ch.ROOK):
            pieceValue = 5.1
        elif (self.board.piece_type_at(square) == ch.BISHOP):
            pieceValue = 3.33
        elif (self.board.piece_type_at(square) == ch.KNIGHT):
            pieceValue = 3.2
        elif (self.board.piece_type_at(square) == ch.QUEEN):
            pieceValue = 8.8

        if (self.board.color_at(square) != self.color):
            return -pieceValue
        else:
            return pieceValue

    def engine(self, candidate, depth):

        if (depth == self.maxDepth
                or self.board.legal_moves.count() == 0):
            return self.evalFunct()

        else:
            # Lista laillisita liikkeist
            moveListe = list(self.board.legal_moves)

            newCandidate = None

            if (depth % 2 != 0):
                newCandidate = float("-inf")
            else:
                newCandidate = float("inf")


            for i in moveListe:

                self.board.push(i)


                value = self.engine(newCandidate, depth + 1)

                # minmax algorithm:
                if (value > newCandidate and depth % 2 != 0):

                    if (depth == 1):
                        move = i
                    newCandidate = value
                #  minimizing
                elif (value < newCandidate and depth % 2 == 0):
                    newCandidate = value

                # Alpha-beta prunning
                if (candidate != None
                        and value < candidate
                        and depth % 2 == 0):
                    self.board.pop()
                    break
                elif (candidate != None
                      and value > candidate
                      and depth % 2 != 0):
                    self.board.pop()
                    break

                self.board.pop()


            if (depth > 1):

                return newCandidate
            else:

                return move





































