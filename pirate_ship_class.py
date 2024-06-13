# !/usr/bin/env python3

"""
Created by: Curtis Edwards
Created on: June 2023
This is the "PirateShip" class
"""

from images import Images

import constants
import random

class PirateShip(Images):
    def __init__(self, _x_position: int, _y_position: int, _screen_side: str):
        super().__init__(_x_position, _y_position)
        self.screen_side = _screen_side

    # Getter for y_position
    @property
    def spawn_side(self) -> str:
        return self.screen_side


    def is_pirate_ship_left_side(self) -> bool:
        return self.screen_side == "left"
