# Data Setup

## Raw Data

The data we currently have is ~115,000 entries of this form:

```json
{
    "num_players": <num_players>,
    "board": <board_cards>,
    "players": <players_list>,
    "id": <id>
}
```

The `<board_cards>` and `<players_list>` consist of various representations of cards (encoded into unique numerical format from 2-53), with the latter taking the form of:

```python
[
    [<player_1_cards>, <player_1_won>],
    [<player_2_cards>, <player_2_won>],
    ...
    [<player_n_cards>, <player_n_won>]
]
```

Now, the `<board_cards>` and `<player_i_cards>` variables take similar forms, the first being a list of 5 and the latter being a list of 2 of the aforementioned unique numerical values. `<player_i_won>` is a 0-1 boolean representing if the ith player had non-zero winnings or not.

## Intention of Model and Requirements of Data

