import json
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

class Color:
    BOLD = '\033[1m'
    GREEN = '\033[32m'
    CYAN = '\033[36m'
    WHITE = '\033[97m'
    CLEAR = '\033[0m'

print("Building models for each stage...")

stages = {'p': 'preflop', 'f': 'flop', 'r': 'river', 't': 'turn'}
models = {k: None for k in stages.keys()}

for short, stage in stages.items():
    X, Y = [], []
    stage_file_str = 'game_data/encoded_' + stage + '.json'
    with open(stage_file_str, 'r') as f:
        X, Y = json.loads(f.read())
        f.close()

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)
    clf = LogisticRegression().fit(X_train, Y_train)

    models[short] = clf

    print("\n{}{}{} model built.".format(Color.BOLD + Color.GREEN, stage.upper(), Color.CLEAR))
    print("{}Parameters{}: {}".format(Color.CYAN, Color.CLEAR, [round(c, 7) for c in clf.coef_[0]]))
    print("Mean {}Accuracy{} on Training Data: {}{}{}".format(Color.CYAN, Color.CLEAR, Color.WHITE, clf.score(X_train, Y_train), Color.CLEAR))
    print("Mean {}Accuracy{} on Test Data: {}{}{}".format(Color.CYAN, Color.CLEAR, Color.WHITE, clf.score(X_test, Y_test), Color.CLEAR))
    if short != 't':
        print("\n\t-------")

print("\nAll models built.")