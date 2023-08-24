# Pong Game

Pong is a classic two-player game where each player controls a paddle and tries to bounce a ball back and forth without letting it pass their paddle. This implementation of the Pong game is created using Python and the Turtle graphics library.

## How the Game Works

- The game is played on a black screen, where each player controls a paddle.
- The players can move their paddles up and down to hit the ball.
- The ball moves across the screen, bouncing off the walls and paddles.
- If a player misses the ball and it goes off the screen, the opponent scores a point.
- The player with the highest score wins the game.

## Python Concepts Implemented

### Classes and Inheritance
- The game is organized using classes. Each element (ball, paddles, scores) is represented by a class.
- Inheritance is used to create subclasses that inherit properties and methods from a parent class.

### Encapsulation
- The classes use encapsulation to hide the implementation details and provide a clean interface for interaction.

### Turtle Graphics
- The game utilizes the Turtle graphics library to create the game window, draw elements, and manage user input.

### Object-Oriented Programming (OOP)
- OOP principles are employed to structure the code and manage the game's logic.

### Control Flow
- Loops and conditional statements are used to control the game's flow, such as updating the screen, detecting collisions, and updating scores.

### Event Handling
- The `onkey` function from the Turtle library is used to handle keyboard events and move the paddles.

### Mathematical Calculations
- Mathematical calculations are used to determine the ball's movement, bouncing off walls and paddles.

### Game Mechanics
- Game mechanics, such as updating scores, increasing game speed, and resetting the ball's position, are implemented to create a playable game.

## How to Run the Game

1. Install Python on your system.
2. Clone or download this repository.
3. Open a terminal or command prompt and navigate to the game's directory.
4. Run the main script using the command: `python main.py`

## Controls

- Player 1 (Right Paddle): Use the `Up` and `Down` arrow keys to move the paddle.
- Player 2 (Left Paddle): Use the `W` and `S` keys to move the paddle.

---