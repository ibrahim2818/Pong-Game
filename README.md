# Pong-Game
A classic Pong game implemented in Python using the turtle module. This project includes a simple two-player Pong game where players control paddles to hit a ball back and forth, aiming to score points by making the opponent miss the ball.

Features:
Two-player gameplay: One player controls the left paddle using 'w' (up) and 's' (down), and the other player controls the right paddle using the up and down arrow keys.
Scorekeeping: A scoreboard keeps track of each player's score.
Ball physics: The ball bounces off the paddles and the top and bottom walls. The game speed increases each time the ball hits a paddle, adding a challenge.
Game reset: The ball resets to the center when a player scores a point.

Code Structure:
main.py: The main game loop and setup.
ball.py: Contains the Ball class which handles ball movement and collision detection.
paddle.py: Contains the Paddle class which handles paddle movement.
scoreboard.py: Contains the Scoreboard class which updates and displays the score.
