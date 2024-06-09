# !/usr/bin/env python3

"""
Created by: Curtis Edwards
Created on: June 2023
This is the "PirateShip" class
"""

import constants
import random

class PirateShip:
    def __init__(self, _x_position: int, _y_position: int, _screen_side: str):
        self.x_position = _x_position
        self.y_position = _y_position
        self.screen_side = _screen_side

    # Getter for x_position
    @property
    def x_pos(self) -> int:
        return self.x_position

    # Getter for y_position
    @property
    def y_pos(self) -> int:
        return self.y_position

    # Getter for y_position
    @property
    def spawn_side(self) -> str:
        return self.screen_side

    # Setter for x_position
    @x_pos.setter
    def x_pos(self, value: int):
        self.x_position = value

    # Setter for y_position
    @y_pos.setter
    def y_pos(self, value: int):
        self.y_position = value

    def is_pirate_ship_left_side(self) -> bool:
        return self.screen_side == "left"

    def is_off_screen(self) -> bool:
        return self.y_position == constants.OFF_SCREEN_Y

    def is_out_of_bounds(self) -> bool:
        return (self.x_position > constants.SCREEN_X) or (self.x_position < -16)

    def move_off_screen(self):
        self.x_position = constants.OFF_SCREEN_X
        self.y_position = constants.OFF_SCREEN_Y
