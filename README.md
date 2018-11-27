# ATP_prediction
<b>Exploring the capabilities of some ML models as well as simple Multi Perceptron Neural Net to predict results of the tennis ATP matches .</b><br><br>


Since there are not any good patterns in sportsmen performance, ML models aren't supposed to give a good accuracy. Hence the metrics that I use is a money you can gain betting on the matches on the models' advice. Even though all the data can be used to predict a single match winner, I am using just the data containing past matches of only first or second player of the match we are trying to predict. This will preserve some interesting properties of the players (eg. if it is typical of player1 to quite often lose to the weaker players but to quite often win over top players). Since The whole dataset is involving all matches played in 2017 and 2018, for a typical match a training dataset has on average 40-110 samples. While one can think it is too few especially for NN, this proves to be rather efficient and takes much less time to train.

---------------------------------------------------------------------------------------------------------------------------------------

Let's discuss some details of the idea.
I use five different ML models: SVM, GradientBoosting, AdaBoost, Logistic Regression and simple MLP from sklearn. For each model, I do cross-validation as one block of models and maintain a fixed ones as another. Fixed models are tuned by fixed hyperparameters that are get by running tuning programs every month (for example. Surely, this time estimate depends on the tournaments played). Results of tuning on the Masters 1000 and Grand Slam events are more valuable than on the ATP 250 tournaments, for instance.
While testing, the decision is to not consider first and second round predictions as there you can observe lots of tennisists unstability and not reliable game. At the same time, those predictions are also archived because this information is valuable as well.
To sum up on this, the "models" folder contains one python program for each of 10 models as well as one generalising program (it predicts the last n match with all 10 models and write the results to the testing tables that are in "testings" folder in excel format; recommendatino to use this big <i>_all.py</i> script rather than specialised scripts for each algorithm - they are not capable of instant writing the result to the tables and are not being updated as <i>_all.py</i> is). Besides, the folder contains all the models-tuning scripts, which I use 2-3 times per season to tune a little hyperparameters of each model, basing on their performance in the last tournaments.

Each model (read: algorithm) counts the bet in 4 different ways - betting strategies. They are rather simple. 
The first one is betting on a predicted winner only if odds on him are not less than 1.50 (if the model predicted that player1 win and odds were 1.3-3.05, the bet size would be 0; if the odds were 1.6-2.1, the bet is the base value - usually 1/10 of the current bank).
The second one is just betting on a predicted winner in all the matches - no limits.
The third can look weird, and it is, but its performance is not worse than others', so I left it among the godd strategies. The key point is it bets on a predicted winner only if odds are not less than 1.5, as the first one, but then, it uses a complex formula to count the bet (I won't write it here, but roughly the bet is higher if the odds on a predicted winner are higher and vice versa).
The fourth one looks the most sensible - the bet is higher if the probability (given by the model) that the predicted winner would win the match is high and vice versa. And, I should say it really shows a stable good performance, even though the profit is not the highest.

Let's now switch to features.
36 different columns in Data excel tables are giving 20 features in the output. From the obvious ones, like ATP Ranking of the players, surface, winning percentage etc., to some constructed by me during the process, like elo ranking of the player (see Wikipedia for more details) which I consider as the great idea, aces and break points percentage, serve-winning percentage etc. As for such an amount of training set for each match, more features would probably kill the accuracy of the models. During the process also, some features were thrown away as insufficient and some were taken into consideration because of they improving the accuracy and profit relatively strongly.

The good question is where I get all the data. 
Such statistics of all matches are open for all on the official ATP World Tour page, so after every matchday I just use "helping/servestats.py" script to get that bunch of data (don't mind the script name, it is a long history). Another part of data involves betting odds - I just get them manually from the tennisexplorer.com page (yeah, manually...but believe, there is a little problem). Lastly, elo rankings which can't be get from the Internet, as I started counting it only from the beginning of 2017. So I maintain elo_rankings tables in Data directory - not just general elo rankings but also at each surface separately. Using "helping/elo.py" script you can recount and update elo rankings after each matchday.

----------------------------------------------------------------------------------------------------------------------------------------

I think all the main points of the project are explained, now we can move to some details.
Besides already mentioned scripts, in the helping folder you can find also day_end.py and bank_or_profit.py scripts, which exist just to make our life easier and automatize some computations and fillings up in the testings tables. day_end.py counts the overall profit in the current day for all 4 betting methods and add this to the bank through the current tournament if needed. bank_or_profit.py is used just for filling up all the tables with the starting bank at the beginning of the tournament or counting up the overall profit for each in the end of the tournament. 
Temp folder is created just for the sake of data safety. One misclick and any script may mess up all the valuable data in elo_ranking tables or <i>'_simple'</i> tables...
The last detail is "evaluation" table in the testings directory. There are some approximate rankings of the algorithms, based on which I am planning to get rid of the worst one in the future (as we can see, this will probably be AdaBoost or its fixed version :)

----------------------------------------------------------------------------------------------------------------------------------------

The sections will be updated whenever I have time and remember some important things about the project.
Good luck!
