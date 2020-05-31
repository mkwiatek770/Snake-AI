# Snake-AI
Self learning snake game using genetic algorithms.

## Components

All logic is inside `app` package. `test` directory is responsible for asserting whether program works as expected.

* `app/game.py` - Main executable file. All components from other files are imported here.

class **Snake**

attributes

- 

actions

- move
- eat
- check_collision
- check_food_collision

* `app/snake.py` - Logic for snake that is build from `nodes`.
* `app/food.py` - Module responsible for generating and redrawing food which is single `node`.
* `app/node.py` - The unit upon which other game instances like snake, food are build.

## Game rules
- Snake dies whenever it hits the wall or itself

## Useful commands
`python app/game.py` - start game
`pytest tests/` - run tests
