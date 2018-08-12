# CellularCaves.py
Caves generated via Cellular Automata as per the algorithm explained in [roguebasin](http://www.roguebasin.com/index.php?title=Cellular_Automata_Method_for_Generating_Random_Cave-Like_Levels), implemented in Python.

So far it's just the basic caves generation. Running `python cellularcaves.py` will ask you for the width and height of the map, and how many iterations of the cellular automata to pass it through, printing to the console the original random map and each version of the map after every iteration.

The chance for walls to spawn at the start is set at 45%. Outputs seem to have little variance outside "looks good" and "flooded"/"completely empty" and letting the user define that percentage just made running the demo a bit more cumbersome if you don't know the base parameters, but I've left the code to change it to user input commented out inside. Same thing happens with the "rule" that decides how many walls have to exist in a 3x3 cell for the center tile to be a wall in the next iteration, which is currently set at 5.
