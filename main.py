from flask import Flask, render_template

app = Flask(__name__)


import asyncio

from pywizlight import wizlight, PilotBuilder, discovery


@app.route('/')
def index():
    return 'heloo 2'

@app.route('/ChangeClr')
def ChangeClr():
    light = wizlight("192.168.1.41", port=38899)
    light.turn_on(PilotBuilder(rgb = (255, 000, 000)))
    print('Done')
    return 'Light Changed to red'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
