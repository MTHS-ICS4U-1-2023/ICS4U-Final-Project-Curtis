# !/usr/bin/env python3

"""
Created by: Curtis Edwards
Created on: June 2023
This program is the "Pirate Shooter" program on the PyBadge
"""

from boat_class import Boat
from cannon_ball_class import CannonBall
from cannon_ball_list_class import CannonBallList
from pirate_ship_class import PirateShip
from pirate_ship_list_class import PirateShipList

import random
import time

import constants
import stage
import supervisor
import ugame


def splash_scene():
    """
    This function is the splash_scene
    """

    # get sound ready
    coin_sound = open("coin.wav", "rb")
    sound = ugame.audio
    sound.stop()
    sound.mute(False)
    # sound.play(coin_sound)
    
    # image banks for CircuitPython
    image_bank_mt_background = stage.Bank.from_bmp16("mt_game_studio.bmp")

    # set the background to image 0 in the image bank
    # and the size (10x8 tiles of size 16x16)
    background = stage.Grid(image_bank_mt_background, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y)
    
    # used this program to split the image into tile: 
    #   https://ezgif.com/sprite-cutter/ezgif-5-818cdbcc3f66.png
    background.tile(2, 2, 0)  # blank white
    background.tile(3, 2, 1)
    background.tile(4, 2, 2)
    background.tile(5, 2, 3)
    background.tile(6, 2, 4)
    background.tile(7, 2, 0)  # blank white

    background.tile(2, 3, 0)  # blank white
    background.tile(3, 3, 5)
    background.tile(4, 3, 6)
    background.tile(5, 3, 7)
    background.tile(6, 3, 8)
    background.tile(7, 3, 0)  # blank white

    background.tile(2, 4, 0)  # blank white
    background.tile(3, 4, 9)
    background.tile(4, 4, 10)
    background.tile(5, 4, 11)
    background.tile(6, 4, 12)
    background.tile(7, 4, 0)  # blank white

    background.tile(2, 5, 0)  # blank white
    background.tile(3, 5, 0)
    background.tile(4, 5, 13)
    background.tile(5, 5, 14)
    background.tile(6, 5, 0)
    background.tile(7, 5, 0)  # blank white

    # create a stage for the background to show up on
    # and set the frame rate to 60fps
    game = stage.Stage(ugame.display, constants.FPS)

    # set all layers of all sprites, items show up in order
    game.layers = [background]

    # render all sprites
    # most likely you will only render the background once per game scene
    game.render_block()

    # repeat forever, game loop
    while True:
        # wait for 2 seconds
        time.sleep(2.0)
        menu_scene()


def menu_scene():
    """
    this function is the menu_scene
    """

    # image banks for CircuitPython
    image_bank1 = stage.Bank.from_bmp16("mt_game_studio.bmp")
    image_bank2 = stage.Bank.from_bmp16("pirate_shooter.bmp")

    # add text objects
    text = []
    text1 = stage.Text(width=29, height=12, font=None, palette=constants.WHITE_BLACK_PALETTE, buffer=None)
    text1.move(10, 10)
    text1.text("PIRATE SHOOTER")
    text.append(text1)
    
    text2 = stage.Text(width=29, height=12, font=None, palette=constants.RED_PALETTE, buffer=None)
    text2.move(10, 90)
    text2.text("SELECT: rules")
    text.append(text2)

    text3 = stage.Text(width=29, height=12, font=None, palette=constants.RED_PALETTE, buffer=None)
    text3.move(10, 110)
    text3.text("START: start game")
    text.append(text3)

    # set the background to image 0 in the image bank
    # and the size (10x8 tiles of size 16x16)
    background = stage.Grid(image_bank1, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y)
    water = stage.Grid(image_bank2, 10, 4)

    boat = stage.Sprite(image_bank2, 1, 74, 56)

    # create a stage for the background to show up on
    # and set the frame rate to 60fps
    game = stage.Stage(ugame.display, constants.FPS)

    # set all layers of all sprites, items show up in order
    game.layers = text + [boat] + [water] + [background]

    # render all sprites
    # most likely you will only render the background once per game scene
    game.render_block()

    # repeat forever, game loop
    while True:
        # get user input
        keys = ugame.buttons.get_pressed()
        
        if keys & ugame.K_START != 0:
            game_scene()

        if keys & ugame.K_SELECT != 0:
            game_rules()

        # redraw sprites
        game.tick()


