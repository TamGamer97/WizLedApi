from flask import Flask, render_template

app = Flask(__name__)


import asyncio

from pywizlight import wizlight, PilotBuilder, discovery


@app.route('/')
def index():
    return 'heloo'

@app.route('/ChangeClr')
async def ChangeClr():
    light = wizlight("192.168.1.41", port=38899)
    await light.turn_on(PilotBuilder())
    await light.turn_on(PilotBuilder(rgb = (255, 000, 000)))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
