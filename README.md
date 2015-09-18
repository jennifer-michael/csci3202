# csci3202

The second heuristic I used is Euclidean distance. I chose to use this heuristic because Euclidean distance will calculate a shorter/more accurate path than a Manhattan distance will. Compared to using the Manhatten distance heuristic, the Euclidean distance heuristic got nearly the same distance of 130 but it only evaluated 48 locations. The Manhatten distance heuristic calculated a distance of 138 and evaluated 62 locations (added something to open 62 times).

The path Manhatten distance finds for World1 is:
(0,0)
(1,0)
(2,0)
(3,1)
(3,2)
(4,3)
(5,4)
(6,4)
(7,4)
(8,5)
(9,6)
(9,7)

The path Euclidean distance finds for World1 is:
(0,0)
(1,1)
(2,0)
(3,1)
(4,2)
(4,3)
(5,4)
(6,4)
(7,5)
(7,6)
(8,7)
(9,7)


The command line arguments ask for the maze file and a heuristic abbreviation.
Type in World1.txt or World2.txt for the first argument.
Type in M for Manhatten distance heuristic or O for Other heuristic.


