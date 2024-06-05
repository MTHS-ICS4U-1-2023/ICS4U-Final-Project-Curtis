# !/usr/bin/env python3

"""
Created by: Curtis Edwards
Created on: June 2023
This is the "CannonBall" class
"""

import constants

class CannonBall:
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

    # Setter for x_position
    @x_pos.setter
    def x_pos(self, value: int):
        self._x_position = value

    # Setter for y_position
    @y_pos.setter
    def y_pos(self, value: int):
        self._y_position = value

    def is_off_screen(self) -> bool:
        return self._x_position == constants.OFF_SCREEN_X

    def is_cannon_ball_left_side(self) -> bool:
        return self._x_position < 74

    def is_out_of_bounds(self) -> bool:
        return (self._x_position > constants.SCREEN_X) or (self._x_position < -16)

    def fire_cannon_ball(self, boat_x_pos: int, boat_y_pos: int, cannon_ball_direction: int):
        self._x_position = boat_x_pos + cannon_ball_direction
        self._y_position = boat_y_pos

    def velocity(self, cannon_ball_speed: int) -> None:
        self._x_position += cannon_ball_speed

    def move_off_screen(self):
        self._x_position = constants.OFF_SCREEN_X
        self._y_position = constants.OFF_SCREEN_Y
