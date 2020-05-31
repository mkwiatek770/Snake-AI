# Welcome to SnakeAI

## Project description


## Commands

* `pipenv shell` - start virtual environment (pipenv package required)
* `pipenv install --dev` - install required packages with included developer ones
* `python app/game.py` - start game
* `pytest tests/` - run tests
* `mkdocs serve` - open documentation server

## Project layout

    mkdocs.yml    # Documentation configuration
    Pipfile       # List of packages
    Pipfile.lock 
    README.md
    app/          # Main game package, all business logic is in here
        snake.py
        node.py
        food.py
        utils.py
        game.py
    tests/ 
    docs/         # Documentation can be found here
