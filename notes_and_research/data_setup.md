# Data Setup

## Raw Data

The data we currently have is ~115,000 entries of this form:

```
<obj> = {
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
<data_point> = [
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

I have decided not to follow this approach following an investigation into the logistic regression model (see [`model.md`](model.md)). I will scrape the encoded data into a number of different `.json` files, most likely within [PokerHandsDataset](https://github.com/linuskelsey/PokerHandsDataset) itself, so for example we will have something like `encoded_preflop.json`, `encoded_flop.json` and so on. Then from each of these `.json`'s, I will build my various models with the logistic regression model.

## Importing Data

This repository is set up to be concurrent with [PokerHandsDataset](https://github.com/linuskelsey/PokerHandsDataset), so as a prerequisite you will need to clone this repo, and follow the commands all the way through to the separation of the data (at least one stage).

### Tutorial

From this directory, run the terminal scripts as such:

```zsh
cd ../                                            # move above current directory
git clone https://github.com/linuskelsey/PokerHandsDataset.git

mkdir PokerHandsML                                # OPTIONAL - only needed if both repos cloned into an already populated folder
mv PokerHandsDataset PokerHandsML
mv PokerHandModel PokerHandsML                    # Keep everything tidy!

cd PokerHandsML/PokerHandsDataset                 # move into the dataset folder
wget http://poker.cs.ualberta.ca/IRC/IRCdata.tgz  # download the database (-> IRCdata.tgz)
tar -xvf IRCdata.tgz                              # unzip the tgz file (-> IRCdata)

python3 extract.py                                # extract data (-> hands.json)
python3 clean.py                                  # drop invalid hand data (-> hands_valid.json)
python3 extract_basic.py                          # extract only the board, players' pocket cards and winners (-> hands_basic.json)
# Remove trailing comma in hands_basic.json here
python3 encode_basic.py                           # encode data from hands_basic.json into integers for a machine learning model (-> encoded_basic.json)

mkdir game_data                                   # setup folder for separated data
python3 separate_stages.py                        # separate encoded data into different stages of a hand (preflop, flop, river and turn (or all))
cp -rf game_data ../PokerHandModel                # copy separated data to model folder

cd ../PokerHandModel                              # return to model directory
```