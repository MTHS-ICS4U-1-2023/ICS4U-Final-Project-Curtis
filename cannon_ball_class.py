# !/usr/bin/env python3

"""
Created by: Curtis Edwards
Created on: June 2023
This is the "CannonBall" class
"""

from images import Images

import constants

class CannonBall(Images):
    def __init__(self, _x_position: int, _y_position: int):
        super().__init__(_x_position, _y_position)


    def is_cannon_ball_left_side(self) -> bool:
        return self.x_position < 74
