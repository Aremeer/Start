 # Sudoku Solver
### Video Demo:  [Sudoku Solver](https://www.youtube.com/watch?v=AdeBlJO0Kbo).
## Description:
Sudoku solver a simple programm that solvers sudoku using backtracking algorythm. Backtracking is a depth-first search, because it will completely explore one branch to a possible solution before moving to another branch. Even tho it is a relatively slow brute force method, it is guaranteed to find a solution. The idea was to search each empty cell to find possible solutions, write them down and keep going untile we can no longer find a solution. After that we move back one cell and start over, repeating the cycle until we find a solution.
## Project files:
### project.py:
The core file of the programm, containing all of the code. Here is how it works:

- Code starts by getting a unsolved sudoku from an API - [dosuku](https://sudoku-api.vercel.app/) and saves it as a csv file.
* It then reads the file and changes it's contetnts into a list of each row of the sudoku.
* It transforms the list into a list of dictionaries containing key:value pairs:
    "index":int
    "value":int
    "row":int
    "column":int
    "box":int
    "potential":boolean or list of int
    "solid":boolean
* It ask the user whether the user want's to procced.
* It then checks each cell for:
    * Whether the cell index isn't over the max index
    * *Whether cell is sold that is whether it has been in the original unsolved sudoku, sice those cell are guaranteed to be right.
    * *If all above is False it checks all possible solutions for a given cell and based solutions it get's it:
        * if there is only one solution, wirte it down and move to the next cell
        * if there is more than one solution, write it down and set the value of the key - "potential" to the rest of the solutions and move on.
        * if there is no solution move back and:
            * Check for solid again and move back if is solid
            * Else - check the potential:
            * if no potential - set cell value to 0 and move back
            * if there is one potential solution - change value to it and move forward
            * if potential is more than one - write first one down, delete it from a potential pool and move on.
    * Repeat until sudoku is solved
* Once it is solved we save it into a new file called results.csv
+ And finaly print the the sudoku.

### api.csv:
File that we save the unsolved sudoku from the API

### result.csv:
File that we save the solved sudoku into

### refrence.txt:
Refrences to the websites that used to help me write this programm.

### requirements.txt:
List of required python libraries to run the code.

### test_project.py:
Some untit tests.

### test1.csv:
Test sudoku for unit tests.

### README.md:
A README file.