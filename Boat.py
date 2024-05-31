# !/usr/bin/env python3

"""
Created by: Curtis Edwards
Created on: June 2023
This is the "Boat" class
"""

class Images:
    def __init__(self, x_position: int, y_position: int, sprite_image: str):
        self._x_position = x_position
        self._y_position = y_position
        self._sprite_image = sprite_image

    # Getters
    def x_position(self) -> int:
        return self._x_position

    def y_position(self) -> int:
        return self._y_position

    def sprite_image(self) -> str:
        return self._sprite_image

    # Setters
    def x_position(self, value: int):
        self._x_position = value

    def y_position(self, value: int):
        self._y_position = value

    # Methods
    def velocity(self) -> int:
        # Implement the logic to calculate velocity
        pass

    def is_colliding(sprite1, sprite2) -> bool:
        # Implement the logic to determine if two sprites are colliding
        pass

    def collision(self, sprite) -> bool:
        # Implement the logic to handle collision with another sprite
        pass

    def is_off_screen(self, stage) -> bool:
        # Implement the logic to determine if the sprite is off screen
        pass
