This folder contains the fifth homework assignment for CSCI3202, fall semester 2015.
It is a maze searching program that utilizes the value iteration algorithm.

Run Instructions:
Run the program as normal, when it asks for world input, type "World1MDP.txt", and some number when it asks for epsilon.
Then press enter and it should do its work.

Questions to answer:

I ran my program using many values of epsilon, from .5 to 1,000,000,000,000,000,000 to .00000000000000004. Nothing changed the result!
I got the same solution for the maze everytime. I started printing out the delta value that exited the while loop,
and those values varied a lot based off the epsilon. However, the solution did not change.


Results for an epsilon value of .5:
(looks much prettier if you read in the raw format!!!)


Please give me a world to navigate! Please type 'World1MDP.txt': World1MDP.txt
Please give me a value of epsilon: .5

*******************HOW THE HORSE SHOULD GET TO THE APPLE********************
(0, 0) has the utility 0.792984681064
(0, 1) has the utility 0.983170211162
(0, 2) has the utility 1.51540129824
(0, 3) has the utility 2.09308802252
(1, 3) has the utility 2.71770959917
(1, 4) has the utility 3.51304469172
(1, 5) has the utility 3.49033984961
(2, 5) has the utility 4.40862795591
(3, 5) has the utility 5.57424345649
(4, 5) has the utility 6.96637838652
(4, 6) has the utility 8.36327516163
(4, 7) has the utility 9.74680974852
(5, 7) has the utility 13.8808198928
(6, 7) has the utility 18.1856286505
(7, 7) has the utility 26.646706459
(8, 7) has the utility 36.0
(9, 7) has the utility 50

********************THIS IS THE POLICY FOR THE MAZE**********************
R R R R R R R R R *
X X R R U U X U X U
R R R R U U X R R U
X U X X R R R U X U
R U X R U X U U R U
U U X R U X R U X U
U L X U U X U U X X
U R R R R R U U L L
