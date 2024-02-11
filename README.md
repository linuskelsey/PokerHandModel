# PokerHandModel
Machine Learning model with training data generated in [PokerHandsDataset](https://github.com/linuskelsey/PokerHandsDataset).

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

For more information on each of these scripts, check out [PokerHandsDataset](https://github.com/linuskelsey/PokerHandsDataset).


## Results

With the current encoding (RofS -> numeric(R) + 13 * numeric(S), so 7 of Hearts is mapped to 7 + 13 * 3 = 46) the accuracy for each of the four stages sits around 53%. I'm wondering whether changing the encoding to prefer rank over suit will affect anything so now the 7 of Hearts -> (7 - 2) * 4 + 3 = 23 and the Queen of Hearts -> (12 - 2) * 4 + 3 = 43.