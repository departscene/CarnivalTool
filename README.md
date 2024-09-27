# Idle Heroes Carnival Event Calculator

This is a simple calculator to help with the Carnival Event. At each step after each square
has been revealed, it calculates the average number of flags each line will get.

It does this by testing all the permutations of the remaining numbers and the places they could
be found. It then converts line total to its corresponding number of flags and calculates the average.
This allows you to see which columns will on average yield the best results.

## How to use

1. Change the current working directory to inside `Carnival Tool` folder.
2. Run the main script with `python main.py` (the `python` command may be under a different alias. If this doesn't
work, try `py` and `python3`, otherwise check your PATH environment variables).
3. Enter the code for the square revealed. The format should be `sv` where `s` is the square number and `v` is the revealed value
- For example, if square 5 is revealed to contain a 4, you would enter `54`.
- Enter 'new' to start a new board.
- CTRL+C to kill the program
4. Read the output to see which columns are most likely to yield the best results. The results are in average number of flags for that particular line across all possible ways the remaining numbers could be placed.

**NOTE: This program does NOT stop you from entering more revealed squares than the game allows. You should manually type `new` when you have revealed all the allowed squares**

## Square Indices

The squares are indexed as follows:

```
  1 2 3
  4 5 6
  7 8 9
```

The line names are pretty self explanatory:
- Diagonal 1 is from top left to bottom right, and Diagonal 2 is from top right to bottom left.
- Column 1 is the leftmost column, and Column 3 is the rightmost column.
- Row 1 is the top row, and Row 3 is the bottom row.

## Strategy

This may not be the best strategy, but I used a greedy best-first search strategy on my account. After the game reveals a random square at the start of each scratchcard, I always revealed the middle square. Then after that I explored the 'most promising' line based on the program's analysis. There may be a more optimal way to reveal squares but this was just the strategy I used to get a good amount of success.