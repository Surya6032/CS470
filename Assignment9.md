1)
a)I changed max coins which a player can take to 5 and it made the AI to take only one coin at one time.
b) When it reached less than twenty it gave an error. KeyError 19. The range argument in the method takes a list of depths that it will try out. But when the range is (2,4) then its too small of range to try out all the depths as no moves are left to play.

2)a) I can win if the negamax parameter is 1, if it's more than 1 than its always a draw. AI plays good but it plays same even if the parameter is 2 or 7. If its 1 then it looses.
b) GameController([Human_Player(), AI_Player(algorithm)]).play() change this line on 51 to this:-
   GameController([Human_Player(), Human_Player()]).play()
3)
a) Player 2 algorithm which is State space search has more tree depth or is more accurate in getting the solution than Negamax therefore performs better calculation and wins everytime with same parameter.
b) As we increase parameters, it slows down the program as it does more calculation then the previous parameter. It goes in more depth of the tree therefore its slow
c)If we change the parameters here in this statement:-
    algo_neg = Negamax(5)
    algo_sss = SSS(5)
  to this 
    algo_neg = Negamax(5)
    algo_sss = SSS(1)
  
  This will help player one win. This can happen as state space search is making better decisions than Negamax algorithm. That's decreasing the depth of SSS helps           player one to win.
4)
a) This game is a variant of chess and is played between two players. In the particular game 4x4 board is taken. Also, only pawns are used, like in chess there are many pieces like:-

    The Pawn
    The Bishop
    The Knight
    The Rook
    The Queen
    The King
As in chess, each pawn may be moved in two different ways: it may be moved one square forward, or it may capture a pawn one square diagonally ahead of it. A pawn may not be moved forward if there is a pawn in the next square. Unlike chess, the first move of a pawn may not advance it by two spaces. A player loses if he/she has no legal moves or the other player reaches the end of the board with a pawn. 

b) In this game both players are AI with same parameter 12 and same algorithm which Negamax.
c) These are the following changes that were made so that a human player can play the game: -
             game = GameController([AI_Player(algorithm), 
             Human_Player()])

I was able to beat the AI when the parameter was 8. These are the following moves which lead me to win the game:-
D4 C4
D2 C1
C1 B2
C4 B4
D1 C2

5)
