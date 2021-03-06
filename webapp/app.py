# SPDX-FileCopyrightText: © 2020 The insulin-reminder Authors
# SPDX-License-Identifier: MIT

import datetime
import json

import flask

app = flask.Flask("Insulin Reminder")


@app.route("/status_led")
def status_led():

    try:
        with open("last_button_click.json", mode="rt") as f:
            data = json.load(f)
    except Exception:
        data = {}

    if "last_button_click" in data:
        last_button_click = datetime.datetime.fromisoformat(data["last_button_click"])
    else:
        last_button_click = None

    if last_button_click:
        now = datetime.datetime.now()
        threshold = datetime.datetime(now.year, now.month, now.day, 5, 0)

        if now.hour < 5:
            threshold -= datetime.timedelta(days=1)

        if last_button_click > threshold:
            return flask.jsonify({"led": 0xFF4000, "refresh": 3600})

    return flask.jsonify({"led": 0x800000, "refresh": 30})


@app.route("/button_clicked", methods=["POST"])
def button_clicked():
    with open("last_button_click.json", mode="wt") as f:
        json.dump({"last_button_click": datetime.datetime.now().isoformat()}, f)

    return flask.jsonify()