def game_rules():
    """
    this function is the game_rules
    """

    # image banks for CircuitPython
    image_bank = stage.Bank.from_bmp16("mt_game_studio.bmp")

    # add text objects
    text = []
    text1 = stage.Text(width=29, height=12, font=None, palette=constants.BLUE_PALETTE, buffer=None)
    text1.move(10, 10)
    text1.text(
        "-Up and Down to\nmove.\n" +
        "-A and B to shoot.\n" +
        "-Player can warp\nbetween edges of\nthe screen.\n" +
        "-If a projectile\nmisses, youlose\na point.\n"
    )
    text.append(text1)

    text2 = stage.Text(width=29, height=12, font=None, palette=constants.RED_PALETTE, buffer=None)
    text2.move(10, 110)
    text2.text("PRESS START")
    text.append(text2)

    # set the background to image 0 in the image bank
    # and the size (10x8 tiles of size 16x16)
    background = stage.Grid(image_bank, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y)


    # create a stage for the background to show up on
    # and set the frame rate to 60fps
    game = stage.Stage(ugame.display, constants.FPS)

    # set all layers of all sprites, items show up in order
    game.layers = text + [background]

    # render all sprites
    # most likely you will only render the background once per game scene
    game.render_block()

    # repeat forever, game loop
    while True:
        # get user input
        keys = ugame.buttons.get_pressed()
        
        if keys & ugame.K_START != 0:
            game_scene()

        # redraw sprites
        game.tick()


