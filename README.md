# Sonic Clone Game

This project is a demonstration of my software development skills, showcasing proficiency in Object-Oriented Programming (OOP), design patterns, and adherence to SOLID principles. The game does not include a narrative or story, and its primary purpose is to illustrate best practices in software design and development.

## Table of Contents

- [Installation](#installation)
- [How to Play](#how-to-play)
- [Design Patterns](#design-patterns)
- [SOLID Principles](#solid-principles)
- [Purpose of This Game](#purpose-of-this-game)

## Installation

1. **Install Python:**

   - Download and install Python from the official website: [Python.org](https://www.python.org/downloads/).
   - Make sure to add Python to your system's PATH during installation.

2. **Clone the Repository:**

   ```bash
   git clone https://github.com/majidsamadi/sonic_clone.git
   cd sonic-clone


3. **Run the Game:**

   ```bash
    python main.py



### 4. **How to Play**

Explain how users can interact with the game.

## How to Play

- **Move Sonic:** Use the arrow keys to move Sonic left or right.
- **Jump:** Press the space bar to make Sonic jump.
- **Collect Items:** Move Sonic over the collectibles to pick them up.
- **Avoid Enemies:** Jump over enemies to avoid losing the game.
- **Levels:** Sonic progresses through different levels, each with unique layouts and challenges.

The game restarts automatically if Sonic loses. Enjoy the game!

## Design Patterns

This game demonstrates the following design patterns:

1. **State Pattern:**
   - The `State` pattern is utilized in handling the different states of Sonic (e.g., `IdleState`, `RunningState`, `JumpingState`). Each state encapsulates behavior associated with a particular state of Sonic, and Sonic's behavior changes when its state changes.
   - Example: In the `sonic.py` file, Sonic's movement logic is encapsulated in different state classes. For example, when Sonic is in the RunningState, it handles running animations and movement, while in `JumpingState`, it handles the upward and downward motion of Sonic.

2. **Strategy Pattern:**
   - The `Strategy pattern` is implemented to handle different movement strategies for Sonic's direction (left or right).
   - Example: The `FacingLeftState` and `FacingRightState` classes in the `direction_state.py` file represent different strategies for rendering Sonic's image based on the direction he's facing.

3. **Observer Pattern:**
   - The `Observer` pattern is used for handling events in the game, such as collisions between Sonic and enemies or collectibles.
   - Example: In the `observer.py` file, the observer pattern allows Sonic to notify observers when a particular event, like collision detection, occurs, triggering the appropriate response.

4. **Command Pattern:**
   - The `Command` pattern is used to handle input actions from the player, such as moving Sonic left or right or making him jump.
   - Example: In the `command.py` file, actions like `MoveLeftCommand`, `MoveRightCommand`, and `JumpCommand` encapsulate the request to move Sonic in a specific direction or jump. The `Controller` class in `controller.py` invokes these commands based on user input.

5. **Facade Pattern:**
    - The `Facade` pattern is implemented to provide a simplified interface to the complex subsystem of the game. This pattern allows the game loop to interact with the game objects more easily.
    - Example: The `GameFacade` class in `facade.py` provides a simplified interface to manage Sonic, levels, enemies, and collectibles.

6. **Factory Pattern:**
   - The `Factory` pattern is used for creating instances of objects like levels and enemies.
   - Example: In `factory.py`, the `LevelFactory` and `EnemyFactory` classes are used to encapsulate the creation logic of levels and enemies, allowing easy scalability and separation of concerns.

7. **Template Method Pattern:**
   - The `Template Method` pattern is used to define the skeleton of an algorithm in the `LevelState` base class, while allowing subclasses to define specific steps.
   - Example: In `level_state.py`, the `load_level` method in `LevelState` defines the general workflow of loading a level, while specific levels (e.g., `Level1State`, `Level2State`) override certain steps.


## SOLID Principles

The game is designed with SOLID principles in mind:

1. **Single Responsibility Principle:**
    - **Explanation**: Each class in the game has a single responsibility. For example, the `Sonic` class is responsible only for managing Sonic's attributes and states, while `LevelState` handles the management of level-specific behaviors.
    - **Example**: The `CollectibleInterface` class is solely responsible for defining the interface of collectibles, separating it from the actual game logic.

2. **Open/Closed Principle:**
    - **Explanation**: The game is open for extension but closed for modification. Adding new levels or enemy types can be done without changing existing code.
    - **Example**: To add a new level, you can simply create a new subclass of `LevelState` and implement the required methods. No other part of the game needs to be modified.

3. **Liskov Substitution Principle:**
    - **Explanation**: Objects of a superclass should be replaceable with objects of a subclass without affecting the functionality of the program.
    - **Example**: The `SonicState` subclasses like `IdleState`, `RunningState`, and `JumpingState` can be used interchangeably with Sonic without altering the expected 

4. **Interface Segregation Principle:**
    - **Explanation**: Clients should not be forced to depend on methods they do not use. The game adheres to this principle by providing lean and specific interfaces.
    - **Example**: The `CollectibleInterface` only defines the methods that are necessary for a collectible to function, separating concerns and ensuring that subclasses only implement what they need.

5. **Dependency Inversion Principle:**
    - **Explanation**: High-level modules should not depend on low-level modules. Both should depend on abstractions.
    - **Example**: The game loop depends on abstract classes like `SonicState`, `LevelState`, and `Controller`, rather than concrete implementations, allowing for greater flexibility and easier modifications.

## Purpose of This Game

This game was developed as a demonstration of my software development skills, specifically to showcase my proficiency in Object-Oriented Programming (OOP) principles, the use of design patterns, and adherence to SOLID principles. The primary goal of this project is to illustrate my ability to create clean, maintainable, and scalable code through the application of best practices in software design.

It is important to note that this game does not include any particular story or narrative. Its sole purpose is to serve as a technical demonstration, showing how a game can be effectively programmed using OOP and design patterns, while fully respecting the SOLID principles.

Throughout the development process, I carefully applied various design patterns to ensure that the game's architecture is both robust and flexible. By following SOLID principles, I aimed to create a codebase that is easy to extend and modify, while minimizing the risk of introducing errors.

This project is not just about creating a game but about demonstrating the thought process, discipline, and technical expertise required to build a well-structured software application. It reflects my commitment to writing high-quality code that adheres to industry standards and best practices.
