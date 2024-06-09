# !/usr/bin/env python3

"""
Created by: Curtis Edwards
Created on: June 2023
This is the "PirateShipList" class
"""

from pirate_ship_class import PirateShip

import constants
import random
import stage
import ugame

class PirateShipList:
    def __init__(self):
        self.pirate_ships = []

    def add_to_list(self, pirate_ship):
        self.pirate_ships.append(pirate_ship)

    def spawn_pirateship(self):
        random_side = random.choice(["right", "left"])
        if random_side == "right":
            self.spawn_pirateship_right()
        else:
            self.spawn_pirateship_left()

    def spawn_pirateship_right(self):
        for pirate_ship in self.pirate_ships:
            if not pirate_ship.is_pirate_ship_left_side():
                if pirate_ship.is_off_screen():
                    pirate_ship.x_position = constants.OFF_RIGHT_SCREEN
                    pirate_ship.y_position = random.randint(0, (constants.SCREEN_Y - constants.SPRITE_SIZE))
                    break

    def spawn_pirateship_left(self):
        for pirate_ship in self.pirate_ships:
            if pirate_ship.is_pirate_ship_left_side():
                if pirate_ship.is_off_screen():
                    pirate_ship.x_position = constants.OFF_LEFT_SCREEN
                    pirate_ship.y_position = random.randint(0, (constants.SCREEN_Y - constants.SPRITE_SIZE))
                    break

    def velocity(self, pirate_ship_speed: int) -> None:
        for pirate_ship in self.pirate_ships:
            if not pirate_ship.is_off_screen():
                if not pirate_ship.is_pirate_ship_left_side():
                    pirate_ship.x_position -= pirate_ship_speed
                elif pirate_ship.is_pirate_ship_left_side():
                    pirate_ship.x_position += pirate_ship_speed

                if pirate_ship.is_out_of_bounds():
                    pirate_ship.move_off_screen()
                    self.spawn_pirateship()

    def is_cannon_ball_colliding(self, cannonball_objects) -> bool:
        game = stage.Stage(ugame.display, 60)
        for cannon_ball in cannonball_objects.cannon_balls:
            for pirate_ship in self.pirate_ships:
                if (not cannon_ball.is_off_screen() and not pirate_ship.is_off_screen() and
                    stage.collide(
                        cannon_ball.x_pos + 4, cannon_ball.y_pos + 4, cannon_ball.x_pos + 12, cannon_ball.y_pos + 12,
                        pirate_ship.x_pos, pirate_ship.y_pos, pirate_ship.x_pos + 16, pirate_ship.y_pos + 16,
                    )
                ):
                    cannon_ball.move_off_screen()
                    pirate_ship.move_off_screen()
                    self.spawn_pirateship()
                    self.spawn_pirateship()
                    return True
        return False

    def is_boat_colliding(self, boat_object) -> bool:
        game = stage.Stage(ugame.display, 60)
        for pirate_ship in self.pirate_ships:
            if (not pirate_ship.is_off_screen() and
                stage.collide(
                pirate_ship.x_pos + 1, pirate_ship.y_pos + 1, pirate_ship.x_pos + 15, pirate_ship.y_pos + 15,
                boat_object.x_pos + 6, boat_object.y_pos + 3, boat_object.x_pos + 10, boat_object.y_pos + 13,
                )
            ):
                return True
        return False


