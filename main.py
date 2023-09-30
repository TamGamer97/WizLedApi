from flask import Flask, render_template

app = Flask(__name__)


import asyncio

from pywizlight import wizlight, PilotBuilder, discovery


@app.route('/')
def index():
    return 'heloo 2'

@app.route('/ChangeClr')
async def ChangeClr():
    # light = wizlight("192.168.1.41", port=38899)
    # await light.turn_on(PilotBuilder(rgb = (255, 000, 000)))
    # print('Done')
    # return 'Light Changed to red'

    bulbs = await discovery.discover_lights(broadcast_space="192.168.1.255")
    print("Bulb IP address & Port: "+ str(bulbs[0].ip) + " " + str(bulbs[0].port))
    for bulb in bulbs:
        print('Turning bulb off')
        # Turn off all available bulbs
        await bulb.turn_off()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
