from flask import Flask

import tv_rs232

app = Flask(__name__)
tv = tv_rs232.TV()


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/tv/hdmi")
def hdmi():
    tv.command("INPUT-HDMI")
    return "ok"


@app.route("/tv/dp")
def dp():
    tv.command("INPUT-DP")
    return "ok"


@app.route("/tv/pip/on")
def pip_on():
    tv.command("PIP-TR")
    return "ok"


@app.route("/tv/pip/off")
def pip_off():
    tv.command("PIP-OFF")
    return "ok"


@app.route("/tv/pip/hdmi")
def pip_hdmi():
    tv.command("PIP-S-HDMI")
    return "ok"


@app.route("/tv/pip/dp")
def pip_dp():
    tv.command("PIP-S-DP")
    return "ok"
