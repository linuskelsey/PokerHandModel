from model import models, stages
from encoding import encode_card

# Setup
print("\nWelcome to the Poker Hand Predictor! Use this tool to see the predicted win probability of any poker hand.")
stage = input('First, which stage of the hand are you in? Enter "p" for preflop, "f" for flop and so on. ')
while stage not in ['p', 'f', 'r', 't']:
    stage = input('Please enter a value from "p", "f", "r" and "t". ')
stage_long = stages[stage]

model = models[stage]
n_com_cards = len(model.coef_[0]) - 2

print("\n\t-----\n")

pocket = []
community = []

# Pocket cards
pc1 = input("Great! Let's see your pocket cards now (don't worry I won't tell anyone). Enter your first pocket card in RankSuit format like such: 7S = 7 of Spades, QH = Queen of Hearts, TD = Ten of Diamonds. ").title()
while True:
    try:
        pc1 = encode_card(pc1)
        pocket.append(pc1)
        break
    except ValueError:
        pc1 = input("Please enter a valid format of card. ")

pc2 = input("Enter your second pocket card in RankSuit format. ").title()
while True:
    try:
        pc2 = encode_card(pc2)
        pocket.append(pc2)
        break
    except ValueError:
        pc2 = input("Please enter a valid format of card. ")

# Community cards
if n_com_cards > 0:
    print("\n\t-----\n\nOkay, so we have your pocket cards, now we just need the {} community cards on the table.".format(n_com_cards))
    idx_str = ['1st', '2nd', '3rd']

    for i in range(3):
        cc = input("Enter the {} community card in RankSuit format. ".format(idx_str[i])).title()
        while True:
            try:
                cc = encode_card(cc)
                community.append(cc)
                break
            except ValueError:
                cc = input("Please enter a valid format of card. ")

    if n_com_cards > 3:
        for i in range(3, n_com_cards):
            cc = input("Enter the {}th community card in RankSuit format. ".format(i+1)).title()
            while True:
                try:
                    cc = encode_card(cc)
                    community.append(cc)
                    break
                except ValueError:
                    cc = input("Please enter a valid format of card. ")

# Calculation and output
print("Amazing! Now that we have your cards, let's calculate your predicted probability of winning this hand.")
cards = [pocket + community]
prob = model.predict_proba(cards)[0][1]
print(prob)