# Tower of Hanoi 
Tower of Hanoi is a puzzle consisting of imaginary pegs and discs, where each disc gets smaller in size with the largest one at the bottom. This is implemented through recursion, where the smallest disc in sequence begins as the source and is moved to the target location.

## Core Functions
### hanoi_solver()
hanoi_solver() establishes position with a dictionary. Each key represents said position, with the first key's value representing the starting position to work from. The following values for the remaining keys are initially empty to allow recursive movement.

### solve_move()
solve_move() uses positional arguments and if statements to append movements and directly facilitate recursion. The positional arguments set the guidelines as the key:value pairs that represent the peg lists gets removed from one position and added to another.