def game_scene():
    """
    This function is for the main game
    """
    
    # for score
    score = 0
    
    score_text = stage.Text(width=29, height=14)
    score_text.clear()
    score_text.cursor(0, 0)
    score_text.move(1, 1)
    score_text.text("Score: {0}".format(score))

    # image banks for CircuitPython
    image_bank = stage.Bank.from_bmp16("pirate_shooter.bmp")

    # buttons that you want to keep state information on
    a_button = constants.button_state["button_up"]
    b_button = constants.button_state["button_up"]
    start_button = constants.button_state["button_up"]
    select_button = constants.button_state["button_up"]

    # get sound ready
    cannon_sound = open("player_cannon.wav", "rb")
    pirate_boom = open("pirate_explosion.wav", "rb")
    """sound = ugame.audio
    sound.stop()
    sound.mute(False)"""

    # set the background to image 0 in the image bank
    # and the size (10x8 tiles of size 16x16)
    background = stage.Grid(image_bank, 10, 8)

    boat = stage.Sprite(image_bank, 1, 74, 56)
    boat_object = Boat(74, 56)

    # create list of pirateships,for both the left and right side
    pirateships = []
    pirateship_objects = PirateShipList()

    for pirateship_number in range(constants.TOTAL_NUMBER_OF_RIGHT_PIRATES):
        a_single_pirateship = stage.Sprite(image_bank, 3, constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)

        pirateships.append(a_single_pirateship)
        a_pirateship_object = PirateShip(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y, "right")
        pirateship_objects.add_to_list(a_pirateship_object)

    for pirateship_number in range(constants.TOTAL_NUMBER_OF_LEFT_PIRATES):
        a_single_pirateship = stage.Sprite(image_bank, 4, constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)

        pirateships.append(a_single_pirateship)
        a_pirateship_object = PirateShip(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y, "left")
        pirateship_objects.add_to_list(a_pirateship_object)
    
    # place 2 pirateships on the screen
    pirateship_objects.spawn_pirateship_right()
    pirateship_objects.spawn_pirateship_left()
    
    # create list of cannonballs for when we shoot
    cannonballs = []
    cannonball_objects = CannonBallList()

    for cannon_ball_number in range(constants.TOTAL_NUMBER_OF_CANNONBALLS):
        a_single_cannon_ball = stage.Sprite(image_bank, 2, constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
        cannonballs.append(a_single_cannon_ball)

        a_cannon_ball_object = CannonBall(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
        cannonball_objects.add_to_list(a_cannon_ball_object)

    # create a stage for the background to show up on
    # and set the frame rate to 60fps
    game = stage.Stage(ugame.display, 60)

    # set all layers of all sprites, items show up in order
    game.layers = [score_text] + pirateships + [boat] + cannonballs + [background]

    # render all sprites
    # most likely you will only render the background once per game scene
    game.render_block()

    # repeat forever, game loop
    while True:
        # get user input
        keys = ugame.buttons.get_pressed()
        
        if keys & ugame.K_X:
            if a_button == constants.button_state["button_up"]:
                a_button = constants.button_state["button_just_pressed"]
            elif a_button == constants.button_state["button_just_pressed"]:
                a_button = constants.button_state["button_still_pressed"]
        else:
            if a_button == constants.button_state["button_still_pressed"]:
                a_button = constants.button_state["button_released"]
            else:
                a_button = constants.button_state["button_up"]

        if keys & ugame.K_O:
            if b_button == constants.button_state["button_up"]:
                b_button = constants.button_state["button_just_pressed"]
            elif b_button == constants.button_state["button_just_pressed"]:
                b_button = constants.button_state["button_still_pressed"]
        else:
            if b_button == constants.button_state["button_still_pressed"]:
                b_button = constants.button_state["button_released"]
            else:
                b_button = constants.button_state["button_up"]

        if keys & ugame.K_UP:
            if boat.y > constants.OFF_TOP_SCREEN:
                boat_object.velocity(-constants.BOAT_SPEED)
                boat.move(boat_object.x_pos, boat_object.y_pos)
            else:
                boat_object.warp_bottom()
                boat.move(boat_object.x_pos, boat_object.y_pos)

        if keys & ugame.K_DOWN:
            if boat.y < constants.OFF_BOTTOM_SCREEN:
                boat_object.velocity(constants.BOAT_SPEED)
                boat.move(boat_object.x_pos, boat_object.y_pos)
            else:
                boat_object.warp_top()
                boat.move(boat_object.x_pos, boat_object.y_pos)

        # Update the position of each sprite based on the corresponding CannonBall object
        for cannon_ball_counter, cannon_ball in enumerate(cannonball_objects.cannon_balls):
            cannonballs[cannon_ball_counter].move(cannon_ball.x_pos, cannon_ball.y_pos)

        for pirate_ship_counter, pirate_ship in enumerate(pirateship_objects.pirate_ships):
            pirateships[pirate_ship_counter].move(pirate_ship.x_pos, pirate_ship.y_pos)

        # update game logic
        if a_button == constants.button_state["button_just_pressed"]:
            cannonball_objects.fire_cannon_ball(boat_object.x_pos, boat_object.y_pos, -1)

        if b_button == constants.button_state["button_just_pressed"]:
            cannonball_objects.fire_cannon_ball(boat_object.x_pos, boat_object.y_pos, 1)
        
        cannonball_objects.velocity(constants.CANNONBALL_SPEED)

        pirateship_objects.velocity(constants.PIRATE_SPEED)

        if cannonball_objects.is_cannon_ball_off_screen():
            score -= 1
            if score < 0:
                score = 0
            score_text.clear()
            score_text.cursor(0, 0)
            score_text.move(1, 1)
            score_text.text(f"Score: {score:.0f}")

        if pirateship_objects.is_cannon_ball_colliding(cannonball_objects):
            sound.stop()
            # sound.play(pirate_boom)
            score += 1
            score_text.clear()
            score_text.cursor(0, 0)
            score_text.move(1, 1)
            score_text.text(f"Score: {score:.0f}")

        if pirateship_objects.is_boat_colliding(boat_object):
            # sound.stop()
            # sound.play(pirate_boom)
            time.sleep(2.0)
            game_over_scene(score)

        # redraw sprites
        game.render_sprites(pirateships + [boat] + cannonballs)
        game.tick()


def game_over_scene(final_score: int):
    # this function is the game over scene

    # turn off sound from last scene
    sound = ugame.audio
    sound.stop()

    # image banks for CircuitPython
    image_bank_mt_background = stage.Bank.from_bmp16("mt_game_studio.bmp")

    # set the background to image 0 in the image bank
    # and the size (10x8 tiles of size 16x16)
    background = stage.Grid(
        image_bank_mt_background, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y
    )

    # add text objects
    text = []
    text1 = stage.Text(
        width=29, height=14, font=None, palette=constants.BLUE_PALETTE, buffer=None
    )

    text1.move(22, 20)
    text1.text(f"Final Score: {final_score:.0f}")
    text.append(text1)

    text2 = stage.Text(
        width=29, height=14, font=None, palette=constants.RED_PALETTE, buffer=None
    )

    text2.move(43, 60)
    text2.text("GAME OVER")
    text.append(text2)

    text3 = stage.Text(
        width=29, height=14, font=None, palette=constants.BLUE_PALETTE, buffer=None
    )

    text3.move(32, 110)
    text3.text("PRESS SELECT")
    text.append(text3)

    # create a stage for the background to show up on
    # and set the frame rate to 60fps
    game = stage.Stage(ugame.display, constants.FPS)

    # set all layers of all sprites, items show up in order
    game.layers = text + [background]

    # render all sprites
    # most likely you will only render the background once per game scene
    game.render_block()

    # repeat forever, game loop
    while True:
        # wait for 2 seconds
        keys = ugame.buttons.get_pressed()

        # get user input
        if keys & ugame.K_SELECT != 0:
            supervisor.reload()

        # update game logic
        game.tick()  # wait until refresh rate finishes


if __name__ == "__main__":
    splash_scene()