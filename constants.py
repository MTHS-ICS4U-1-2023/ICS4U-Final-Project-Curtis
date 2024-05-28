# !/usr/bin/env python3

"""
Created by: Curtis Edwards
Created on: Mar 2023
This constants file is for Space Alien game
"""

# PyBadge screen size is 160x128 and sprites are 16x16
SCREEN_X = 160
SCREEN_Y = 128
SCREEN_GRID_X = 10
SCREEN_GRID_Y = 8
SPRITE_SIZE = 16

TOTAL_NUMBER_OF_LEFT_PIRATES = 3
TOTAL_NUMBER_OF_RIGHT_PIRATES = 3
TOTAL_NUMBER_OF_CANNONBALLS = 4
BOAT_SPEED = 1
PIRATE_SPEED = 1
CANNONBALL_SPEED = 2

OFF_SCREEN_X = -100
OFF_SCREEN_Y = -100
OFF_TOP_SCREEN = -12
OFF_BOTTOM_SCREEN = SCREEN_Y - 6
OFF_LEFT_SCREEN = -12
OFF_RIGHT_SCREEN = SCREEN_X - 6
FPS = 60

# Using for button state
button_state = {
    "button_up": "up",
    "button_just_pressed": "just pressed",
    "button_still_pressed": "still pressed",
    "button_released": "released",
}

# pallets for filled text
WHITE_BLACK_PALETTE = (
    b"\xf8\x1f\x00\x00\xcey\xff\xff\xf8\x1f\x00\x19\xfc\xe0\xfd\xe0"
    b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
)
RED_PALETTE = (
    b"\xff\xff\x00\x00\xcey\x66\xff\xff\xff\xff\xff\xff\xff\xfd\xe0"
    b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
)
BLUE_PALETTE = (
    b"\xff\xff\x00\x22\xcey\x22\xff\xff\xff\xff\xff\xff\xff\xff\xff"
    b"\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff"
)