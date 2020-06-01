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

## Food
filename: `app/food.py`

attributes

- `x` - width coordinate
- `y` - height coordinate

## Node
filename: `app/node.py`

attributes and properties

- `x` - width coordinate
- `y` - height coordinate
- `direction` - enum with one of possible direction (UP, DOWN, LEFT, RIGHT)
- `_turns` - list of Node objects which are list of specific node directions LIFO structure
- `turns` - property which returns list of turn.
- `next_turn` - return soonest turn

actions
- `has_turns()` - boolean that tells whether node has any following turns
- `add_turn()` - add turn at the end of queue (LIFO)
- `turn()` - make turn which means - remove fist element from list.
