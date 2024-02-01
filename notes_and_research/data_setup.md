# Data Setup

## Raw Data

The data we currently have is ~115,000 entries of this form:

```json
obj = {
    "num_players": <num_players>,
    "board": <board_cards>,
    "players": <players_list>,
    "id": <id>
}
```

The `<board_cards>` and `<players_list>` variables consist of various representations of cards (encoded into unique numerical format from 2-53), with the latter taking the form of:

```python3
<players_list> = [
    [<player_1_hand>, <player_1_won>],
    [<player_2_hand>, <player_2_won>],
    ...
    [<player_n_hand>, <player_n_won>]
]
```

Now, the `<board_cards>` and `<player_i_hand>` variables take similar forms, the former being a list of 5 and the latter being a list of 2 of the aforementioned unique numerical values. `<player_i_won>` is a 0-1 boolean representing if the ith player had non-zero winnings or not.

## Intention of Model and Requirements of Data

What I ultimately want this model to do is to give a (predicted) percentage probability of winning at *every* stage of a hand of hold 'em. That means, the predictor will show a (likely) different number at the pre-flop, as it does at the flop, as it does at the river and as it does at the turn.

So the question arises of: how do I build my model? And do I build only one model? Or one for each stage of the hand? Whatever the case, a single data point should look something like this:

```python3
data_point = [
    <in> = [
        <board_cards>,
        <player_hand>
    ],
    <out> = <player_won>
]
```

Here, `<board_cards>` can be an empty list, or a list of length 3, 4 or 5 (depending on the stage being modelled).

One way of doing everything all in one model (which is desirable, to improve concurrency and maintain clear file structure), is to include `<stage>` as an input, an integer from 1-4 representing one of the four stages of competition, so `<in>` would look like:

```python3
<in> = [
    <stage>,
    <board_cards>,
    <player_hands>
]
```