# SPDX-FileCopyrightText: © 2020 The insulin-reminder Authors
# SPDX-License-Identifier: MIT
"""Simple Feather M4/M0 compatible code to cycle the connected RGB LEDs.

This code simply runs through the three colours (Red, Green, Blue) at five different
intensities, one second each, terminating with 10 seconds of "yellow".

It is intended to test that the connection of the LEDs are correct, both in terms of
wiring and in term of configuration of the pins.
"""

import time

import adafruit_rgbled
import board
import neopixel

# Turn off the on-board neopixel, it's annoying while developing.
board_pixel = neopixel.NeoPixel(board.NEOPIXEL, 1, brightness=0.2)
board_pixel[0] = (0, 0, 0)

print("Pixel off?")

my_light = adafruit_rgbled.RGBLED(board.D5, board.D6, board.D9)

while True:
    print("Red")
    my_light.color = (0x10, 0x0, 0x0)
    time.sleep(1)
    my_light.color = (0x20, 0x0, 0x0)
    time.sleep(1)
    my_light.color = (0x40, 0x0, 0x0)
    time.sleep(1)
    my_light.color = (0x80, 0x0, 0x0)
    time.sleep(1)
    my_light.color = (0xFF, 0x0, 0x0)
    time.sleep(1)

    print("Green")
    my_light.color = (0x0, 0x10, 0x0)
    time.sleep(1)
    my_light.color = (0x0, 0x20, 0x0)
    time.sleep(1)
    my_light.color = (0x0, 0x40, 0x0)
    time.sleep(1)
    my_light.color = (0x0, 0x80, 0x0)
    time.sleep(1)
    my_light.color = (0x0, 0xFF, 0x0)
    time.sleep(1)

    print("Blue")
    my_light.color = (0x0, 0x0, 0x10)
    time.sleep(1)
    my_light.color = (0x0, 0x0, 0x20)
    time.sleep(1)
    my_light.color = (0x0, 0x0, 0x40)
    time.sleep(1)
    my_light.color = (0x0, 0x0, 0x80)
    time.sleep(1)
    my_light.color = (0x0, 0x0, 0xFF)
    time.sleep(1)

    print("Yellow")
    my_light.color = (0xFF, 0x40, 0)
    time.sleep(10)
