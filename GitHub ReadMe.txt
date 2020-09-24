Hello,
My name is Keith Simmons and I am a Data Sciences student at the Pennsylvania State University.  This is a repository of Python programming projects that I have worked on in my spare time using the help of internet resources to improve my working knowledge of Python.


Programs:


Games: 


AsteroidTest.py: A recreation of the old-school, arcade game Asteroids.  Utilizes the pygame library and object-oriented programming.  Some errors still occur and hyperdrive is not added, but mostly working.


BallGameDist.py: Easy game created using the turtle library in Python.  Users have to move around the screen to collect the moving targets.  Serves as an introduction to programming games.


Flappy.py: A recreation of the hit mobile game, Flappy Bird.  This program utilizes object oriented programming along with the pygame library.  It is very basic with no sprites, no score counting feature, or any way to lose.  However, it has all the functionalities to add these features later (hit detection works), but I plan on using this program as a test for evolutionary algorithms under machine learning.






Analysis:


CatanBestPlaceMulti.py: This program was made after a session of playing the strategic, board game Catan with my friends.  To begin the game, players must choose locations for the initial two settlements in a snaking order, i.e. first player places their settlements first and last, second player places their settlements second and second to last, and so on.  Each location is adjacent to resource tiles that give the player a corresponding resource if the number on the tile is rolled (by dice).  This program simulates the opening round of Catan many times in order to determine which position is best to pick in regarding the likelihood of rolling an adjacent tile.  This program utilizes object oriented programming and the matplotlib library in doing so.
(Hint: the first player is best off, while the last player is worse off.)


PSURedditWebScraper.py: Program used to mine data about the top 25 posts on the Penn State subreddit on Reddit.  Current functionality is to plot time vs. amount of upvotes and fit some function, but this is done with standard regression techniques.  I will revisit this program once I am finished taking my Applied Time Series Analysis course at Penn State.  Utilizes requests, matplotlib, pandas, and BeautifulSoup libraries to perform the tasks.


Pinochle.py: One of my programs in a series of programs analyzing the point distributions in the card card Pinochle.  These programs focus on four player Pinochle, as I usually play four player Pinochle with my family.  With these programs, I was able to determine the distribution of the amount of initial points in players’ hands.  This is very useful in a game like Pinochle where you have to make educated predictions on the points held by other players.  These programs utilize the matplotlib and seaborn libraries to visualize the data.






Machine Learning:


BetterColorBW.py: Probably the most complex of any of my programs thus far.  Applies the NNFunc.py that I have created to determine if white or black text should be used on a specifically colored background.  The program asks the user to input whether the black or white text looks better on the background and also produces a prediction to what color text would be best.  The program learns from the user input and will make better guesses with the more input that the user provides.  Could also be used with labelled input if that is available.  This program was a practice for both my machine learning skills and the pygame library.


LineGuess.py:  Solves a simple binary classification problem using machine learning.  Separates points on a plane via some arbitrary line and then the program tries to find that line using machine learning techniques.


NNFunc.py: My three layer neural network class.  Instances of the class can be used to create neural networks with an amount of nodes specified by the instance of the class.  This is the class used in the BetterColorBW.py.