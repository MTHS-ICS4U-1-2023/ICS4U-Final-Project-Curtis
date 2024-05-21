# !/usr/bin/env python3

"""
Created by: Curtis Edwards
Created on: June 2023
This program is the "Pirate Shooter" program on the PyBadge
"""

import stage
import ugame


def game_scene():
    """
    This function is for the main game
    """

    # image banks for CircuitPython
    image_bank = stage.Bank.from_bmp16("pirate_shooter.bmp")

    # set the background to image 0 in the image bank
    # and the size (10x8 tiles of size 16x16)
    background = stage.Grid(image_bank, 10, 8)

    boat = stage.Sprite(image_bank, 1, 75, 66)

    # create a stage for the background to show up on
    # and set the frame rate to 60fps
    game = stage.Stage(ugame.display, 60)

    # set all layers of all sprites, items show up in order
    game.layers = [boat] + [background]

    # render all sprites
    # most likely you will only render the background once per game scene
    game.render_block()

    # repeat forever, game loop
    while True:
        # get user input

        # update game logic

        # redraw sprites
        game.render_sprites([boat])
        game.tick()


if __name__== "__main__":
    game_scene()