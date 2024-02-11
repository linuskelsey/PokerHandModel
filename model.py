import json
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

stage = input('Which stage of the game would you like to prepare the model for? ("p" - preflop, "f" - flop, "r" - river or "t" - turn) ')
while stage not in ['p', 'f', 'r', 't', 'a']:
    stage = input('Please select one of "p", "f", "r", "t" and "a". ')

stages = {'p': 'preflop', 'f': 'flop', 'r': 'river', 't': 'turn'}
stage_file_str = 'game_data/encoded_' + stages[stage] + '.json'

X, Y = [], []
with open(stage_file_str, 'r') as f:
    X, Y = json.loads(f.read())
    f.close()

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)
clf = LogisticRegression().fit(X_train, Y_train)