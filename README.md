# Background

The tic-tac-toe game is played with two people in a 3x3 grid. One player is the ‘O’ and the other player is the ‘X’. The goal of the game is to get 3 in a row - it can be done horizontally, vertically, or diagonally. If one player were to be an AI (that plays optimally) it would prove a good challenge for the human player.

# Instructions

This is assuming that you are running it in vscode. Uncomment the last line ****#game_loop()**** by deleting the hashtag. Then all you need to do is to run the program in a write to terminal by clicking the play button in the top right. The program will ask you to input where in the tic tac toe grid you would like to place your piece. You can choose any combo of (1,2,3) for your row and columns. And like the prompt suggests, type in your row first, then press the space bar, then your column number the hit enter. 

Example: 2 2

If I wanted to place my marker in the middle spot. Typing anything else will result in an error and the system with prompt you to input something valid. If you try to place your marker in an already taken spot you will be told to choose another open spot. Once you hit enter, the AI will place their move and then it is your turn. Play the game to completion and see if you win, tie , or lose!

# Explanation

In this code I used the minimax algorithm using the alpha-beta pruning technique to make sure that the AI ran optimally. The minimax algorithm makes sure that the AI will make the most optimal move possible by recursively traversing all the possible outcomes that can happen. It is quite a time costly algorithm which is why I added the alpha-beta pruning technique. This means that this algorithm would not be very efficient if the game were to be larger. On the other hand, this algorithm always gives me the most optimal solution. It can always at least tie if not win in any situation.



****Note: lots of copy and paste from my report doc
