Hexapawn
========

Two-player combinatorial game on a 3x3 grid with three pawns from each player.
The initial game board is as follows:

```plain
  | 0 | 1 | 2 |
---------------
0 | B | R | R |
---------------
1 |   |   |   |
---------------
2 | B | B | B |
---------------
```

`R` represents a Red pawn. `B` represents a Blue pawn. 
Without loss of generality, the first player is Red.

To play the game:
Run 'Hexapawn.py' and type 'n' when asked prompted to
solve for a winnner, then select either 'r'ed or 'b'lue
to begin playing.

The rules of the game are simple; as the name suggests, 
Hexapawn is based on the game of Chess only in this game 
all the pieces are pawns. 
Each pawn can only move straight forwards by one space and 
only if there is no other piece in the way. Each pawn can 
also capture any piece of the opposing color, that is one 
space diagonally forwards to the left or right.
The game is won when a pawn reaches the opposite side of 
the board from which it started or when the opposing player 
has no possible moves or no pieces remaining.
