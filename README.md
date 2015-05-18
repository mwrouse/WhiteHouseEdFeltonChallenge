# Ed Felton Challenge Solution

This is a solution to the [challenge posted on the White House Blog](https://www.whitehouse.gov/blog/2015/05/17/hello-world) by [Ed Felton](https://twitter.com/EdFelten44) in Python 3.1.1.

<h3>The Problem</h3>
Alice and Bob are playing a game.  They are teammates, so they will win or lose together.  Before the game starts, they can talk to each other and agree on a strategy. 

When the game starts, Alice and Bob go into separate soundproof rooms – they cannot communicate with each other in any way.  They each flip a coin and note whether it came up Heads or Tails.  (No funny business allowed – it has to be an honest coin flip and they have to tell the truth later about how it came out.)  Now Alice writes down a guess as to the result of Bob’s coin flip; and Bob likewise writes down a guess as to Alice’s flip.

If either or both of the written-down guesses turns out to be correct, then Alice and Bob both win as a team.  But if both written-down guesses are wrong, then they both lose.


<h3>The Solution</h3>
If Alice always guesses what she flipped, and Bob always guesses what he did NOT flip, then they will win 100% of the time.


