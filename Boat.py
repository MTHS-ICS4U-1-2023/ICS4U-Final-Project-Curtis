# !/usr/bin/env python3

"""
Created by: Curtis Edwards
Created on: June 2023
This is the "Boat" class
"""

import constants

class Boat:
    def __init__(self, x_position: int, y_position: int):
        self._x_position = x_position
        self._y_position = y_position

    # Getter for x_position
    @property
    def x_position(self) -> int:
        return self._x_position

    # Getter for y_position
    @property
    def y_position(self) -> int:
        return self._y_position

    # Setter for y_position
    @y_position.setter
    def y_position(self, value: int):
        self._y_position = value

    # Method to change the boat's velocity
    def velocity(self, boat_speed: int) -> None:
        self._y_position += boat_speed


"""
    def is_colliding(sprite1, sprite2) -> bool:
        # Implement the logic to determine if two sprites are colliding
        pass

    def collision(self, sprite) -> bool:
        # Implement the logic to handle collision with another sprite
        pass

    def is_off_screen(self, stage) -> bool:
        # Implement the logic to determine if the sprite is off screen
        pass
"""