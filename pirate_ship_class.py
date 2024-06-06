# !/usr/bin/env python3

"""
Created by: Curtis Edwards
Created on: June 2023
This is the "PirateShip" class
"""

import constants
import random

class PirateShip:
    def __init__(self, x_position: int, y_position: int):
        self._x_position = x_position
        self._y_position = y_position

    # Getter for x_position
    @property
    def x_pos(self) -> int:
        return self._x_position

    # Getter for y_position
    @property
    def y_pos(self) -> int:
        return self._y_position

    # Getter for y_position
    @property
    def screen_side(self) -> str:
        return self._screen_side

    # Setter for x_position
    @x_pos.setter
    def x_pos(self, value: int):
        self._x_position = value

    # Setter for y_position
    @y_pos.setter
    def y_pos(self, value: int):
        self._y_position = value

    def is_off_screen(self) -> bool:
        return self._y_position == constants.OFF_SCREEN_Y

    def is_out_of_bounds(self) -> bool:
        return (self._x_position > constants.SCREEN_X) or (self._x_position < -16)

    def spawn_pirateship_right(self):
        self._x_position = constants.OFF_RIGHT_SCREEN
        self._y_position = random.randint(0, (constants.SCREEN_Y - constants.SPRITE_SIZE))

    def spawn_pirateship_left(self):
        self._x_position = constants.OFF_LEFT_SCREEN
        self._y_position = random.randint(0, (constants.SCREEN_Y - constants.SPRITE_SIZE))


    def velocity(self, pirate_speed: int) -> None:
        self._x_position += pirate_speed

    def move_off_screen(self):
        self._x_position = constants.OFF_SCREEN_X
        self._y_position = constants.OFF_SCREEN_Y
