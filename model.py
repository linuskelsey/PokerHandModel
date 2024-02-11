import json
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

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

    print(f"\n{stage.title()} model built.")
    print(f"Parameters: {[round(c, 5) for c in clf.coef_[0]]}")