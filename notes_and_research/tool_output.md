# Tool Output

## Representation

In terms of the representation of the tool, I'm not overly bothered by it (at the moment). I'm thinking a simple command line tool, allowing you to enter the stage of competition, table cards and pocket cards. Something like:

```zsh
Enter the stage of the competition (preflop 'p', flop 'f', river 'r', turn 't'): f
Enter the first community card: 6h
Enter the second community card: qd
Enter the third community card: 3s
     ---    ---   ---   ---
Enter your first pocket card: qs
Enter your second pocket card: jh
     ---    ---   ---   ---
Calculating prediction...
Your predicted win percentage is: 63.27%
Go for it, you can win this pot!
```

I think actually I'd like to make a web app to represent the model output and data. The page will consist of multiple stages before a win percentage is given. First, he player's pocket cards are selected, then the player chooses the stage of the hand that they are in, and finally, they choose the community cards. From these the tool prints the predicted win probability. 

First I will make a terminal tool as a prototype.