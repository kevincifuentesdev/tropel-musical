# Tropel Musical Simulation

[Leer en Español](./README_es.md)

## Authors

- Kevin Sebastián Cifuentes López
- Mariana Lopera Correa
- Emanuel García Ríos

## Description

Tropel Musical is an interactive physics simulation that uses Pygame and Pymunk to model a system of dominoes, ramps, and balls. The goal is to provide a visual and educational experience about how physical interactions work in a simulated environment.

---

## How to Run the Project

### Cloning

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/your-username/tropel-musical.git
   ```

   **Note:** If you want to make changes, please fork the repository and work on your own fork.

### Installing Dependencies

This project uses `poetry` for dependency management. If you don't have `poetry` installed, follow the instructions in the [official Poetry documentation](https://python-poetry.org/docs/).

1. Install `poetry` (if you don't have it):

   ```bash
   curl -sSL https://install.python-poetry.org | python3 -
   ```

2. Navigate to the project directory:

   ```bash
   cd tropel-musical
   ```

3. Configure Poetry to create virtual environments inside the project directory:

   ```bash
   poetry config virtualenvs.in-project true
   ```

4. Install the dependencies:

   ```bash
   poetry install --no-root
   ```

### Running the User Interface

1. Activate the `poetry` virtual environment:

   **Note:** Visit the official Poetry page to check how to activate the virtual environment. It is important to activate it to run the project smoothly within your virtual environment using its interpreter. [Environment Activation](https://python-poetry.org/docs/managing-environments/#bash-csh-zsh)

   ```bash
   eval $(poetry env activate)
   ```

2. Run the main file to start the simulation:

   ```bash
   python src/view/gui/tropel_musical_gui.py
   ```

---

## Project Structure

The project structure is as follows:

```bash
tropel-musical/
├── README.md
├── poetry.lock
├── pyproject.toml
├── src/
│   ├── model/
│   │   └── tropel_musical_model.py
│   ├── view/
│   │   └── gui/
│   │       └── tropel_musical_gui.py
```

- **README.md**: Project documentation.
- **poetry.lock** and **pyproject.toml**: `poetry` configuration files for dependency management.
- **src/**: Main source code folder.
  - **model/**: Contains the logic for the physical model.
  - **view/gui/**: Contains the graphical user interface.

---

## Code Explanation

### `tropel_musical_model.py`

This file contains the main functions to create the physical elements of the simulation:

- **`create_boundaries`**: Defines the boundaries of the physical space.
- **`create_ball`**: Creates a ball with specific physical properties.
- **`create_table`**: Generates a static table in the space.
- **`create_ramps`**: Creates a series of alternating ramps.
- **`create_domino`**: Generates a domino with physical properties.

### `tropel_musical_gui.py`

This file contains the logic for the graphical interface and the main program loop:

- **`draw`**: Draws the physical elements in the Pygame window.
- **`ball_hits_domino`**: Handles collisions between the ball and the dominoes.
- **`create_dominoes`**: Creates a row of dominoes in the space.
- **`run`**: Runs the main loop, handling events and updating the simulation.

With this structure, the project combines physical logic with an interactive graphical interface to simulate a dynamic system of objects.

---

## License

This project is licensed under the MIT License. For more details, see the [LICENSE](./LICENSE) file.
