# !/usr/bin/env python3

"""
Created by: Curtis Edwards
Created on: June 2023
This is the "Boat" class
"""

from images import Images

import constants

class Boat(Images):
    def __init__(self, _x_position: int, _y_position: int):
        super().__init__(_x_position, _y_position)


    def velocity(self, boat_speed: int) -> None:
        self.y_position += boat_speed

    def warp_bottom(self) -> None:
        self.y_position = constants.OFF_BOTTOM_SCREEN

    def warp_top(self) -> None:
        self.y_position = constants.OFF_TOP_SCREEN
