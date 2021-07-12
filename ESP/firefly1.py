# Firefly simulation
# Converted from original code for Raspberry Pi Pico ws2812b driver
# G.D. Walters 25 May, 2021
# -------------------------------------------------
# This program combines the Neopixel capabilities with a touchpad lead to act as a button
# -------------------------------------------------

import time, random, neopixel
# import ws2812b
# import random
import machine
from machine import TouchPad

# setup Touchpad 
tpad = TouchPad(machine.Pin(14))
numpix = 24  # 8  # Number of NeoPixels
p = 16  # 12
# Pin where NeoPixels are connected
# strip = ws2812b.ws2812b(numpix, 0,16)
np = neopixel.NeoPixel(machine.Pin(p), numpix)

colors = [
    [232, 100, 255],  # Purple
    [200, 200, 20],  # Yellow
    [30, 200, 200],  # Blue
    [150,50,10],
    [50,200,10],
]

def clear():
  for i in range(numpix):
    np[i] = (0, 0, 0)
    np.write()
    
max_len=20
min_len = 5
#pixelnum, posn in flash, flash_len, direction
flashing = []

num_flashes = 10

for i in range(num_flashes):
    pix = random.randint(0, numpix - 1)
    col = random.randint(1, len(colors) - 1)
    flash_len = random.randint(min_len, max_len)
    flashing.append([pix, colors[col], flash_len, 0, 1])
    
# strip.fill(0,0,0)
for cntr in range(numpix):
    np[cntr]=(0,0,0)
    np.write()

# while True:
loopit = True
while loopit:
    # strip.show()
    tval = tpad.read()
    if tval <= 125:  # 200:
        loopit = False    
    np.write()
    for i in range(num_flashes):

        pix = flashing[i][0]
        brightness = (flashing[i][3]/flashing[i][2])
        colr = (int(flashing[i][1][0]*brightness), 
                int(flashing[i][1][1]*brightness), 
                int(flashing[i][1][2]*brightness))
        # strip.set_pixel(pix, colr[0], colr[1], colr[2])
        np[pix]=(colr[0],colr[1],colr[2])

        if flashing[i][2] == flashing[i][3]:
            flashing[i][4] = -1
        if flashing[i][3] == 0 and flashing[i][4] == -1:
            pix = random.randint(0, numpix - 1)
            col = random.randint(0, len(colors) - 1)
            flash_len = random.randint(min_len, max_len)
            flashing[i] = [pix, colors[col], flash_len, 0, 1]
        flashing[i][3] = flashing[i][3] + flashing[i][4]
        # time.sleep(0.005)
        time.sleep(0.015)

clear()
print('Program Terminated...')