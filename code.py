# !/usr/bin/env python3

"""
Created by: Curtis Edwards
Created on: June 2023
This program is the "Pirate Shooter" program on the PyBadge
"""

from Boat import Boat

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
    image_bank = stage.Bank.from_bmp16("mt_game_studio.bmp")

    # add text objects
    text = []
    text1 = stage.Text(width=29, height=12, font=None, palette=constants.RED_PALETTE, buffer=None)
    text1.move(20, 10)
    text1.text("MT Game Studios")
    text.append(text1)
    
    text2 = stage.Text(width=29, height=12, font=None, palette=constants.RED_PALETTE, buffer=None)
    text2.move(40, 110)
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
    
    """def show_pirateships_right():
        # this function takes an pirateship from off the screen and moves it on screen
        for pirateship_number_right in range(len(pirateships_right)):
            if pirateships_right[pirateship_number_right].y == constants.OFF_SCREEN_Y:
                pirateships_right[pirateship_number_right].move(
                    constants.OFF_RIGHT_SCREEN,
                    random.randint(0, (constants.SCREEN_Y - constants.SPRITE_SIZE))
                )
                break

    def show_pirateships_left():
        # this function takes an pirateship from off the screen and moves it on screen
        for pirateship_number_left in range(len(pirateships_left)):
            if pirateships_left[pirateship_number_left].y == constants.OFF_SCREEN_Y:
                pirateships_left[pirateship_number_left].move(
                    constants.OFF_LEFT_SCREEN,
                    random.randint(0, (constants.SCREEN_Y - constants.SPRITE_SIZE))
                )
                break"""

    # image banks for CircuitPython
    image_bank = stage.Bank.from_bmp16("pirate_shooter.bmp")

    # buttons that you want to keep state information on
    a_button = constants.button_state["button_up"]
    b_button = constants.button_state["button_up"]
    start_button = constants.button_state["button_up"]
    select_button = constants.button_state["button_up"]

    # get sound ready
    cannon_sound = open("player_cannon.wav", "rb")
    # pirate_boom = open("player_explosion.wav", "rb")
    pirate_boom = open("pirate_explosion.wav", "rb")
    sound = ugame.audio
    sound.stop()
    sound.mute(False)

    # set the background to image 0 in the image bank
    # and the size (10x8 tiles of size 16x16)
    background = stage.Grid(image_bank, 10, 8)

    boat = stage.Sprite(
        image_bank, 1, 74, 56
    )

    boat_sprite = Boat(74, 56)
    
    """pirate_ship_right = stage.Sprite(
        image_bank,
        3,
        (constants.SCREEN_X - (constants.SPRITE_SIZE * 2)),
        56,
    )
    
    pirate_ship_left = stage.Sprite(
        image_bank,
        4,
        (0 + constants.SPRITE_SIZE),
        56,
    )
    
    # create list of pirateships,for both the left and right side
    pirateships_right = []
    for pirateship_number in range(constants.TOTAL_NUMBER_OF_RIGHT_PIRATES):
        a_single_pirateship = stage.Sprite(
            image_bank,
            3,
            constants.OFF_SCREEN_X,
            constants.OFF_SCREEN_Y
        )
        pirateships_right.append(a_single_pirateship)

    pirateships_left = []
    for pirateship_number in range(constants.TOTAL_NUMBER_OF_LEFT_PIRATES):
        a_single_pirateship = stage.Sprite(
            image_bank,
            4,
            constants.OFF_SCREEN_X,
            constants.OFF_SCREEN_Y
        )
        pirateships_left.append(a_single_pirateship)
    
    # place 2 pirateships on the screen
    show_pirateships_right()
    show_pirateships_left()
    
    # create list of cannonballs for when we shoot
    cannonballs = []
    for cannon_ball_number in range(constants.TOTAL_NUMBER_OF_CANNONBALLS):
        a_single_cannon_ball = stage.Sprite(
        image_bank, 
        2, 
        constants.OFF_SCREEN_X, 
        constants.OFF_SCREEN_Y
        )
        cannonballs.append(a_single_cannon_ball)

    """# create a stage for the background to show up on
    # and set the frame rate to 60fps
    game = stage.Stage(ugame.display, 60)

    # set all layers of all sprites, items show up in order
    # game.layers = [score_text] + pirateships_left + pirateships_right + [boat] + cannonballs + [background]
    game.layers = [score_text] + [boat] + [background]

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
                boat_sprite.velocity(-constants.BOAT_SPEED)
                boat.move(boat.x, boat_sprite.y_position)
            else:
                boat_sprite.warp_bottom()
                boat.move(boat.x, boat_sprite.y_position)

        if keys & ugame.K_DOWN:
            if boat.y < constants.OFF_BOTTOM_SCREEN:
                boat_sprite.velocity(constants.BOAT_SPEED)
                boat.move(boat.x, boat_sprite.y_position)
            else:
                boat_sprite.warp_top()
                boat.move(boat.x, boat_sprite.y_position)

        # update game logic
        """if a_button == constants.button_state["button_just_pressed"]:
            for cannon_ball_number in range(len(cannonballs)):
                if cannonballs[cannon_ball_number].x < 0:
                    cannonballs[cannon_ball_number].move(boat.x - 1, boat.y)
                    # sound.play(cannon_sound)
                    break

        if b_button == constants.button_state["button_just_pressed"]:
            for cannon_ball_number in range(len(cannonballs)):
                if cannonballs[cannon_ball_number].x < 0:
                    cannonballs[cannon_ball_number].move(boat.x + 1, boat.y)
                    # sound.play(cannon_sound)
                    break
            
        # each frame move the cannonballs,that have been fired
        for cannon_ball_number in range(len(cannonballs)):
            if cannonballs[cannon_ball_number].x > constants.OFF_SCREEN_Y:
                # check if cannonball is on the left or right side of the ship
                if cannonballs[cannon_ball_number].x > boat.x:
                    cannonballs[cannon_ball_number].move(
                        cannonballs[cannon_ball_number].x + constants.CANNONBALL_SPEED, 
                        cannonballs[cannon_ball_number].y
                    )
                    if cannonballs[cannon_ball_number].x > constants.SCREEN_X:
                        # remove a point if yuor cannonball misses
                        score = score - 1
                        if score < 0:
                            score = 0
                        score_text.clear()
                        score_text.cursor(0, 0)
                        score_text.move(1, 1)
                        score_text.text(f"Score: {score:.0f}")

                        cannonballs[cannon_ball_number].move(
                            constants.OFF_SCREEN_X,
                            constants.OFF_SCREEN_Y
                        )

                if cannonballs[cannon_ball_number].x < boat.x:
                    cannonballs[cannon_ball_number].move(
                        cannonballs[cannon_ball_number].x - constants.CANNONBALL_SPEED, 
                        cannonballs[cannon_ball_number].y
                    )
                    if cannonballs[cannon_ball_number].x < -16:
                        # remove a point if yuor cannonball misses
                        score = score - 1
                        if score < 0:
                            score = 0
                        score_text.clear()
                        score_text.cursor(0, 0)
                        score_text.move(1, 1)
                        score_text.text(f"Score: {score:.0f}")

                        cannonballs[cannon_ball_number].move(
                            constants.OFF_SCREEN_X,
                            constants.OFF_SCREEN_Y
                        )
        
        # each frame move the pirateships across, that are on screen
        for pirateships_number_left in range(len(pirateships_left)):
            if pirateships_left[pirateships_number_left].x > constants.OFF_SCREEN_Y:
                pirateships_left[pirateships_number_left].move(
                    pirateships_left[pirateships_number_left].x + constants.PIRATE_SPEED,
                    pirateships_left[pirateships_number_left].y,
                )
                if pirateships_left[pirateships_number_left].x > constants.SCREEN_X:
                    pirateships_left[pirateships_number_left].move(
                        constants.OFF_SCREEN_X,
                        constants.OFF_SCREEN_Y
                    )

                    # randomly spawn a pirateship on either the left or right side
                    random_number = random.randint(1, 2)
                    if random_number == 1:
                        show_pirateships_left()
                    if random_number == 2:
                        show_pirateships_right()

        for pirateships_number_right in range(len(pirateships_right)):
            if pirateships_right[pirateships_number_right].x > constants.OFF_SCREEN_Y:
                pirateships_right[pirateships_number_right].move(
                    pirateships_right[pirateships_number_right].x - constants.PIRATE_SPEED,
                    pirateships_right[pirateships_number_right].y,
                )
                if pirateships_right[pirateships_number_right].x < -16:
                    pirateships_right[pirateships_number_right].move(
                        constants.OFF_SCREEN_X,
                        constants.OFF_SCREEN_Y
                    )

                    # randomly spawn a pirateship on either the left or right side
                    random_number = random.randint(1, 2)
                    if random_number == 1:
                        show_pirateships_left()
                    if random_number == 2:
                        show_pirateships_right()

        # checks if a cannonball and a pirateship are colliding
        for cannon_ball_number in range(len(cannonballs)):
            if cannonballs[cannon_ball_number].y > constants.OFF_SCREEN_Y:
                for pirate_number in range(len(pirateships_right)):
                    if pirateships_right[pirate_number].y > constants.OFF_SCREEN_Y:
                        if stage.collide(cannonballs[cannon_ball_number].x + 4, cannonballs[cannon_ball_number].y + 4,
                                        cannonballs[cannon_ball_number].x + 12, cannonballs[cannon_ball_number].y + 12,
                                        pirateships_right[pirate_number].x, pirateships_right[pirate_number].y,
                                        pirateships_right[pirate_number].x + 16, pirateships_right[pirate_number].y + 16,):
                            # you hit an alien
                            pirateships_right[pirate_number].move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
                            cannonballs[cannon_ball_number].move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
                            sound.stop()
                            # sound.play(pirate_boom)
                            score = score + 1
                            score_text.clear()
                            score_text.cursor(0, 0)
                            score_text.move(1, 1)
                            score_text.text(f"Score: {score:.0f}")
                            random_number = random.randint(1, 2)
                            if random_number == 1:
                                show_pirateships_left()
                            if random_number == 2:
                                show_pirateships_right()
                            random_number = random.randint(1, 2)
                            if random_number == 1:
                                show_pirateships_left()
                            if random_number == 2:
                                show_pirateships_right()

        # checks if a laser and an alien are colliding
        for cannon_ball_number in range(len(cannonballs)):
            if cannonballs[cannon_ball_number].y > constants.OFF_SCREEN_Y:
                for pirate_number in range(len(pirateships_left)):
                    if pirateships_left[pirate_number].y > constants.OFF_SCREEN_Y:
                        if stage.collide(cannonballs[cannon_ball_number].x + 4, cannonballs[cannon_ball_number].y + 4,
                                        cannonballs[cannon_ball_number].x + 12, cannonballs[cannon_ball_number].y + 12,
                                        pirateships_left[pirate_number].x, pirateships_left[pirate_number].y,
                                        pirateships_left[pirate_number].x + 16, pirateships_left[pirate_number].y + 16,):
                            # you hit an alien
                            pirateships_left[pirate_number].move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
                            cannonballs[cannon_ball_number].move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
                            sound.stop()
                            # sound.play(pirate_boom)
                            score = score + 1
                            score_text.clear()
                            score_text.cursor(0, 0)
                            score_text.move(1, 1)
                            score_text.text(f"Score: {score:.0f}")
                            random_number = random.randint(1, 2)
                            if random_number == 1:
                                show_pirateships_left()
                            if random_number == 2:
                                show_pirateships_right()
                            random_number = random.randint(1, 2)
                            if random_number == 1:
                                show_pirateships_left()
                            if random_number == 2:
                                show_pirateships_right()

        # checks if the boat and an pirateship are colliding
        for pirate_number in range(len(pirateships_left)):
            if pirateships_left[pirate_number].x > 0:
                if stage.collide(
                    pirateships_left[pirate_number].x + 1,
                    pirateships_left[pirate_number].y + 1,
                    pirateships_left[pirate_number].x + 15,
                    pirateships_left[pirate_number].y + 15,
                    boat.x + 6,
                    boat.y + 3,
                    boat.x + 10,
                    boat.y + 13,
                ):
                    # alien hit the ship
                    sound.stop()
                    # sound.play(pirate_boom)
                    time.sleep(3.0)
                    game_over_scene(score)

        # checks if the boat and an pirateship are colliding
        for pirate_number in range(len(pirateships_right)):
            if pirateships_right[pirate_number].x > 0:
                if stage.collide(
                    pirateships_right[pirate_number].x + 1,
                    pirateships_right[pirate_number].y + 1,
                    pirateships_right[pirate_number].x + 15,
                    pirateships_right[pirate_number].y + 15,
                    boat.x + 6,
                    boat.y + 3,
                    boat.x + 10,
                    boat.y + 13,
                ):
                    # alien hit the ship
                    sound.stop()
                    # sound.play(pirate_boom)
                    time.sleep(3.0)
                    game_over_scene(score)

        """# redraw sprites
        # game.render_sprites(pirateships_left + pirateships_right + [boat] + cannonballs)
        game.render_sprites([boat])
        game.tick()


def game_over_scene(final_score):
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
        width=29, height=14, font=None, palette=constants.BLUE_PALETTE, buffer=None
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