# SPDX-FileCopyrightText: 2020 The insulin-reminder Authors
# SPDX-FileCopyrightText: Copyright (c) 2019 ladyada for Adafruit Industries
#
# SPDX-License-Identifier: MIT

import secrets
import time

import adafruit_requests as requests
import adafruit_rgbled
import board
import busio
import neopixel
from adafruit_esp32spi import (
    adafruit_esp32spi,
    adafruit_esp32spi_socket,
    adafruit_esp32spi_wifimanager,
)
from digitalio import DigitalInOut

pixel = neopixel.NeoPixel(board.NEOPIXEL, 1, brightness=0.2)
pixel[0] = (0, 0, 0)

insulin_light = adafruit_rgbled.RGBLED(board.D5, board.D6, board.D9)
# Start the light blue, to make it clear it's just configuring.
insulin_light.color = (0, 0, 0x10)

print("ESP32 SPI Setup")

esp32_cs = DigitalInOut(board.D13)
esp32_ready = DigitalInOut(board.D11)
esp32_reset = DigitalInOut(board.D12)

spi = busio.SPI(board.SCK, board.MOSI, board.MISO)
esp = adafruit_esp32spi.ESP_SPIcontrol(spi, esp32_cs, esp32_ready, esp32_reset)

if esp.status != adafruit_esp32spi.WL_IDLE_STATUS:
    print("Something went wrong.")

print("Firmware vers. %s" % esp.firmware_version)
print("MAC addr: %02x:%02x:%02x:%02x:%02x:%02x" % tuple(esp.MAC_address))

while True:
    # While connecting set the light purpleish.
    insulin_light.color = (156, 0, 255)

    wifi = adafruit_esp32spi_wifimanager.ESPSPI_WiFiManager(esp, secrets.WIFI_SECRETS)
    wifi.connect()

    print("Connected to %s" % secrets.WIFI_SECRETS["ssid"])

    requests.set_socket(adafruit_esp32spi_socket, esp)

    while True:
        try:
            response = requests.get(secrets.URL)
            response_parsed = response.json()

            if "led" in response_parsed:
                led_color = int(response_parsed["led"])

            if "refresh" in response_parsed:
                refresh_time = int(response_parsed["refresh"])
            else:
                refresh_time = 60

            print(
                "Last LED status: #%06x. Refresh time: %d seconds"
                % (led_color, refresh_time)
            )

            insulin_light.color = led_color
            response.close()
            time.sleep(refresh_time)
        except Exception as e:
            # This is an annoying way to detect the dropped WiFi. If for whatever reason
            # the WiFi dropped (e.g. rebooted Access Point), the `requests.get()` call
            # will fail, as it can't read data.
            #
            # This leads to a RuntimeError() with the following string being returned over
            # and over.
            if str(e) == "Expected 01 but got 00":
                print("WiFi disconnected, retrying.")
                break
            print(str(e))
            pass
