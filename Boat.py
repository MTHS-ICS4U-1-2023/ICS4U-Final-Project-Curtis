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

    # Method to warp boat to the bottom of the screen
    def warp_bottom(self) -> None:
        self._y_position = constants.OFF_BOTTOM_SCREEN

    # Method to warp boat to the top of the screen
    def warp_top(self) -> None:
        self._y_position = constants.OFF_TOP_SCREEN
