1)
b) When it reached less than twenty it gave an error. KeyError 19.

2)a) I can win if the negamax parameter is 1, if it's more than 1 than its always a draw. AI plays good but it plays same even if the parameter is 2 or 7. If its 1 then it looses.
b) GameController([Human_Player(), AI_Player(algorithm)]).play() change this line on 51 to this:-
   GameController([Human_Player(), Human_Player()]).play()
3)b) As we increase parameters, it slows down the program as it does more calculation then the previous parameter.
c)If we change the parameters here in this statement:-
    algo_neg = Negamax(5)
    algo_sss = SSS(5)
  to this 
    algo_neg = Negamax(5)
    algo_sss = SSS(1)
    
    This will help player one win
