# !/usr/bin/env python3

"""
Created by: Curtis Edwards
Created on: June 2023
This is the "CannonBallList" class
"""

from cannon_ball_class import CannonBall

import constants

class CannonBallList:
    def __init__(self):
        self.cannon_balls = []

    def add_to_list(self, cannon_ball):
        self.cannon_balls.append(cannon_ball)

    def is_off_screen(self) -> bool:
        return self.y_position == constants.OFF_SCREEN_Y

    def fire_cannon_ball(self, boat_x_pos: int, boat_y_pos: int, cannon_ball_direction: int):
        for cannon_ball in self.cannon_balls:
            cannon_ball.is_off_screen() == True:
                cannon_ball.x_position = boat_x_pos + cannon_ball_direction
                cannon_ball.y_position = boat_y_pos
                break

    def velocity(self, cannon_ball_speed: int) -> None:
        for cannon_ball in self.cannon_balls:
            cannon_ball.is_off_screen() == False:
            if cannon_ball.is_cannon_ball_left_side() == True:
                cannon_ball.x_position += cannon_ball_speed
            if cannon_ball.is_cannon_ball_left_side() == False:
                cannon_ball.x_position += cannon_ball_speed


"""
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
        """
