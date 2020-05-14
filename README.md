<!--
SPDX-FileCopyrightText: 2020 The insulin-reminder Authors

SPDX-License-Identifier: MIT
-->

# Insulin Reminder Light

This repository contains the [CircuitPython](https://circuitpython.org) and
[Flask](https://palletsprojects.com/p/flask/) code that I (Flameeyes) wrote to buildmy
insulin reminder light.

For further details on the project, check [my blog
post](https://flameeyes.blog/2020/05/11/insulin-routine-lockdown-and-electronics/).

## Hardware Configuration

The code in `feather/` is designed to run on an [Adafruit Feather M4
Express](https://www.adafruit.com/product/3857) with an [Airlift
FeatherWing](https://www.adafruit.com/product/4264).

It expects that a PWM-capable RGB LED is controlled by D5 (Red), D6 (Green), and D9
(Blue), and a configuration file modelled after `settings.py` for WiFi access and URL to
receive configuration as.
