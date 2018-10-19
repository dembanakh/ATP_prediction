# ATP_prediction
<b>Exploring the capabilities of some ML models as well as simple Multi Perceptron Neural Net to predict results of the tennis ATP matches .</b><br><br>


Since there are not any good patterns in sportsmen performance, ML models aren't supposed to give a good accuracy. Hence the metrics that I use
is a money you can gain betting on the matches on the models' advice. Even though all the data can be used to predict a single match winner, 
I am using just the data containing past matches of only first or second player of the match we are trying to predict. This will preserve some interesting properties of the players (eg. if it is typical of player1 to quite often lose to the weaker players but to quite often win over top players). Since The whole dataset is involving all matches played in 2017 and 2018, for a typical match a training dataset has on average 25-60 samples. While one can think it is too few especially for NN, this proves to be rather efficient and takes much less time to train.

---------------------------------------------------------------------------------------------------------------------------------------

Let's discuss some details of the idea.
I use five differnt ML models: SVM, GradientBoosting, AdaBoost, Logistic Regression and simple MLP by sklearn. For each model, I do cross-validation as one block of models and maintain a fixed ones as another. Fixed models are tuned by fixed hyperparameters that are get by running tuning programs every month (for example. Surely, this time estimate depends on the tournaments played). Results of tuning on the Masters 1000 and Grand Slam events are more valuable than on the ATP 250 tournaments, for instance.
While testing, the decision is to not consider first and second round predictions as there you can observe lots of tennisists unstability and not reliable game. At the same time, those predictions are also archived because this information is valuable as well.
To sum up on this, the "models" folder contains one python program for each of 10 models as well as one generalising program (it predicts the last n match with all 10 models and write the results to the testing table that are in "testings" folder in excel format). Besides, it contains all the models-tuning programs and file "tournaments.py" which gives you the opportunity to play with the tournament winner and draw predictions (obviously it is very unreliable).

Let's now switch to features.
