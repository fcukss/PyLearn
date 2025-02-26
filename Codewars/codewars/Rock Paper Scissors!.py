
"""
Let's play! You have to return which player won!
In case of a draw return Draw!
"""

def rps(p1, p2):
    a = "scissors"
    b = "paper"
    c = "rock"
    if (p1==a and p2==b) or (p1==b and p2==c) or (p1==c and p2==a):
        return "Player 1 won!"
    if (p1==a and p2==c) or (p1==c and p2==b) or (p1==b and p2==a):
        return "Player 2 won!"
    if p1==p2:
        return "Draw"


assert rps('rock', 'scissors')=="Player 1 won!"
assert rps('scissors', 'rock')=="Player 2 won!"
assert rps('rock', 'rock')=="Draw"