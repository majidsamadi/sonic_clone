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
   git clone https://github.com/yourusername/sonic-clone-game.git
   cd sonic-clone-game

3. **Install Dependencies:"

   ```bash
    pip install -r requirements.txt

4. **Run the Game:"

   ```bash
    pip install -r requirements.txt


### 4. **How to Play**

Explain how users can interact with the game.

```md
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
   - Used for managing Sonic's different states like `Idle`, `Running`, and `Jumping`.
   - Example: `IdleState`, `RunningState`, and `JumpingState` classes in `state.py`.

2. **Strategy Pattern:**
   - Employed for handling different movement behaviors.
   - Example: `FacingLeftState` and `FacingRightState` in `direction_state.py`.

3. **Observer Pattern:**
   - Used for managing game events, such as collisions between Sonic and enemies.
   - Example: `Observer` and `Subject` classes in `observer.py`.

4. **Command Pattern:**
   - Implemented for handling input commands, such as moving left, right, or jumping.
   - Example: `MoveLeftCommand`, `MoveRightCommand`, and `JumpCommand` classes in `command.py`.

5. **Factory Pattern:**
   - Used to create enemies and collectibles at runtime.
   - Example: `EnemyFactory` and `CollectibleFactory` classes in `factory.py`.

6. **Template Method Pattern:**
   - Applied to define the steps for loading different levels.
   - Example: `LevelState` and its subclasses in `level_state.py`.

## SOLID Principles

The game is designed with SOLID principles in mind:

1. **Single Responsibility Principle:**
   - Each class has a single responsibility, like handling Sonic's states, managing inputs, or controlling the game loop.

2. **Open/Closed Principle:**
   - The game is designed to be extendable. For example, adding a new level only requires creating a new subclass of `LevelState`.

3. **Liskov Substitution Principle:**
   - Subclasses can be substituted for their base classes without affecting the functionality. For example, different types of enemies are interchangeable in the game.

4. **Interface Segregation Principle:**
   - Interfaces are designed to be specific to the clients' needs. For example, separate interfaces for `Collectible` and `Enemy`.

5. **Dependency Inversion Principle:**
   - High-level modules are not dependent on low-level modules. Abstractions are used to manage dependencies between classes.

## Purpose of This Game

This game was developed as a demonstration of my software development skills, specifically to showcase proficiency in Object-Oriented Programming (OOP), design patterns, and adherence to SOLID principles. The primary goal of this project is to illustrate the ability to create clean, maintainable, and scalable code through the application of best practices in software design.

This game does not include any narrative or story and is solely intended to serve as a technical demonstration.
