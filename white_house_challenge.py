# Example code for the challenge presented by Ed Felton on
# https://whitehouse.gov/blog/2015/05/17/hello-world

# Solution:
# Alice guesses what she flipped, Bob guesses what he did NOT flip
# This will allow them to win 100% of the time.


from random import randint

# Sides of the coin
HEADS = 0
TAILS = 1

# Play a round of the game
def play():
    # Do the coin flips 
    alice_flip = randint(HEADS, TAILS) 
    bob_flip = randint(HEADS, TAILS)
    
    # Make their guesses
    alice_guess = alice_flip        # Alice guesses the same thing as she flipped
    bob_guess = (TAILS, HEADS)[bob_flip == TAILS]    # Bob guesses what he did NOT flip

    # Print out the results
    print("Alice Flip...: ", ("Heads", "Tails")[alice_flip == TAILS])
    print("Alice Guess..: ", ("Heads", "Tails")[alice_guess == TAILS])
    print("Bob Flip.....: ", ("Heads", "Tails")[bob_flip == TAILS])
    print("Bob Guess....: ", ("Heads", "Tails")[bob_guess == TAILS])
    print("")
    print("Result.......: ", ("They Lost", "They Won!")[(alice_guess == bob_flip) or (bob_guess == alice_flip)]) # They won if Alice's guess was right OR if Bob's guess was right
    print("")
    

# Play the game ten times
for i in range(1, 10):
    print("===== Round ", i, " =====")
    play()
