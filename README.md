# Snake-AI
Self learning snake game using genetic algorithms.

## Installation

Required:
* python 3.8
* pipenv

1. Create virtual environment(recommended) `pipenv shell`
2. Install packages `pipenv install` if you want developer packages type `pipenv install --dev`
3. Run game by typing `python game.py`

## Documentation

Documentation can be found in `docs/` folder. To open browser version type `mdkdocs serve` on documentation will be available on `localhost:8000/`
All logic is inside `app` package. `test` directory is responsible for asserting whether program works as expected.

## Game rules
- Snake dies whenever it hits the wall or itself

## Useful commands
- `pipenv shell` - start virtual environment (pipenv package required)
- `pipenv install --dev` - install required packages with included developer ones
- `python app/game.py` - start game
- `pytest tests/` - run tests
- `mkdocs serve` - open documentation server
