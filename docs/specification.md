# Game specification

Modules and its interfaces are described here 



## Snake
filename: `app/snake.py`

class: `Snake`

attributes

- `alive` - boolean flag that tells whether snake is alive
- `_speed` - enum value which specify speed mode
- `_nodes` - list of `Node` class objects which are "items" that snake is build upon
- `_window_size` - game window width and height in pixels, that is needed to check whether snake is still on allowed board

actions

- move()
- eat()
- check_collision()
- check_food_collision()

* `app/snake.py` - Logic for snake that is build from `nodes`.
* `app/food.py` - Module responsible for generating and redrawing food which is single `node`.
* `app/node.py` - The unit upon which other game instances like snake, food are build.
