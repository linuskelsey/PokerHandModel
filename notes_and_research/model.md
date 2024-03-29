# The Model

Because we'll be working with 0-1 outputs in the training data, but want to assign each testing and actual input a number in [0,1], I think a supervised logistic regression model will work the best.

Having looked at the wiki page for [logistic regression](https://en.wikipedia.org/wiki/Logistic_regression), it seems we'll have to do one model per stage of the game, so that would be one model for the preflop, one for the flop and so on. Each model would be trained on the same data (just at each stage, separated out), and each model would be MLR, just with different coefficients and hyper-parameters.

We'll be using the `scikit-learn` package and their [`LogisticRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html) model to build our predictor.